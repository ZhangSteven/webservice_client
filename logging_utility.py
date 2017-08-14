# coding=utf-8
# 
# from config_logging package, provides a config object (from config file)
# and a logger object (logging to a file).
# 
import logging
import logging.config



def _get_logger():
	"""
	Read the logging configuration file, return a logger. With the logger,
	you can:

	1. show log messages to the console and print to the log file at the same
		time.
	2. config log levels to the console and log file differently.

	log file and code skeleton comes from:
	https://stackoverflow.com/a/17100643/3331297
	"""
	logging.config.fileConfig('logging.config')
	return logging.getLogger('applog')



# initialized only once when this module is first imported by others
if not 'logger' in globals():
	logger = _get_logger()
