"""
Code to divide up training sub into smaller files
    max 100 sentences in each file
@author Peace Han
"""

import pprint

version = 1.1
path = 'koreanframenet/data/{}/'.format(version)
file = 'training.tsv'
sub_path = 'data/'
sub = 'training_sub{}.tsv'

# file = 'test.tsv'
i = 0
j = 1
f = open(path + file)
out = open(path + sub.format(j), 'w')
sub_list = []
for line in f:
    # if i < 100:
    #     sub_list.append(line)
    #     out.write(line)
    if "#anno-id:" in line:
        i += 1
    if i == 100:
        sub_list = []
        out.close()
        j += 1
        i = 0
        out = open(path + sub.format(j), 'w')
        sub_list.append(line)
    out.write(line)

print(i, j)

out.close()
f.close()

