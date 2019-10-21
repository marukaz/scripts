import argparse

from sumeval.metrics.rouge import RougeCalculator


def concat(snt):
    snt = snt.replace(' ', '')
    if snt.startswith('▁'):
        snt= snt[1:]
    return snt


def main(args):
    if args.rouge == '1':
        RC = RougeCalculator(stopwords=True, lang=args.lang)
        rouge = RC.rouge_1
    else:
        RC = RougeCalculator(stopwords=False, lang=args.lang)
        if args.rouge == '2':
            rouge = RC.rouge_2
        else:
            rouge = RC.rouge_l

    line_num = 0
    detect_num = 0
    with open(args.path1) as f1, open(args.path1src) as f1s, open(args.path2) as f2, open(args.path2src) as f2s:
        for l1, l1s, l2, l2s in zip(f1, f1s, f2, f2s):
            line_num += 1
            if args.concat_tokens:
                l1s = concat(l1s)
                l1 = concat(l1)
                l2s = concat(l2s)
                l2 = concat(l2)
            score = rouge(summary=l1, references=l2)
            if score < args.threshold:
                detect_num += 1
                print(l1s, '=====> '+l1, l2s, '=====> '+l2)
    print()
    print('lines: ', line_num)
    print('detect: ', detect_num)
    print(f'detected percent: {f:.2%}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('path1src')
    parser.add_argument('path1')
    parser.add_argument('path2src')
    parser.add_argument('path2')
    parser.add_argument('-r', '--rouge', choices=['1', '2', 'l'], default='1')
    parser.add_argument('-t', '--threshold', type=float, default=0.8, help='Detect if the rouge score is lower than this threshold.')
    parser.add_argument('-l', '--lang', default='ja')
    parser.add_argument('-c', '--concat-tokens', action='store_true')
    args = parser.parse_args()
    main(args)

