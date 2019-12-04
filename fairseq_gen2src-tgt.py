import argparse
from pathlib import Path

from utils import process_bpe_symbol


def extract(line, remove_bpe):
    sp = line.split('\t')
    id_ = int(sp[0][2:])
    snt = sp[-1]
    snt = process_bpe_symbol(snt, remove_bpe)
    return id_, snt

def main(args):
    out_dir = Path(args.output_dir)
    out_dir.mkdir(exist_ok=True)
    out_src = out_dir/'gen.src'
    out_tgt = out_dir/'gen.tgt'
    generate = {}
    refernce = {}
    with open(args.filename) as f:
        for line in f:
            if line.startswith('S'):
                id_, snt = extract(line.strip(), args.remove_bpe)
                refernce[id_] = snt
            elif line.startswith('H'):
                id_, snt = extract(line.strip(), args.remove_bpe)
                generate[id_] = snt
    with open(out_src, 'w') as wfr, open(out_tgt, 'w') as wfg:
        ref_items = sorted(refernce.items())
        wfr.write('\n'.join([item[1] for item in ref_items]))
        gen_items = sorted(generate.items())
        wfg.write('\n'.join([item[1] for item in gen_items]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    parser.add_argument('--remove-bpe', default=None)
    parser.add_argument('--output-dir', default=None)
    args = parser.parse_args()
    main(args)
