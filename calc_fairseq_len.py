import argparse
import json
import numpy as np


def main(args):
    count = 0
    ref_longest = 0
    with open(args.filename) as f:
        for line in f:
            try:
                d = json.loads(line)
            except json.JSONDecodeError:
                continue
            longest = np.argmax([len(hypo['text']) for hypo in d['hypos']])
            if longest == 0:
                ref_longest += 1
            count += 1
    print(f'ratio of reference which is longest: {ref_longest/count}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    main(args)
