from koreanframenet import koreanframenet
version = 1.1
kfn = koreanframenet.interface(version=version)

lus = kfn.lus_by_word('입증하다')
[print(lu) for lu in lus]

annotations = kfn.annotations_by_lu(5566)
[print(annotation) for annotation in annotations]


class Schema:
    def __init__(self, name, roles, constraints):
        self.name = name
        self.roles = roles
        self.constraints = constraints

    def __str__(self):
        return "schema {}\n\thas roles {}\n\thas constraints {}".format(self.name,
                                                                        self.roles,
                                                                        self.constraints)


roles = {}
roles['mover'] = 'Entity'
roles['goal'] = 'Location'
roles['path'] = 'SPG'
roles['action'] = 'Xschema'
roles['time'] = 'Time'


ex = Schema("Run", roles, "RUN-XSCHEMA")
print(ex)

