import sys

import traceback

# Alternative approach using traceback module (more robust)
class CustomException(Exception):
    """Custom exception class using traceback module."""
    
    def __init__(self, error_message: str) -> None:
        self.error_message = error_message
        
        # Get traceback information
        tb = traceback.extract_tb(sys.exc_info()[2])
        if tb:
            # Get the last frame (where the error occurred)
            last_frame = tb[-1]
            self.file_name = last_frame.filename
            self.lineno = last_frame.lineno
        else:
            self.file_name = "unknown"
            self.lineno = 0
    
    def __str__(self) -> str:
        return "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
            self.file_name, self.lineno, str(self.error_message)
        )


if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        raise CustomException(str(e))