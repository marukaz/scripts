import argparse
import re
import gzip
from pathlib import Path


parser = argparse.ArgumentParser()
parser.add_argument('src')
parser.add_argument('workdir')
args = parser.parse_args()

src = Path(args.src)
workdir = Path(args.workdir)
agiga_output_dir = workdir/src.parent.name
agiga_output_dir.mkdir(exist_ok=True)

# Strip off .gz ending
end = src.parent.name + '/' + (src.name[:-len('.xml.gz')]+'.txt')

out = open(workdir/end, "w")

# Parse and print titles and articles
NONE, HEAD, NEXT, TEXT, CONTINUE = 0, 1, 2, 3, 4
MODE = NONE
full_article_parse = []

instance_num = 0
t_word_num = 0
a_word_num = 0
fa_word_num = 0
fa_sent_num = 0

# FIX: Some parses are mis-parenthesized.
def fix_paren(parse):
    if len(parse) < 2:
        return parse
    if parse[0] == "(" and parse[1] == " ":
        return parse[2:-1]
    return parse

def get_words(parse, period_stop=True):
    words = []
    for w in parse.split():
        if w[-1] == ')':
            words.append(w.strip(")"))
            if period_stop and words[-1] == ".":
                break
    return words


for l in gzip.open(src, 'rt'):
    if MODE == HEAD:
        title_parse = fix_paren(l.strip())
        MODE = NEXT

    if MODE == TEXT or MODE == CONTINUE:
        if l.strip() == "</TEXT>":
            instance_num += 1
            t_word_num += len(get_words(title_parse, False))
            a_word_num += len(get_words(article_parse, False))
            fa_word_num += sum([len(get_words(sent, False)) for sent in full_article_parse])
            fa_sent_num += len(full_article_parse)

            article_parse = ""
            full_article_parse = []
            MODE = NONE
        elif l.strip() not in ["<P>", "</P>"]:
            full_article_parse.append(fix_paren(l.strip()))

    if MODE == NONE and l.strip() == "<HEADLINE>":
        MODE = HEAD

    if MODE == NEXT and l.strip() == "<P>":
        MODE = TEXT

    if MODE == TEXT and l.strip() == "</P>":
        articles = []
        # Annotated gigaword has a poor sentence segmenter.
        # Ensure there is a least a period.

        for i in range(len(full_article_parse)):
            articles.append(full_article_parse[i])
            if "(. .)" in full_article_parse[i]:
                break

        article_parse = "(TOP " + " ".join(articles) + ")"
        MODE = CONTINUE

print(instance_num, file=out)
print(t_word_num, file=out)
print(a_word_num, file=out)
print(fa_word_num, file=out)
print(fa_sent_num, file=out)