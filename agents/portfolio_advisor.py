"""Portfolio Advisor Agent - Provides portfolio recommendations."""

from typing import Dict, List, Any
from datetime import datetime


class PortfolioAdvisor:
    """Agent responsible for providing portfolio recommendations and adjustments."""
    
    def __init__(self):
        """Initialize the Portfolio Advisor agent."""
        self.name = "Portfolio Advisor"
        self.recommendations = []
    
    def advise_portfolio(self, portfolio: Dict[str, Any], analysis: Dict[str, Any], 
                        risk_assessment: Dict[str, Any]) -> Dict[str, Any]:
        """
        Provide portfolio advice based on market analysis and risk assessment.
        
        Args:
            portfolio: Current portfolio composition
            analysis: Market analysis from market analyst
            risk_assessment: Risk assessment from risk assessor
            
        Returns:
            Portfolio recommendations and suggested adjustments
        """
        advice = {
            "timestamp": datetime.now().isoformat(),
            "agent": self.name,
            "current_portfolio": portfolio,
            "suggested_adjustments": self._generate_adjustments(portfolio, analysis),
            "rebalancing_actions": self._calculate_rebalancing(portfolio, risk_assessment),
            "allocation_targets": self._get_target_allocation()
        }
        self.recommendations.append(advice)
        return advice
    
    def _generate_adjustments(self, portfolio: Dict[str, Any], analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate suggested portfolio adjustments."""
        return [
            {"action": "INCREASE", "symbol": "AAPL", "percentage": 5},
            {"action": "DECREASE", "symbol": "XYZ", "percentage": 3}
        ]
    
    def _calculate_rebalancing(self, portfolio: Dict[str, Any], risk_assessment: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Calculate rebalancing actions based on risk assessment."""
        return [
            {"from": "TECH", "to": "FINANCE", "amount": 10000}
        ]
    
    def _get_target_allocation(self) -> Dict[str, float]:
        """Get target asset allocation."""
        return {
            "EQUITY": 0.60,
            "FIXED_INCOME": 0.25,
            "CASH": 0.10,
            "ALTERNATIVES": 0.05
        }
    
    def get_recommendations(self) -> List[Dict[str, Any]]:
        """Return all portfolio recommendations."""
        return self.recommendations
