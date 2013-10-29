'''
Created on Oct 27, 2013

@author: sina
'''

import importlib
import argparse
import sys

from utils.utils import setup_logger
logger = setup_logger()


def _valid_level(level):
    min_level = 0
    max_level = 10
    if level < min_level or level > max_level:
        logger.error('Invalid level. Select a level between %s and %s' % (min_level, max_level))
        sys.exit(1)


def _solve(level):
    try:
        Level = importlib.import_module('level.level_%s' % level)
    except ImportError:
        logger.error('Level %s is not solved yet! or the package import failed :(' % level)
        logger.debug(sys.exc_info())
        sys.exit(1)
    l = getattr(Level, 'Level%s' % level)()
    l.solve()


def main(argv):
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-l', '--level', dest='level', type=int, help='Provide number of the level to solve', default=0)
    args = arg_parser.parse_args(argv)
    level = args.level
    _valid_level(level)
    _solve(level)
    

if __name__ == '__main__':
    main(sys.argv[1:])
