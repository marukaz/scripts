import argparse


parser = argparse.ArgumentParser()
parser.add_argument('data')
parser.add_argument('filter')
args = parser.parse_args()

with open(args.data) as f1, open(args.filter) as f2:
    for line, flag in zip(f1, f2):
        if flag == '1':
            print(line)