import argparse
import os


class ArgsParser:
    @staticmethod
    def parse_args(args):
        parser = argparse.ArgumentParser(description='Write directory')
        parser.add_argument('--d', dest='directory',
                            help='Enter directory', required=False, default=os.getcwd())
        return parser.parse_args(args)
