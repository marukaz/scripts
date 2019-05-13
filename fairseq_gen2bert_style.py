import argparse


def main(args):
    out_filename = '.'.join(args.filename.split('.')[:-1] + ['tsv'])
    with open(args.filename) as rf, open(out_filename, 'w') as wf:
        for line in rf:
            if line.startswith('S'):
                splits = line.rstrip().split('\t')
                snt = ''.join(splits[-1].split(' '))
                if snt.startswith('▁'):
                    snt = snt[1:]
                wf.write(f'{splits[0][2:]}\t{snt}\t')
            elif line.startswith('H'):
                splits = line.split('\t')
                snt = ''.join(splits[-1].split(' '))
                if snt.startswith('▁'):
                    snt = snt[1:]
                wf.write(snt)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    main(args)
