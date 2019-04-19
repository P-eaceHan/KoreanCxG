import pprint
from koreanframenet import koreanframenet
version = 1.1
kfn = koreanframenet.interface(version=version)

# lus = kfn.lus_by_word('입증하다')
# [print(lu) for lu in lus]
#
# annotations = kfn.annotations_by_lu(5564)
# [print(annotation) for annotation in annotations]
#
# definition = kfn.get_frame_definition('Verification')
# print(definition)
#
# sentence = '동물의 효험 연구에서, Anthim은 한 번의 예방 투여량으로 탄저병 포자의 도전에 대해 완전한 보호를 입증하였고 치명적인 도전 후 최대 이틀 간의 투여 시 상당한 보호를 보여주었다.'
#

path = 'koreanframenet/data/1.1/'
file = 'training.tsv'
sub = 'training_sub{}.tsv'

# f = open(path + file)
# # o = open(path + sub, 'w')
# i = 0
# for line in f:
#     # line = line.strip()
#     # if i != 0:
#     if "#text:" in line:
#         i += 1
#         # o.write(line)
#         print(line)
# print(i)
# f.close()

# def collect100sents(filename, outfile, count):
#     f = open(filename)
#     out = open(outfile.format(count), 'w')
#     for line in f:



file = 'test.tsv'
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

#     if i == 100:
#         out.close()
#         j += 1
#         out = open(path + sub.format(j), 'w')
#     if "#anno-id:" in line:
#         i += 1
#     out.write(line)


out.close()
f.close()

# file = 'training_sub1.tsv'
# f = open(path+ file)
# for line in f:
#     print(line)
#     if "#anno-id:" in line:
# class Schema:
#     def __init__(self, name, roles, constraints):
#         self.name = name
#         self.roles = roles
#         self.constraints = constraints
#
#     def __str__(self):
#         return "schema {}\n\thas roles {}\n\thas constraints {}".format(self.name,
#                                                                         self.roles,
#                                                                         self.constraints)
#
#
# roles = {}
# roles['mover'] = 'Entity'
# roles['goal'] = 'Location'
# roles['path'] = 'SPG'
# roles['action'] = 'Xschema'
# roles['time'] = 'Time'
#
#
# ex = Schema("Run", roles, "RUN-XSCHEMA")
# print(ex)

