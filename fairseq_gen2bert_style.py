import argparse


def main(args):
    out_filename = '.'.join(args.filename.split('.')[:-1].append('tsv'))
    with open(args.filename) as rf, open(out_filename, 'w') as wf:
        for line in rf:
            if line.startswith('S'):
                splits = line.rstrip().split('\t')
                wf.write(f'{splits[0][2:]}\t{splits[-1]}\t')
            elif line.startswith('H'):
                wf.write(line.split('\t')[-1])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    main(args)
