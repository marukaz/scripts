import argparse
from pathlib import Path

from tqdm import tqdm
from pytorch_transformers import BertTokenizer


def main(args):
    path = Path(args.path)
    save_dir = Path(str(path.parent) +'_wp')
    save_dir.mkdir(exist_ok=True)
    save_path = save_dir/path.name

    wp = BertTokenizer.from_pretrained(args.tokenizer_data, do_lower_case=False)
    with path.open() as rf, save_path.open('w') as wf:
        for line in tqdm(rf):
            if args.replace_sharp:
                line = line.replace('#', '1')
            tokenized = wp._tokenize(line)
            print(' '.join(tokenized), file=wf)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    parser.add_argument('-d', '--tokenizer-data')
    parser.add_argument('-r', '--replace-sharp', action='store_true')
    args = parser.parse_args()
    main(args)
