"""Risk Assessor Agent - Evaluates portfolio and market risks."""

from typing import Dict, List, Any
from datetime import datetime


class RiskAssessor:
    """Agent responsible for assessing market and portfolio risks."""
    
    def __init__(self):
        """Initialize the Risk Assessor agent."""
        self.name = "Risk Assessor"
        self.risk_assessments = []
    
    def assess_risk(self, portfolio: Dict[str, Any], market_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Assess risks in portfolio and market conditions.
        
        Args:
            portfolio: Current portfolio composition
            market_data: Current market data
            
        Returns:
            Risk assessment with scores and recommendations
        """
        assessment = {
            "timestamp": datetime.now().isoformat(),
            "agent": self.name,
            "portfolio_risk": self._calculate_portfolio_risk(portfolio),
            "market_risk": self._calculate_market_risk(market_data),
            "recommendations": self._generate_risk_recommendations(portfolio)
        }
        self.risk_assessments.append(assessment)
        return assessment
    
    def _calculate_portfolio_risk(self, portfolio: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate portfolio risk metrics."""
        return {
            "concentration_risk": 0.45,
            "volatility_risk": 0.52,
            "liquidity_risk": 0.30,
            "overall_risk_score": 0.42
        }
    
    def _calculate_market_risk(self, market_data: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate market-level risk factors."""
        return {
            "volatility_index": 18.5,
            "market_sentiment": "neutral",
            "systemic_risk": 0.35
        }
    
    def _generate_risk_recommendations(self, portfolio: Dict[str, Any]) -> List[str]:
        """Generate risk mitigation recommendations."""
        return ["Diversify sector exposure", "Reduce concentration in top holdings"]
    
    def get_assessments(self) -> List[Dict[str, Any]]:
        """Return all risk assessments."""
        return self.risk_assessments
