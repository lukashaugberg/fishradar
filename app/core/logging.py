import logging
from config import config

def setup_logging():
    logging.basicConfig(
        level=logging.DEBUG if config.debug else logging.INFO,
        format="%(asctime)s %(levelname)s [%(name)s] %(message)s"
    )
