import logging
import os
from datetime import datetime

# Generate a unique log file name using the current date and time, like "07_02_2025_21_45_30.log"
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the path where the logs will be saved: current working directory + "logs" folder
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Example: if your project is in "C:\Users\kiran\project", log_path will be "C:\Users\kiran\project\logs"

# Create the logs directory if it doesn't already exist
os.makedirs(log_path, exist_ok=True)

# Combine log folder and log filename to get the full log file path
LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)
# Example: LOG_FILE_PATH = "C:\Users\kiran\project\logs\07_02_2025_21_45_30.log"


# Configure logging to:
# - write logs to the file defined by LOG_FILE_PATH
# - format logs to include timestamp, line number, logger name, level, and message
# - set logging level to INFO (you can change to DEBUG, ERROR, etc. as needed)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


# Example
# def divide(a, b):
#     logging.info(f"Starting division: {a} / {b}")   # Logs function entry
#     try:
#         result = a / b
#         logging.info(f"Division successful: result = {result}")
#         return result
#     except ZeroDivisionError as e:
#         logging.error("Division by zero attempted!", exc_info=True)
#         return None

# divide(10, 2)   # Normal case
# divide(5, 0)    # Error case

# [2025-07-02 21:58:04,122] 13 root - INFO - Starting division: 10 / 2
# [2025-07-02 21:58:04,123] 15 root - INFO - Division successful: result = 5.0
# [2025-07-02 21:58:04,124] 13 root - INFO - Starting division: 5 / 0
# [2025-07-02 21:58:04,125] 17 root - ERROR - Division by zero attempted!
# Traceback (most recent call last):
#   File "example.py", line 14, in divide
#     result = a / b
# ZeroDivisionError: division by zero

