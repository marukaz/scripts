import argparse
from pathlib import Path

from tqdm import tqdm
from pytorch_transformers import BertTokenizer


def main(args):
    path = Parh(args.path)
    save_dir = Path(str(ref_path) +'_wp')
    save_dir.mkdir(exist_ok=True)
    save_path = save_dir/path.name

    wp = BertTokenizer.from_pretrained(args.tokenizer_data, do_lower_case=False)
    with path.open() as rf, save_path.open('w') as wf:
        for line in tqdm(rf):
            tokenized = wp._tokenize(line)
            print(' '.join(tokenized), file=wf)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    parser.add_argument('-d', '--tokenizer-data')
    args = parser.parse_args()
    main(args)