"""Risk Analysis Task - Handles risk assessment workflow."""

from typing import Dict, Any
from agents.risk_assessor import RiskAssessor
from data.stock_data import StockDataManager


class RiskAnalysisTask:
    """Task for executing risk analysis workflow."""
    
    def __init__(self):
        """Initialize risk analysis task."""
        self.assessor = RiskAssessor()
        self.data_manager = StockDataManager()
    
    def execute(self, portfolio: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the risk analysis task.
        
        Args:
            portfolio: Current portfolio composition
            
        Returns:
            Risk assessment results
        """
        print(f"[TASK] Starting risk analysis...")
        
        # Fetch market data
        market_data = self.data_manager.fetch_market_data()
        
        # Run risk assessment
        assessment = self.assessor.assess_risk(portfolio, market_data)
        
        print(f"[TASK] Risk analysis completed.")
        return assessment
    
    def get_results(self) -> Dict[str, Any]:
        """Get assessment results."""
        return {
            "task": "Risk Analysis",
            "assessments": self.assessor.get_assessments()
        }
