import argparse
from pathlib import Path

from tqdm import tqdm
from pytorch_transformers import BertTokenizer
import sentencepiece as spm


def main(args):
    path = Path(args.path)
    if args.algorithm == 'wordpiece':
        save_dir = Path(str(path.parent) +'_wp')
    elif args.algorithm == 'sentencepiece':
        save_dir = Path(str(path.parent) +'_sp')
    else:
        raise ValueError('algorithm is wrong')
    save_dir.mkdir(exist_ok=True)
    save_path = save_dir/path.name
    if args.algorithm == 'wordpiece':
        wp = BertTokenizer.from_pretrained(args.tokenizer_data, do_lower_case=False)
        with path.open() as rf, save_path.open('w') as wf:
            for line in tqdm(rf):
                if args.replace_sharp:
                    line = line.replace('#', '1')
                tokenized = wp._tokenize(line)
                print(' '.join(tokenized), file=wf)
    elif args.algorithm == 'sentencepiece':
        sp = spm.SentencePieceProcessor()
        sp.load(args.tokenizer_data)
        with path.open() as rf, save_path.open('w') as wf:
            for line in tqdm(rf):
                tokenized = sp.EncodeAsPieces(line.rstrip())
                print(' '.join(tokenized), file=wf)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    parser.add_argument('-d', '--tokenizer-data')
    parser.add_argument('-a', '--algorithm', default='wordpiece', choices=['wordpiece', 'sentencepiece'])
    parser.add_argument('-r', '--replace-sharp', action='store_true')
    args = parser.parse_args()
    main(args)
