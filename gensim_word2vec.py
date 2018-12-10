import argparse
import logging
import sys

from gensim.models import word2vec


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def main(args):
    sentences = word2vec.LineSentence(args.loadfile)
    model = word2vec.Word2Vec(sentences)
    model.save(args.savefile)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('loadfile')
    parser.add_argument('savefile', default='word2vec.model')
    args = parser.parse_args()
    main(args)
