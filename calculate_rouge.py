# -*- coding: utf-8 -*-

#calculate rouge score by using sumeval: https://github.com/chakki-works/sumeval
#system output is one sentence per line
#correct output can be multiple sentences per line (if multiple references setting), splitted by tab


import sys
import collections
import numpy as np
from sumeval.metrics.rouge import RougeCalculator
import argparse


def read_file(filename):
    return [line.strip() if not '\t' in line else [subline.strip() for subline in line.strip().split('\t')] for line in open(filename)]


def main(args):
    system_out = read_file(args.system_output)
    reference_list = read_file(args.reference)
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
    args = parser.parse_args()
    main(args)
