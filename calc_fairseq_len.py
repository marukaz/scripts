import argparse
import json
import numpy as np


def main(args):
    count = 0
    ref_shortest = 0
    with open(args.filename) as f:
        for line in f:
            try:
                d = json.loads(line)
            except json.JSONDecodeError:
                continue
            shortest = np.argmin([len(hypo['text']) for hypo in d['hypos']])
            if shortest == 0:
                ref_shortest += 1
            count += 1
    print(ref_shortest/count)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    main(args)