import logging
import sys

def configure_root_logger(
    filename="app.log",
    level=logging.INFO,
    format_str="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
):
    """Configure the root logger as the logging hub"""
    formatter = logging.Formatter(format_str)
    
    # File handler (shared by all modules)
    file_handler = logging.FileHandler(filename)
    file_handler.setFormatter(formatter)
    
    # Console handler (optional)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    
    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)

