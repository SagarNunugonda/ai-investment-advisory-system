"""Main Entry Point - AI Investment Advisory System."""

import sys
from typing import Dict, Any
from tasks.portfolio_task import PortfolioTask
from utils.config import Config


def main():
    """Main application entry point."""
    print("=" * 60)
    print("AI Investment Advisory System")
    print("=" * 60)
    
    # Validate configuration
    Config.validate_config()
    
    # Sample portfolio
    sample_portfolio = {
        "AAPL": {"shares": 100, "value": 25000},
        "MSFT": {"shares": 50, "value": 20000},
        "GOOGL": {"shares": 30, "value": 28000},
        "AMZN": {"shares": 25, "value": 27000},
        "CASH": {"amount": 10000}
    }
    
    print("\nCurrent Portfolio:")
    print_portfolio(sample_portfolio)
    
    # Execute portfolio advisory workflow
    print("\n" + "-" * 60)
    print("Starting Portfolio Advisory Workflow...")
    print("-" * 60 + "\n")
    
    try:
        portfolio_task = PortfolioTask()
        results = portfolio_task.execute(sample_portfolio)
        
        print("\n" + "-" * 60)
        print("Portfolio Advisory Results")
        print("-" * 60)
        print_results(results)
        
        print("\n" + "=" * 60)
        print("Workflow Completed Successfully")
        print("=" * 60)
        
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)


def print_portfolio(portfolio: Dict[str, Any]) -> None:
    """Print portfolio details."""
    total_value = 0
    
    for symbol, details in portfolio.items():
        if symbol == "CASH":
            print(f"  {symbol}: ${details['amount']:,.2f}")
            total_value += details['amount']
        else:
            print(f"  {symbol}: {details['shares']} shares @ ${details['value']:,.2f}")
            total_value += details['value']
    
    print(f"\nTotal Portfolio Value: ${total_value:,.2f}")


def print_results(results: Dict[str, Any]) -> None:
    """Print advisory results."""
    if "suggested_adjustments" in results:
        print("\nSuggested Adjustments:")
        for adjustment in results["suggested_adjustments"]:
            print(f"  - {adjustment['action']} {adjustment['symbol']} by {adjustment['percentage']}%")
    
    if "rebalancing_actions" in results:
        print("\nRebalancing Actions:")
        for action in results["rebalancing_actions"]:
            print(f"  - Move ${action['amount']:,.2f} from {action['from']} to {action['to']}")
    
    if "allocation_targets" in results:
        print("\nTarget Asset Allocation:")
        for asset_class, allocation in results["allocation_targets"].items():
            print(f"  - {asset_class}: {allocation*100:.1f}%")


if __name__ == "__main__":
    main()
