"""Configuration Management - Centralized config for the application."""

import os
from typing import Dict, Any


class Config:
    """Configuration class for application settings."""
    
    # API Configuration
    API_KEY = os.getenv("API_KEY", "your_api_key_here")
    API_BASE_URL = os.getenv("API_BASE_URL", "https://api.example.com")
    
    # Data Configuration
    DATA_SOURCE = os.getenv("DATA_SOURCE", "yfinance")
    CACHE_ENABLED = os.getenv("CACHE_ENABLED", "True").lower() == "true"
    CACHE_TTL = int(os.getenv("CACHE_TTL", "3600"))  # seconds
    
    # Analysis Configuration
    ANALYSIS_WINDOW = int(os.getenv("ANALYSIS_WINDOW", "30"))  # days
    MIN_CONFIDENCE_SCORE = float(os.getenv("MIN_CONFIDENCE_SCORE", "0.7"))
    
    # Risk Management
    MAX_PORTFOLIO_CONCENTRATION = float(os.getenv("MAX_PORTFOLIO_CONCENTRATION", "0.30"))
    MAX_SECTOR_ALLOCATION = float(os.getenv("MAX_SECTOR_ALLOCATION", "0.40"))
    
    # Logging Configuration
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE = os.getenv("LOG_FILE", "logs/app.log")
    
    # Database Configuration
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///data.db")
    
    @classmethod
    def get_all_config(cls) -> Dict[str, Any]:
        """Get all configuration settings."""
        return {
            "api_key": cls.API_KEY,
            "api_base_url": cls.API_BASE_URL,
            "data_source": cls.DATA_SOURCE,
            "cache_enabled": cls.CACHE_ENABLED,
            "cache_ttl": cls.CACHE_TTL,
            "analysis_window": cls.ANALYSIS_WINDOW,
            "min_confidence_score": cls.MIN_CONFIDENCE_SCORE,
            "max_portfolio_concentration": cls.MAX_PORTFOLIO_CONCENTRATION,
            "max_sector_allocation": cls.MAX_SECTOR_ALLOCATION,
            "log_level": cls.LOG_LEVEL,
            "log_file": cls.LOG_FILE,
            "database_url": cls.DATABASE_URL
        }
    
    @classmethod
    def validate_config(cls) -> bool:
        """Validate configuration settings."""
        required_fields = ["API_KEY", "API_BASE_URL"]
        
        for field in required_fields:
            if not getattr(cls, field):
                print(f"Warning: {field} is not configured")
        
        return True
