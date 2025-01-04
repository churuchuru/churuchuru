# cleanup.py
import os
import time
import logging
from apscheduler.schedulers.background import BackgroundScheduler

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def cleanup_old_files(upload_dir, retention_period_seconds):
    """
    Delete files older than the retention period based on their modification time.
    """
    current_time = time.time()
    for filename in os.listdir(upload_dir):
        file_path = os.path.join(upload_dir, filename)
        
        # Skip directories (if any)
        if os.path.isdir(file_path):
            continue
        
        # Get the file's modification time
        modification_time = os.path.getmtime(file_path)
        
        # Delete the file if it's older than the retention period
        if current_time - modification_time > retention_period_seconds:
            os.remove(file_path)
            logger.info(f"Deleted old file: {filename}")

def start_cleanup_scheduler(upload_dir, retention_period_seconds):
    """
    Start a background scheduler to periodically clean up old files.
    """
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        cleanup_old_files,
        'interval',
        # hours=1,  # Run every hour
        minutes=15,  # Run every x minutes
        args=[upload_dir, retention_period_seconds],
    )
    scheduler.start()
    logger.info("Cleanup scheduler started.")