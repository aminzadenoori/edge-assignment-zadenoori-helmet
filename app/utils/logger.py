"""This module contains logger configuration.
Author: Stefano Ravagnan <stefano@energiacollettiva.com>
"""
import logging
import logging.config

logging.config.fileConfig("./app/config/logging.ini", disable_existing_loggers=False)
logger = logging.getLogger("root")