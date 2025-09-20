import inspect
import logging



def customLogger():
    logname = inspect.stack()[1][3]
    logger = logging.getLogger(logname)
    logger.setLevel(logging.DEBUG)
    fileHandler = logging.FileHandler("../Reports/automation.log",mode='a')
    fileHandler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s',datefmt='%d/%m/%y %I:%M:%S %p %A')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    return logger
