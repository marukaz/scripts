import argparse
import logging

from gensim.models import word2vec


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def main(args):
    model = word2vec.Word2Vec(corpus_file=args.load, sg=1, min_count=0, workers=8)
    model.wv.save_word2vec_format(args.save)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--load')
    parser.add_argument('-s', '--save', default='word2vec.model')
    args = parser.parse_args()
    main(args)
