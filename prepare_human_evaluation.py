import argparse
import random
from pathlib import Path


def main(args):
    random.seed(args.seed)
    save_dir = Path(args.output_dir)
    save_dir.mkdir(exist_ok=True)
    save_flag_path = save_dir/'shuffle_flag.txt'
    save_tsv_path = save_dir/'eval.tsv'
    eval_list = []
    with open(args.src) as sf, open(args.ours) as of, open(args.base) as bf:
        for src, ours, base in zip(sf, of, bf):
            src = src.strip()
            if len(src) < 10:
                continue
            ours = ours.strip()
            base = base.strip()
            eval_list.append((src, ours, base))
    random.shuffle(eval_list)
    with save_flag_path.open('w') as ff, save_tsv_path.open('w') as tf:
        for src, ours, base in eval_list:
            if random.random() >= 0.5:
                print('True', file=ff)
                print('\t'.join((src, base, ours)), file=tf)
            else:
                print('False', file=ff)
                print('\t'.join((src, ours, base)), file=tf)
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--src')
    parser.add_argument('--ours')
    parser.add_argument('--base')
    parser.add_argument('--output-dir')
    parser.add_argument('--seed', type=int, default=516)
    args = parser.parse_args()
    main(args)