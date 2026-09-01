"""Logging utilities."""

import logging
import sys
from pathlib import Path


def setup_logging(
    name: str = "crypto_quant",
    level: str = "INFO",
    log_dir: Path = Path("./logs"),
) -> logging.Logger:
    """
    Setup logging configuration.
    
    Args:
        name: Logger name
        level: Logging level
        log_dir: Directory for log files
        
    Returns:
        Configured logger
    """
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level))
    
    # Create logs directory if it doesn't exist
    log_dir.mkdir(parents=True, exist_ok=True)
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(getattr(logging, level))
    
    # File handler
    file_handler = logging.FileHandler(log_dir / f"{name}.log")
    file_handler.setLevel(getattr(logging, level))
    
    # Formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger
