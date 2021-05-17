import argparse

class Parser:
    def __init__(self, sys_args):
        parser = argparse.ArgumentParser()
        parser.add_argument('--outfile', type=str, help="output path", required=True)
        parser.add_argument('--params', type=str, default="params.json")
        self.args = parser.parse_args(sys_args)