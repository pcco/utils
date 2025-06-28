#!/bin/userenv python3

from argparse import ArgumentParser
import qrcode
from pathlib import Path
import os

def process_args():
    argparser = ArgumentParser() 
    argparser.add_argument("--data", "-d", action="store", required=True)
    argparser.add_argument("--output-png", "-o", action="store", default="qrcode")
    return argparser.parse_args()


def main():
    args = process_args()
    os.makedirs(name=Path(args.output_png).parent, exist_ok=True)
    img = qrcode.make(args.data)
    img.save(f'{args.output_png}.png')

if __name__ == "__main__":
    main()
