import argparse


def extract(line):
    sp = line.split('\t')
    id_ = int(sp[0][2:])
    snt = sp[-1]
    return id_, snt

def main(args):
    generate = {}
    refernce = {}
    with open(args.filename) as f:
        for line in f:
            if line.startswith('T'):
                id_, snt = extract(line.strip())
                refernce[id_] = snt
            elif line.startswith('H'):
                id_, snt = extract(line.strip())
                generate[id_] = snt
    with open('reference.txt', 'w') as wfr, open('generation.txt', 'w') as wfg:
        ref_items = sorted(refernce.items())
        wfr.write('\n'.join([item[1] for item in ref_items]))
        gen_items = sorted(generate.items())
        wfg.write('\n'.join([item[1] for item in gen_items]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    main(args)
