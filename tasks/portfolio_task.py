"""Portfolio Task - Handles portfolio advice workflow."""

from typing import Dict, Any
from agents.portfolio_advisor import PortfolioAdvisor
from tasks.market_analysis_task import MarketAnalysisTask
from tasks.risk_analysis_task import RiskAnalysisTask


class PortfolioTask:
    """Task for executing portfolio advice workflow."""
    
    def __init__(self):
        """Initialize portfolio task."""
        self.advisor = PortfolioAdvisor()
        self.market_task = MarketAnalysisTask()
        self.risk_task = RiskAnalysisTask()
    
    def execute(self, portfolio: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the portfolio advice workflow.
        
        Args:
            portfolio: Current portfolio composition
            
        Returns:
            Portfolio recommendations and advice
        """
        print(f"[TASK] Starting portfolio advisory workflow...")
        
        # Execute market analysis
        market_analysis = self.market_task.execute()
        
        # Execute risk analysis
        risk_assessment = self.risk_task.execute(portfolio)
        
        # Generate portfolio advice
        advice = self.advisor.advise_portfolio(portfolio, market_analysis, risk_assessment)
        
        print(f"[TASK] Portfolio advisory workflow completed.")
        return advice
    
    def get_results(self) -> Dict[str, Any]:
        """Get portfolio advice results."""
        return {
            "task": "Portfolio Advisory",
            "recommendations": self.advisor.get_recommendations()
        }
