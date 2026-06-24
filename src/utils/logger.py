"""
Logger Utility

Stock-CIO
"""

import logging


class Logger:
    """Application Logger"""

    @staticmethod
    def get_logger(name: str = "Stock-CIO") -> logging.Logger:
        logger = logging.getLogger(name)

        if logger.handlers:
            return logger

        logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "[%(levelname)s] %(message)s"
        )

        console = logging.StreamHandler()
        console.setFormatter(formatter)

        logger.addHandler(console)

        return logger