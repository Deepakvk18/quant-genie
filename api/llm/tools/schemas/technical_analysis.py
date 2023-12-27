# Technical Analysis Schemas
from pydantic.v1 import BaseModel, Field
from typing import List
from enum import Enum

class TechnicalIndicators(str, Enum):
    exponential_moving_average = 'Exponential Moving Average'
    ichimoku_cloud = 'Ichimoku Cloud'
    advancers_decliners = 'Advancers Decliners'
    aroon_indicator = 'Aroon Indicator'
    accumulation_distribution_line = 'Accumulation Distribution Line'
    average_directional_index = 'Average Directional Index'
    average_true_range = 'Average True Range'
    balance_of_power = 'Balance of Power'
    bollinger_bands = 'Bollinger Bands'
    chaikin_oscillator = 'Chaikin Oscillator'
    chande_momentum_oscillator = 'Chande Momentum Oscillator'
    force_index = 'Force Index'
    commodity_channel_index = 'Commodity Channel index'
    detrended_price_oscillator = 'Detrended Price Oscillator'
    keltner_channels = 'Keltner Channels'
    mcclellan_oscillator = 'Mcclellan Oscillator'
    moving_average = 'Moving Average'
    money_flow_index = 'Money Flow Index'
    on_balance_volume = 'On Balance Volume'
    percentage_price_oscillator = 'Percentage Price Oscillator'
    relative_strength_index = 'Relative Strength Index'
    stochastic_oscillator = 'Stochastic Oscillator'
    relative_vigor_index = 'Relative Vigor Index'
    triangular_moving_average = 'Triangular Moving Average'
    trix = 'Trix'
    true_range = 'True Range'
    ultimate_oscillator = 'Ultimate Oscillator'
    williams_percent_r = 'Williams Percent R'

class GetTechnicalIndicators(BaseModel):
    ticker: str = Field(description="Company ticker symbol for which the analysis is to be conducted")
    required_indicators: List[TechnicalIndicators] = Field(description="List of Indicators the user has requested for")