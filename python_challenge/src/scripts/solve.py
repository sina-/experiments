'''
Created on Oct 27, 2013

@author: sina
'''

import importlib
import argparse
import sys

from utils.utils import setup_logger

def _valid_level(level, logger):
    min_level = 0
    max_level = 10
    if level < min_level or level > max_level:
        logger.error('Invalid level. Select a level between %s and %s' % (min_level, max_level))
        sys.exit(1)


def _solve(level, logger):
    try:
        Level = importlib.import_module('level.level_%s' % level)
    except ImportError as e:
        logger.error('Level %s is not solved yet!' % level)
        logger.debug('Exception body: %s' % e)
        sys.exit(1)
    l = getattr(Level, 'Level%s' % level)()
    l.solve()


def main(argv):
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-l', '--level', dest='level', type=int, help='Provide number of the level to solve', default=0)
    arg_parser.add_argument('-v', '--verbose', dest='verbose', action="store_true", help='Set verbosity level to DEBUG', default=False)
    args = arg_parser.parse_args(argv)

    logger = setup_logger(verbose=args.verbose)
    level = args.level
    _valid_level(level, logger)
    _solve(level, logger)


if __name__ == '__main__':
    main(sys.argv[1:])
