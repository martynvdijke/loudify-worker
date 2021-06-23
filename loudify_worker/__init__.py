"""
Initialisation module
"""
import sys
import logging
import argparse
import coloredlogs
from setuptools_scm import get_version

__author__ = "Martyn van Dijke"
__copyright__ = "Martyn van Dijke"
__license__ = "MIT"
__version__ = get_version(version_scheme="post-release", local_scheme="no-local-version")

_logger = logging.getLogger(__name__)


def parse_args(args):
    """
    Args:
        args: cli arguments given to script

    Returns:
        list of supported arguments

    """
    parser = argparse.ArgumentParser(description="Loudify worker")
    # set logging level
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO,
    )
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG,
    )
    return parser.parse_args(args)


def setup_logging(loglevel: str) -> None:
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(
        level=loglevel,
        stream=sys.stdout,
        format=logformat,
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    coloredlogs.install(level=loglevel, logger=_logger)


def main(argv=None) -> None:
    """
    Main function of loudify worker
    Args:
        args: sys arguments

    Returns:
        none
    """
    args = parse_args(argv)
    setup_logging(args.loglevel)
    _logger.info("Started loudify worker")
