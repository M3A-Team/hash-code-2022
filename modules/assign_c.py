# sort based on bbd then points
def sortProj(projs):
    projs = [proj for proj in projs if proj.bbd >= proj.duration]
    return sorted(projs, key=lambda x: (x.bbd, x.points))

def getSkills(conts):
    skills = {}
    for i in conts:
        keys = i.skills.keys()
        for k in keys:
            if k in skills.keys():
                skills[k].append(i)
            else:
                skills[k] = [i]
    return skills

# sort contributors for each skill 
def sortSkills(skills):
    for i in skills:
        skills[i].sort(key=lambda x: x.skills[i])

# check for contributer to fill the role
def checkRole(r, skills, proj):
    if r in skills.keys():
        for c in skills[r]:
            if c.skills[r] >= proj.roles[r] and c.available:
                return c
#             elif c.skills[r] == level - 1:
#                 for co in proj.roles:
#                     if proj.roles[co][r] >= level:
#                         return c
#         cont = filter(lambda x: x.role[r] >= level and x.available == True, skills[r])

