import argparse


def main(args):
    with open(args.filename) as rf, open('reference.txt', 'w') as wfr, open('generation.txt', 'w') as wfg:
        for line in rf:
            if line.startswith('T'):
                snt = ''.join(line.split('\t')[-1].split(' '))
                if snt.startswith('▁'):
                    snt = snt[1:]
                wfr.write(snt)
            elif line.startswith('H'):
                snt = ''.join(line.split('\t')[-1].split(' '))
                if snt.startswith('▁'):
                    snt = snt[1:]
                wfg.write(snt)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    main(args)
