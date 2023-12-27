# Fundamental Analysis Schemas
from pydantic.v1 import BaseModel, Field
from typing import List, Optional
from enum import Enum

class RiskMetrics(str, Enum):
    garch_forecast = 'Garch Forecast'
    garch = 'Garch'
    conditional_value_at_risk = 'Conditional Value At Risk (CVaR)'
    entropic_value_at_risk = 'Entropic Value At Risk (EVaR)'
    kurtosis = 'Kurtosis'
    maximum_drawdown = 'Maximum Drawdown'
    skewness = 'Skewness'
    ulcer_index = 'Ulcer Index'
    value_at_risk ='Value At Risk (VaR)'

class ModelMetrics(str, Enum):
    weighted_average_cost_of_capital = 'Weighted Average Cost of Capital'
    altman_z_score = 'Altman Z-Score'
    dupont_analysis = 'Dupont Analysis'
    enterprise_value_breakdown = 'Enterprise Value Breakdown'
    intrinsic_valuation = 'Intrinsic Valuation'
    piiotroski_score = 'Piotroski Score'

class PerformanceMetrics(str, Enum):
    beta = 'Beta'
    alpha = 'Alpha'
    capital_asset_pricing_model = 'Capital Asset Pricing Model'
    information_ratio = 'Information Ratio'
    jensens_alpha = 'Jensens Alpha'
    m2_ratio = 'M2 Ratio'
    sharpe_ratio = 'Sharpe Ratio'
    treynor_ratio = 'Treynor Ratio'
    sortino_ratio = 'Sortino Ratio'
    ulcer_performance_index = 'Ulcer Performance Index'
    tracking_error = 'Tracking Error'

class AdditionalPerformanceMetrics(str, Enum):
    compoun_growth_rate = 'Compound Growth Rate'
    factor_asset_correlations = 'Factor Asset Correlations'
    factor_correlations = 'Factor Correlations'
    fama_and_french_model = 'FAMA and FRENCH model'

class MacroEconomicMetrics(str, Enum):
    unemployment_rate = 'Unemployment Rate'
    business_confidence_index = 'Business Confidence Index'
    composite_leading_indicator = 'Composite Leading Indicator'
    consumer_confidence_index = 'Consumer Confidence Index'
    consumer_price_index = 'Consumer Price Index (CPI)'
    exchange_rates = 'Exchange Rates'
    composite_leading_indicators = 'Composite Leading Indicators'
    gross_domestic_product = 'Gross Domestic Product (GDP)'
    gross_domestic_product_forecast = 'Gross Domestic Product Forecast (GDP)'
    long_term_interest_rate = 'Long Term Interest Rate'
    house_prices = 'House Prices'
    producer_price_index = 'Producer Price Index'
    purchasing_power_parity = 'Purchasing Power Parity (PPP)'
    rent_prices = 'Rent Prices'
    short_term_interest_rate = 'Short Term Interest Rate'

class GetRatios(BaseModel):
    tickers: List[str] = Field(description="List of companies ticker symbols")
    query: str = Field(description="User's query string")

class GetRisk(BaseModel):
    tickers: List[str] = Field(description="List of companies ticker symbols")
    required_metrics: List[RiskMetrics] = Field(description="Risk Metrics the user has requested for")

class GetModels(BaseModel):
    tickers: List[str] = Field(description="List of companies ticker symbols")
    required_models: List[ModelMetrics] = Field(description="Models the user has requested for")

class GetPerformance(BaseModel):
    tickers: List[str] = Field(description="List of companies ticker symbols")
    required_metrics: List[PerformanceMetrics] = Field(description="Performance Metrics the user has requested for")

class GetAdditionalPerformance(BaseModel):
    tickers: List[str] = Field(description="List of companies ticker symbols")
    required_metrics: List[AdditionalPerformanceMetrics] = Field(description="Performance Metrics the user has requested for")

class GetMacroEconomics(BaseModel):
    required_metrics: List[MacroEconomicMetrics]
    query: str
