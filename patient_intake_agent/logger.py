import logging


# TODO: prevent duplicate logs, possibly due to multiple handlers being attached
def _configure_logger():
    logging.basicConfig()
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # formatter = logging.Formatter(
    #     "%(levelname)s:%(filename)s:%(funcName)s:%(lineno)d:%(message)s"
    # )
    # if not logger.handlers:
    #     # add handler only if there are no handlers already attached
    #     handler = logging.StreamHandler()
    #     handler.setFormatter(formatter)
    #     logger.addHandler(handler)
    return logger


logger = _configure_logger()
