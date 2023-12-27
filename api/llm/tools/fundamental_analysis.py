# Fundamental Analysis
from financetoolkit import Toolkit
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
from langchain.tools import tool
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.output_parsers import CommaSeparatedListOutputParser

from llm.prompts import RATIOS_PROMPT_TEMPLATE, MACRO_ECONOMICS_PROMPT
from llm.tools.schemas.fundamental_analysis import *
from llm.tools.constants import *


def get_list(query: str, prompt_template: str, invoke_input: dict):

    format_instructions = CommaSeparatedListOutputParser().get_format_instructions()

    prompt = PromptTemplate(template=prompt_template,
                            input_variables=['input'],
                            partial_variables={
                                'format_instructions': format_instructions,
                                })

    gemini = ChatGoogleGenerativeAI(model='gemini-pro', temperature=0)
    llm_chain = LLMChain(
        prompt=prompt,
        llm=gemini,
    )
    return llm_chain.invoke(invoke_input)['text'].split(', ')

@tool(args_schema=GetRatios)
def ratios(tickers: List[str], query: str):
    """Get all year wise specified fundamental ratios of the company"""
    ratios = Toolkit(tickers, api_key=FMP_API_KEY).ratios.collect_all_ratios().stack().reset_index()

    input_dict = {
        'input': query,
        'efficiency_ratios': EFFICIENCY_RATIOS,
        'liquidity_ratios': LIQUIDITY_RATIOS,
        'profitability_ratios': PROFITABILITY_RATIOS,
        'solvency_ratios': SOLVENCY_RATIOS,
        'valuation_ratios': VALUATION_RATIOS
    }
    required_ratios = get_list(query, RATIOS_PROMPT_TEMPLATE, input_dict)

    ratios.columns = ['Ticker', 'Ratio', 'Year', 'Value']
    df = ratios.pivot_table(values='Value', columns='Ratio', index=['Ticker', 'Year']).reset_index()
    rows = math.ceil(len(required_ratios) / 3)
    df = df[['Ticker', 'Year']+required_ratios]
    df['Year'] = df['Year'].astype(str)

    fig = plt.figure(figsize=(15, rows*5))

    for index, ratio in enumerate(required_ratios):
        partial_df = df[['Ticker', 'Year', ratio]]
        ax = plt.subplot(rows, 3, index+1)
        sns.lineplot(data=partial_df, x='Year', y=ratio, hue='Ticker', ax=ax)
        plt.title(f'Comparison of {ratio} across years')
        plt.legend()

    plt.tight_layout()
    fig.show()

    return fig, df

@tool(args_schema=GetRisk)
def risk(tickers: List[str], required_metrics: List[RiskMetrics]):
    """Get all Specified metrics of risk of the companies in graphical format"""
    risk = Toolkit(tickers, api_key=FMP_API_KEY).risk
    functions_dict = {
        'Garch Forecast': risk.get_garch_forecast,
        'Garch': risk.get_garch,
        'Conditional Value At Risk (CVaR)': risk.get_conditional_value_at_risk,
        'Entropic Value At Risk (EVaR)': risk.get_entropic_value_at_risk,
        'Kurtosis': risk.get_kurtosis,
        'Maximum Drawdown': risk.get_maximum_drawdown,
        'Skewness': risk.get_skewness,
        'Ulcer Index': risk.get_ulcer_index,
        'Value At Risk (VaR)': risk.get_value_at_risk
    }

    rows = math.ceil(len(required_metrics) / 3)
    fig = plt.figure(figsize=(15, rows*5))

    overall_df = pd.DataFrame()

    for index, metric in enumerate(required_metrics):
        df = functions_dict[metric]()
        overall_df = pd.concat([overall_df, df], axis=1)
        ax = plt.subplot(rows, 3, index+1)
        df.plot(ax=ax)
        plt.title(f'Comparison of {metric} across years')
        plt.legend()

    plt.tight_layout()
    fig.show()

    return fig, overall_df

@tool(args_schema=GetModels)
def models(tickers: List[str], required_models: List[ModelMetrics]):
    """Get all Specified models of the companies in graphical format"""
    models = Toolkit(tickers, api_key=FMP_API_KEY).models
    functions_dict = {
        'Weighted Average Cost of Capital': models.get_weighted_average_cost_of_capital,
        'Altman Z-Score': models.get_altman_z_score,
        'Dupont Analysis': models.get_dupont_analysis,
        'Enterprise Value Breakdown': models.get_enterprise_value_breakdown,
        'Intrinsic Valuation': models.get_intrinsic_valuation,
        'Piotroski Score': models.get_piotroski_score
    }
    rows = math.ceil(len(required_models) / 3)
    fig = plt.figure(figsize=(15, rows*5))

    for index, metric in enumerate(required_models):
        df = functions_dict[metric]()
        ax = plt.subplot(rows, 3, index+1)
        df.plot(ax=ax)
        plt.title(f'Comparison of {metric} across years')
        plt.legend()

    plt.tight_layout()
    fig.show()

    return fig

@tool(args_schema=GetPerformance)
def performance(tickers: List[str], required_metrics:List[PerformanceMetrics]):
    """Get all performance indicators of the companies"""
    performance = Toolkit(tickers, api_key=FMP_API_KEY).performance
    functions_dict = {
        'Beta': performance.get_beta,
        'Alpha': performance.get_alpha,
        'Capital Asset Pricing Model': performance.get_capital_asset_pricing_model,
        'Information Ratio': performance.get_information_ratio,
        'Jensens Alpha': performance.get_jensens_alpha,
        'M2 Ratio': performance.get_m2_ratio,
        'Sharpe Ratio': performance.get_sharpe_ratio,
        'Treynor Ratio': performance.get_treynor_ratio,
        'Sortino Ratio': performance.get_sortino_ratio,
        'Ulcer Performance Index': performance.get_ulcer_performance_index,
        'Tracking Error': performance.get_tracking_error
    }
    rows = math.ceil(len(required_metrics) / 3)
    fig = plt.figure(figsize=(15, rows*5))

    for index, metric in enumerate(required_metrics):
        df = functions_dict[metric]()
        ax = plt.subplot(rows, 3, index+1)
        df.plot(ax=ax)
        plt.title(f'Comparison of {metric} across years')
        plt.legend()

    plt.tight_layout()
    fig.show()

    return fig

# @tool(args_schema=GetAdditionalPerformance)
# def additional_performance(tickers: List[str], required_metrics: List[AdditionalPerformanceMetrics]):
#     """Additional Performance Metrics"""
#     functions_dict = {
#         'Compound Growth Rate': performance.get_compound_growth_rate,
#         'Factor Asset Correlations': performance.get_factor_asset_correlations,
#         'Factor Correlations': performance.get_factor_correlations,
#         'FAMA and FRENCH model': performance.get_fama_and_french_model,
#     }

@tool(args_schema=GetMacroEconomics)
def macro_economics(required_metrics: List[MacroEconomicMetrics], query: str):
    """To Analyze the Macro Economic Data"""
    economics = Toolkit(['MSFT'], api_key=os.getenv('FMP_FMP_API_KEY')).economics
    func_dict = {
        'Unemployment Rate': economics.get_unemployment_rate,
        'Composite Leading Indicator': economics.get_composite_leading_indicator,
        'Consumer Confidence Index': economics.get_consumer_confidence_index,
        'Consumer Price Index (CPI)': economics.get_consumer_price_index,
        'Business Confidence Index': economics.get_business_confidence_index,
        'Exchange Rates': economics.get_exchange_rates,
        'Composite Leading Indicators': economics.get_composite_leading_indicator,
        'Gross Domestic Product (GDP)': economics.get_gross_domestic_product,
        'Gross Domestic Product Forecast (GDP)': economics.get_gross_domestic_product_forecast,
        'Long Term Interest Rate': economics.get_long_term_interest_rate,
        'House Prices': economics.get_house_prices,
        'Producer Price Index': economics.get_producer_price_index,
        'Purchasing Power Parity (PPP)': economics.get_purchasing_power_parity,
        'Rent Prices': economics.get_rent_prices,
        'Short Term Interest Rate': economics.get_short_term_interest_rate,
    }
    countries = list(economics.get_gross_domestic_product_forecast().columns)
    countries_list  = get_list(query, MACRO_ECONOMICS_PROMPT, {'input': query, 'countries': countries})
    dataframes = []

    for metric in required_metrics:
        data = func_dict[metric]()[countries_list]
        dataframes.append(data)

    df = pd.concat(dataframes, axis=1, keys=required_metrics)

    return df


fundamental_tools = [ratios, risk, models, performance, macro_economics]