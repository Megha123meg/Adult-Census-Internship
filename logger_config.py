import os
import logging

# Define the log folder and filename
log_folder = "logs/"
log_filename = "app.log"

# Ensure the log folder exists, create it if it doesn't
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

# Define the full log file path
log_filepath = os.path.join(log_folder, log_filename)

# Configure logging
logging.basicConfig(filename=log_filepath, level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)