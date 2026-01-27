# AI Investment Advisory System

An intelligent investment advisory system powered by autonomous agents that provide comprehensive market analysis, risk assessment, and portfolio recommendations.

## Features

- **Market Analysis Agent**: Analyzes market data and identifies trends
- **Risk Assessor Agent**: Evaluates portfolio and market risks
- **Portfolio Advisor Agent**: Provides portfolio recommendations and adjustments
- **Real-time Data Processing**: Fetches and processes market data
- **Risk Management**: Implements risk mitigation strategies
- **Portfolio Rebalancing**: Suggests optimal portfolio adjustments

## Project Structure

```
ai-investment-advisory-system/
├── agents/                    # AI Agent implementations
│   ├── market_analyst.py     # Market analysis agent
│   ├── risk_assessor.py      # Risk assessment agent
│   └── portfolio_advisor.py  # Portfolio recommendation agent
├── tasks/                     # Task workflows
│   ├── market_analysis_task.py
│   ├── risk_analysis_task.py
│   └── portfolio_task.py
├── data/                      # Data management
│   └── stock_data.py         # Stock data fetching and caching
├── utils/                     # Utilities
│   └── config.py             # Configuration management
├── main.py                    # Application entry point
├── requirements.txt           # Python dependencies
├── docker/                    # Docker configuration
│   └── Dockerfile
└── README.md
```

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai-investment-advisory-system
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

## Usage

### Run the advisory system
```bash
python main.py
```

### Run specific tasks
```python
from tasks.portfolio_task import PortfolioTask

portfolio = {
    "AAPL": {"shares": 100, "value": 25000},
    "MSFT": {"shares": 50, "value": 20000}
}

task = PortfolioTask()
results = task.execute(portfolio)
```

### Run with Docker
```bash
docker build -f docker/Dockerfile -t ai-advisor .
docker run ai-advisor
```

## Configuration

Configuration is managed through `utils/config.py` and environment variables:

- `API_KEY`: API key for market data provider
- `DATA_SOURCE`: Data provider (yfinance, etc.)
- `CACHE_ENABLED`: Enable/disable data caching
- `CACHE_TTL`: Cache time-to-live in seconds
- `LOG_LEVEL`: Logging level (DEBUG, INFO, WARNING, ERROR)

## Architecture

The system follows an agent-based architecture:

1. **Market Analyst**: Processes market data and identifies trends
2. **Risk Assessor**: Evaluates risks and provides mitigation strategies
3. **Portfolio Advisor**: Synthesizes analysis and provides recommendations

These agents work together in the `PortfolioTask` workflow to provide comprehensive investment advice.

## Testing

```bash
pytest tests/
```

## Development

- Use `black` for code formatting
- Use `flake8` for linting
- Use `mypy` for type checking

```bash
black .
flake8 .
mypy .
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Support

For support, email support@example.com or open an issue on GitHub.
