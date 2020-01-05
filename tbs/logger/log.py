import os

LOG_ERROR = "[ERROR]" # type of logging
LOG_DEBUG = "[DEBUG]" # type of logging
LOG_WARM = "[WARN]" # type of logging

WARNING_COLOR = "\033[93m" # color for displaying warning messages
ERROR_COLOR = "\033[91m" # color for error messages
ENDC = "\033[0m" # end color sequence

LOG_LEVEL= int(os.getenv('TBS_LOG', "1"))

def printInColor(type, text):
    """
    Display the right color based on the log type
    @Type is the log type as per defined in the above variables beginning with LOG_
    @text is the text to display
    """
    if (type == LOG_ERROR):
        print(ERROR_COLOR + type + " " + text + ENDC)
    elif (type == LOG_WARM):
        print(WARNING_COLOR + type + " " + text + ENDC)
    else:
        print(type + " " + text)



def log(str, log_type=LOG_DEBUG):
    """
    Print a log based on its log_type
    """
    if(LOG_LEVEL == 3 and (log_type == LOG_WARM or log_type == LOG_DEBUG or log_type == LOG_ERROR)):
        printInColor(log_type, str)
    elif(LOG_LEVEL == 2 and log_type != LOG_DEBUG):
        printInColor(log_type, str )
    elif(log_type == LOG_ERROR):
        printInColor(log_type, str)