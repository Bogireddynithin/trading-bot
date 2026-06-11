import logging

def setup_logger():
    logger = logging.getLogger("trading_bot")
    logger.setLevel(logging.INFO)

    # File handler
    file_handler = logging.FileHandler("trading_bot.log")
    file_handler.setLevel(logging.INFO)

    # Format
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)

    # Add handler
    if not logger.handlers:
        logger.addHandler(file_handler)

    return logger