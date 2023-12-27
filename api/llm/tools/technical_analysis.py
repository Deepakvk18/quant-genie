# Technical Analysis
import os
import math
from financetoolkit import Toolkit
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from langchain.tools import tool
from typing import List

from llm.tools.schemas.technical_analysis import *
from llm.tools.constants import *

@tool(args_schema=GetTechnicalIndicators)
def technicals(ticker: str, required_indicators: List[TechnicalIndicators]):
    """Get all Specified Technical Indicators of the companies"""

    companies = Toolkit([ticker], api_key=FMP_API_KEY, start_date='2015-01-01')
    technicals = companies.technicals
    history = companies.get_historical_data()['Close'][ticker]
    history.columns = ['Stock Prices']
    functions_dict = {
        'Exponential Moving Average': technicals.get_exponential_moving_average,
        'Ichimoku Cloud': technicals.get_ichimoku_cloud,
        'Advancers Decliners': technicals.get_advancers_decliners,
        'Aroon Indicator': technicals.get_aroon_indicator,
        'Accumulation Distribution Line': technicals.get_accumulation_distribution_line,
        'Average Directional Index': technicals.get_average_directional_index,
        'Average True Range': technicals.get_average_true_range,
        'Balance of Power': technicals.get_balance_of_power,
        'Bollinger Bands': technicals.get_bollinger_bands,
        'Chaikin Oscillator': technicals.get_chaikin_oscillator,
        'Chande Momentum Oscillator': technicals.get_chande_momentum_oscillator,
        'Force Index': technicals.get_force_index,
        'Commodity Channel index': technicals.get_commodity_channel_index,
        'Detrended Price Oscillator': technicals.get_detrended_price_oscillator,
        'Keltner Channels': technicals.get_keltner_channels,
        'Mcclellan Oscillator': technicals.get_mcclellan_oscillator,
        'Moving Average': technicals.get_moving_average,
        'Money Flow Index': technicals.get_money_flow_index,
        'On Balance Volume': technicals.get_on_balance_volume,
        'Percentage Price Oscillator': technicals.get_percentage_price_oscillator,
        'Relative Strength Index': technicals.get_relative_strength_index,
        'Stochastic Oscillator': technicals.get_stochastic_oscillator,
        'Relative Vigor Index': technicals.get_relative_vigor_index,
        'Triangular Moving Average': technicals.get_triangular_moving_average,
        'Trix': technicals.get_trix,
        'True Range': technicals.get_true_range,
        'Ultimate Oscillator': technicals.get_ultimate_oscillator,
        'Williams Percent R': technicals.get_williams_percent_r
    }
    rows = math.ceil((len(required_indicators) + 1) / 3)
    fig = plt.figure(figsize=(15, rows*5))

    dataframes = [history]

    ax = plt.subplot(rows, 3, 1)
    history.plot(ax=ax)
    plt.title(f'Trend for {ticker}')

    for index, indicator in enumerate(required_indicators):
        df = functions_dict[indicator]()
        # print(df.columns)
        if len(list(df.columns)) == 1:

            df.columns = [indicator]
        else:
            cols = []
            for col in df.columns:
                cols.append(col[0])
            df.columns = cols
        dataframes.append(df)
        ax = plt.subplot(rows, 3, index+2)
        df.plot(ax=ax)
        plt.title(f'{indicator} for {ticker}')
        plt.legend()

    plt.tight_layout()
    plt.suptitle(f'Technical Analysis of {ticker}')
    fig.show()

    df = pd.concat(dataframes, axis=1)

    return fig, df[-22:]

technical_tools = [technicals]