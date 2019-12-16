import argparse
from pathlib import Path


parser = argparse.ArgumentParser()
parser.add_argument('dir')
args = parser.parse_args()

file_dir = Path(args.dir)

instance_num = 0
t_word_num = 0
a_word_num = 0
fa_word_num = 0
fa_sent_num = 0

for path in file_dir.glob('*'):
    with path.open() as f:
        data = f.read()
        i, t, a, faw, fas, _ = data.split('\n')
        instance_num += int(i)
        t_word_num += int(t)
        a_word_num += int(a)
        fa_word_num += int(faw)
        fa_sent_num += int(fas)

print('instance num:', instance_num)
print('total title word num:', t_word_num)
print('total article word num:', a_word_num)
print('total full article word num:', fa_word_num)
print('total full article sent num:', fa_sent_num)
print('avg. title word num:', t_word_num/instance_num)
print('avg. article word num:', a_word_num/instance_num)
print('avg. full article word num:', fa_word_num/instance_num)
print('avg. full article sent num:', fa_sent_num/instance_num)