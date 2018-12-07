import argparse
import json
import numpy as np


def main(args):
    with open(args.filename) as f:
        for line in f:
            try:
                d = json.loads(line)
            except json.JSONDecodeError:
                continue
            longest = np.argmax([len(hypo['text']) for hypo in d['hypos']])
            if longest != 0:
                print(line, end='')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    main(args)
