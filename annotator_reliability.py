"""
Code to evaluate inter-annotator agreement

data layout:
[sent_num, #anno-id]
['', '#text:]
['', tok_num, token, LU, frame, silverFE,
[0 ,    1   ,   2  , 3 ,   4  ,    5    ,
 proposed_goldFE, match?, JH, Peace]
        6       ,   7   , 8 , 9    ]

to handle: '?' in proposed_goldFE
training_sub2 sent 33 no agreement

@author Peace Han
"""
import os
# TODO: calculate the scores for only non-Os
path = 'data/corrected/'
listing = os.listdir(path)
sent_count = 0            # number of sentences
tok_count = 0             # number of tokens
o_count = 0               # number of O tokens
fe_count = 0              # number of frame element tokens
weighted_tok_count = 0    # weighted number of tokens
agr_score = 0.0           # number of tokens with inter-rater agreement
fe_score = 0.0            # number of fe tokens with inter-rater agreement
weighted_agr_score = 0.0  # weighted agreement score
net_change = 0            # net changes made from silver to gold
for file in listing:
    f = open(path + file)
    # print("current file: " + file)
    next(f)  # skip header
    for line in f:
        if line.strip():  # skip blank lines
            line = line.rstrip()
            line = line.split('\t')
            # print(line)
            weight = 1
            try:
                silver = line[5]
                gold = line[6]
                if line[6] == 'O':
                    weight = 0.5
                    o_count += 1
                else:
                    fe_count += 1
                    fe_score += int(line[7])
                # print(line[7])
                tok_count += 1
                weighted_tok_count += weight * 1
                agr_score += int(line[7])
                weighted_agr_score += weight * int(line[7])
                net_change += int(silver != gold)
            except IndexError:
                if '#anno-id' in line[1]:
                    sent_count += 1
    f.close()

print("total number of sentences in doc:", sent_count)
print('net changes made:', net_change)
print()
print('total number of tokens:', tok_count)
print('total number of tokens with same judgment:', agr_score)
print('total number of "O" tokens:', o_count)
assert tok_count - o_count == fe_count
print('unweighted agreement score:', agr_score / tok_count)
print()
print('total number of frame element tokens:', tok_count - o_count)
print('total number of frame elements with same judgment', fe_score)
print('fe_score:', fe_score / fe_count)
print()
print('weighted_agr_score:', weighted_agr_score)
print('weighted_tok_count:', weighted_tok_count)
print('weighted agreement score:', weighted_agr_score / weighted_tok_count)

