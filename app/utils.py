import logging
# ==========================
# Logging Configuration
# ==========================
log_file="leave_logger.txt"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    filename=log_file,
    filemode="a"
)
logger = logging.getLogger(__name__)

BASE_URL = "http://127.0.0.1:8000"