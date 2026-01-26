"""Market Analysis Task - Handles market analysis workflow."""

from typing import Dict, Any
from agents.market_analyst import MarketAnalyst
from data.stock_data import StockDataManager


class MarketAnalysisTask:
    """Task for executing market analysis workflow."""
    
    def __init__(self):
        """Initialize market analysis task."""
        self.analyst = MarketAnalyst()
        self.data_manager = StockDataManager()
    
    def execute(self) -> Dict[str, Any]:
        """
        Execute the market analysis task.
        
        Returns:
            Market analysis results
        """
        print(f"[TASK] Starting market analysis...")
        
        # Fetch market data
        market_data = self.data_manager.fetch_market_data()
        
        # Run analysis
        analysis = self.analyst.analyze_market_data(market_data)
        
        print(f"[TASK] Market analysis completed.")
        return analysis
    
    def get_results(self) -> Dict[str, Any]:
        """Get analysis results."""
        return {
            "task": "Market Analysis",
            "history": self.analyst.get_analysis_history()
        }
