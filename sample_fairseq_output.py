import argparse
import random
from pathlib import Path

from utils import process_bpe_symbol


def extract(line, remove_bpe):
    sp = line.split('\t')
    id_ = int(sp[0][2:])
    snt = sp[-1]
    snt = process_bpe_symbol(snt, remove_bpe)
    return id_, snt

def main(args):
    random.seed(args.seed)
    path = Path(args.filepath)
    save_hypo_path = path.parent/f'{path.name}.hypo.sample{args.sample_num}'
    save_src_path = path.parent/f'{path.name}.src.sample{args.sample_num}'
    save_ids_path = path.parent/f'{path.name}.ids.sample{args.sample_num}'
    if args.id_file is not None:
        with open(args.od_file) as f:
            sample_ids = [int(id_) for id_ in f]
    else:
        sample_ids = random.sample(range(args.example_num), k=args.sample_num)
    with save_ids_path.open('w') as f:
        for id_ in sample_ids:
            print(id_, file=f)

    with open(args.filepath) as f, save_hypo_path.open('w') as hf, save_src_path.open('w') as sf:
        for line in f:
            if line.startswith('S'):
                id_, snt = extract(line.strip(), args.remove_bpe)
                if id_ in sample_ids:
                    print(snt, file=sf)
            elif line.startswith('H'):
                id_, snt = extract(line.strip(), args.remove_bpe)
                if id_ in sample_ids:
                    print(snt, file=hf)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath')
    parser.add_argument('--seed', type=int, default=516)
    parser.add_argument('--example-num', type=int, default=10000)
    parser.add_argument('--sample-num', type=int, default=100)
    parser.add_argument('--id-file', default=None)
    parser.add_argument('--remove-bpe', default=None)
    args = parser.parse_args()
    main(args)