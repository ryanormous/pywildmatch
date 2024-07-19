
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# IMPORT

import sys

from pywildmatch.logger import get_logger, ParamFormatter
from pywildmatch.param import Parameter


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# GLOBAL

logger = get_logger()
formatter = ParamFormatter(logger)
TTY = formatter.isatty


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# LOG Parameter OBJECT

def log(param:Parameter) -> None:
    logger.debug(formatter.format(param))


def errexit(param:Parameter) -> None:
    log(param) if TTY else print(param, file=sys.stderr)
    raise

