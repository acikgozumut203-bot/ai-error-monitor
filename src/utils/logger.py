import datetime

class Logger:
    def __init__(self):
        self.log_file = "application.log"

    def log(self, message):
        timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.log_file, 'a') as f:
            f.write(f"[{timestamp}] {message}\n")

    def log_error(self, error_message):
        self.log(f"ERROR: {error_message}")

# Usage Example:
if __name__ == '__main__':
    logger = Logger()
    logger.log('This is a log message.')
    logger.log_error('This is an error message.')