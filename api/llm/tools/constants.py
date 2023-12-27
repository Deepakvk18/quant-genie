import os
from financetoolkit import Toolkit
from dotenv import load_dotenv

load_dotenv()

# companies = Toolkit(
#     ["AAPL", "MSFT", "GOOGL", "AMZN"], api_key=os.environ['FMP_API_KEY'], start_date="2005-01-01"
# )

# EFFICIENCY_RATIOS = list(companies.ratios.collect_efficiency_ratios().reset_index()['level_1'])
# LIQUIDITY_RATIOS = list(companies.ratios.collect_liquidity_ratios().reset_index()['level_1'])
# PROFITABILITY_RATIOS = list(companies.ratios.collect_profitability_ratios().reset_index()['level_1'])
# SOLVENCY_RATIOS = list(companies.ratios.collect_solvency_ratios().reset_index()['level_1'])
# PROFITABILITY_RATIOS = list(companies.ratios.collect_profitability_ratios().reset_index()['level_1'])
# VALUATION_RATIOS = list(companies.ratios.collect_valuation_ratios().reset_index()['level_1'])

FMP_API_KEY = os.getenv("FMP_API_KEY")