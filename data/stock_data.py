"""Stock Data Manager - Handles data fetching and management."""

from typing import Dict, List, Any
from datetime import datetime, timedelta
import random


class StockDataManager:
    """Manager for stock data operations."""
    
    def __init__(self):
        """Initialize stock data manager."""
        self.data_cache = {}
    
    def fetch_market_data(self) -> Dict[str, Any]:
        """
        Fetch current market data.
        
        Returns:
            Market data dictionary
        """
        return {
            "timestamp": datetime.now().isoformat(),
            "market_index": 4850.43,
            "market_change": 0.35,
            "stocks": self._generate_stock_data(),
            "market_cap": 2.4e13,
            "trading_volume": 3.2e9
        }
    
    def _generate_stock_data(self) -> List[Dict[str, Any]]:
        """Generate sample stock data."""
        symbols = ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "TSLA", "META"]
        stocks = []
        
        for symbol in symbols:
            stocks.append({
                "symbol": symbol,
                "price": round(random.uniform(50, 500), 2),
                "change": round(random.uniform(-5, 5), 2),
                "volume": random.randint(1000000, 100000000),
                "pe_ratio": round(random.uniform(10, 50), 2),
                "market_cap": round(random.uniform(1e11, 3e12), 2)
            })
        
        return stocks
    
    def fetch_historical_data(self, symbol: str, days: int = 30) -> List[Dict[str, Any]]:
        """
        Fetch historical data for a stock.
        
        Args:
            symbol: Stock symbol
            days: Number of days of history
            
        Returns:
            List of historical data points
        """
        history = []
        base_price = random.uniform(100, 300)
        
        for i in range(days):
            date = datetime.now() - timedelta(days=i)
            price = base_price + random.uniform(-10, 10)
            history.append({
                "date": date.isoformat(),
                "symbol": symbol,
                "price": round(price, 2),
                "volume": random.randint(1000000, 100000000)
            })
        
        return history
    
    def cache_data(self, key: str, data: Any) -> None:
        """Cache data for quick access."""
        self.data_cache[key] = data
    
    def get_cached_data(self, key: str) -> Any:
        """Retrieve cached data."""
        return self.data_cache.get(key)
