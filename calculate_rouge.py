# -*- coding: utf-8 -*-

#calculate rouge score by using sumeval: https://github.com/chakki-works/sumeval
#system output is one sentence per line
#correct output can be multiple sentences per line (if multiple references setting), splitted by tab

import argparse

import numpy as np

from sumeval.metrics.rouge import RougeCalculator


def concat_tokens(tokens):
    return ''.join(tokens.split(' '))


def read_file(filename, do_concat):
    with open(filename) as f:
        if do_concat:
             lines= [concat_tokens(line.strip()) for line in f]
        else:
            lines = [line.strip() for line in f]
    if '\t' in lines[0]:
        lines = [[subline.strip() for subline in line.split('\t')]
                for line in lines]
    return lines


def main(args):
    system_out = read_file(args.system_out, args.concat_tokens)
    reference_list = read_file(args.reference, args.concat_tokens)
    rouge4one = RougeCalculator(stopwords=True, lang="ja")
    rouge4other = RougeCalculator(stopwords=False, lang="ja")
    rougeone_list = []
    rougetwo_list = []
    rougel_list = []
    for index, snt in enumerate(system_out):
        rougeone_list.append(rouge4one.rouge_1(summary=snt, references=reference_list[index]))
        rougetwo_list.append(rouge4other.rouge_2(summary=snt, references=reference_list[index]))
        rougel_list.append(rouge4one.rouge_l(summary=snt, references=reference_list[index]))
    print('ROUGE-1\t%.6f'%(np.average(rougeone_list)))
    print('ROUGE-2\t%.6f'%(np.average(rougetwo_list)))
    print('ROUGE-L\t%.6f'%(np.average(rougel_list)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--system', dest='system_output',
                        required=True, help='specify the system output file name')
    parser.add_argument('-r', '--reference', dest='reference',
                        required=True, help='specify the reference file name')
    parser.add_argument('-c', '--concat-tokens', action='store true')
    args = parser.parse_args()
    main(args)
