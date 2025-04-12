#!/bin/userenv python3

from argparse import ArgumentParser
import qrcode
from pathlib import Path
import os

def main(data, outfile):
    os.makedirs(name=Path(outfile).parent, exist_ok=True)
    img = qrcode.make(data)
    img.save(f'{outfile}.png')

if __name__ == "__main__":
    argparser = ArgumentParser() 
    argparser.add_argument("--data", "-d", action="store", required=True)
    argparser.add_argument("--output-png", "-o", action="store", default="qrcode")
    args = argparser.parse_args()
    main(args.data, args.output_png)
