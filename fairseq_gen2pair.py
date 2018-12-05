import argparse


def main(args):
    with open(args.filename) as rf, open('reference.txt', 'w') as wfr, open('generation.txt', 'w') as wfg:
        for line in rf:
            if line.startswith('T'):
                wfr.write(line.split('\t')[-1])
            elif line.startswith('H'):
                wfg.write(line.split('\t')[-1])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    main(args)
