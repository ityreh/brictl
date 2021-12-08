#!/usr/bin/env python3

import argparse
import pathlib
import shutil

parser = argparse.ArgumentParser(
    prog='imgaug', usage='%(prog)s [options]', description='Data augmentation for images.')
parser.add_argument('input', type=pathlib.Path,
                    help='input path to get original images')
parser.add_argument('output', type=pathlib.Path,
                    help='output path to store generated images')
args = parser.parse_args()

input = args.input
output = args.output

shutil.copyfile(input, output)
