import argparse


def main(args):
    with open(args.file) as f:
        sum_len = 0
        for i, line in enumerate(f, 1):
            sum_len += len(line)
        print(f'Avg. of sentence length: {sum_len / i}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, help='path to corpus file, assume one sentence per line')
    args = parser.parse_args()
    main(args)
