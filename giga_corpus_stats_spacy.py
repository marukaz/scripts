import argparse
import re
import gzip
from pathlib import Path

import spacy
from tqdm import tqdm


spc = spacy.load("en_core_web_sm")

parser = argparse.ArgumentParser()
parser.add_argument('src')
args = parser.parse_args()

src = Path(args.src)

instance_num = 0
t_word_num = 0
a_word_num = 0
fa_word_num = 0
fa_sent_num = 0

with src.open() as f:
    for l in tqdm(f):
        instance_num += 1
        splits = l.strip().split("\t")
        _, _, title, article, full_article = splits
        t_word_num += len(spc(title))
        a_word_num += len(spc(article))
        fa_word_num += len(spc(full_article))
        fa_sent_num += len(list(spc(full_article).sents))

print('instance num:', instance_num)
print('avg. title word num:', t_word_num/instance_num)
print('avg. article word num:', a_word_num/instance_num)
print('avg. full article word num:', fa_word_num/instance_num)
print('avg. full article sent num:', fa_sent_num/instance_num)