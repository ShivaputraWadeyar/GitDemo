import logging

logger =logging.getLogger(__name__)

filehandler=logging.FileHandler("logfile.log")
formatter=logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(msg)s")
filehandler.setFormatter(formatter)
logger.addHandler(filehandler)

logger.setLevel(logging.ERROR)
logger.debug("debug info")
logger.info("info statement")
logger.error("error info")
logger.warning("warning msg")
logger.debug("debug info2")
logger.critical("critical issue")
logger.debug("debug info3")
