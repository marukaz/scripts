import argparse
import sys
from pathlib import Path

from sumeval.metrics.rouge import RougeCalculator


def detokenize(line):
    line = line.replace(' ', '')
    line = line.replace('▁', ' ')
    return line


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
    ref_path = Path(args.reference)
    sys_path = Path(args.system)
    frs = open(args.reference_source) if args.reference_source else None
    fss = open(args.system_source) if args.system_source else None
    if args.filter_mode:
        filtered_dir = ref_path.parent/f'filter_{args.threshold}_RG{args.rouge}'
        filtered_dir.mkdir(exist_ok=True)
        ref_save = filtered_dir/ref_path.name
        ref_fo = ref_save.open('w') 
        sys_save = filtered_dir/sys_path.name
        sys_fo = sys_save.open('w') 
    with ref_path.open() as fr, sys_path.open() as fs:
        for lr, ls in zip(fr, fs):
            if frs:
                ref_source = frs.readline()
            if fss:
                sys_source = fss.readline()
            line_num += 1
            if args.detokenize:
                lr = detokenize(lr)
                ls = detokenize(ls)
            score = rouge(summary=ls, references=lr)
            if args.filter_mode:
                if score > args.threshold:
                    ref_fo.write(lr)
                    sys_fo.write(ls)
            else:
                # detect gushed examples
                if score < args.threshold:
                    detect_num += 1
                    if frs:
                        r_out = 'reference source:\n' + ref_source + '=====> ' + lr
                    else:
                        r_out = 'reference summary:\n' + '=====> ' + lr
                    if fss:
                        s_out = 'system source:\n' + sys_source + '=====> ' + ls
                    else:
                        s_out = 'system summary:\n' + '=====> ' + ls
                    print(r_out.strip())
                    print(s_out.strip())
                    print()
    if not args.filter_mode:
        print()
        print('lines: ', line_num)
        print('detect: ', detect_num)
        print(f'detected percent: {detect_num/line_num:.2%}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('reference')
    parser.add_argument('system')
    parser.add_argument('-rs', '--reference-source')
    parser.add_argument('-ss', '--system-source')
    parser.add_argument('--rouge', choices=['1', '2', 'l'], default='1')
    parser.add_argument('-t', '--threshold', type=float, default=0.8, help='Detect if the rouge score is lower than this threshold.')
    parser.add_argument('-l', '--lang', default='ja')
    parser.add_argument('-d', '--detokenize', action='store_true')
    parser.add_argument('-f', '--filter-mode', action='store_true')
    args = parser.parse_args()
    main(args)

