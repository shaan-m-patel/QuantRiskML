# QuantRiskML

## Project Overview
QuantRiskML is a comprehensive Python framework designed for quantitative finance, integrating machine learning for risk premia prediction with advanced derivatives pricing and dynamic hedging strategies.

## Features
- **Machine Learning**: Predict equity risk premia using models like Random Forest and XGBoost.
- **Derivatives Pricing**: Price options using Black-Scholes and Binomial models; calculate Greeks (Delta, Gamma, Vega, Theta).
- **Dynamic Hedging**: Implement and backtest dynamic hedging strategies (e.g., Delta-Neutral).
- **Backtesting**: Robust backtesting engine with visualization of PnL and risk metrics.

## Project Structure
```
QuantRiskML/
├── data/               # Data storage
│   ├── raw/            # Raw input data
│   └── processed/      # Cleaned and transformed data
├── src/                # Source code
│   ├── data_loader.py  # Data ingestion and preprocessing
│   ├── ml_models.py    # Machine learning models for risk premia
│   ├── pricing.py      # Options pricing engines (Black-Scholes, Binomial)
│   ├── hedging.py      # Hedging strategies
│   └── backtest.py     # Backtesting framework
├── notebooks/          # Jupyter notebooks for exploration
├── tests/              # Unit tests
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd QuantRiskML
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Provide the EODHD API token at runtime**

   `src/dataExploration/dataloader.ipynb` reads the token from the environment. Create or rotate a token in the EODHD dashboard, then export it in the shell that launches Jupyter:

   ```bash
   export EODHD_API_TOKEN="your-token"
   ```

   Do not paste the token into a notebook, source file, or commit. `.env` is gitignored for local use; load it into the environment before starting Jupyter. The notebook does not read `.env` on its own.

## Usage
Check the `notebooks/` directory for example usage of the modules.
