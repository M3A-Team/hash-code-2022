from __init__ import dirname, FILES
from modules.read_files import *
from modules.write_files import *
from modules.assign_c import *



for i in range(len(FILES)):

    DAY = 0

    FLAG = 1

    c_list, p_list = get_files(dirname + '/input', FILES[i])
    p_list = sortProj(p_list)

    skills = getSkills(c_list)
    sortSkills(skills)

    running_projects = []
    finished_projects = []

    while FLAG > 0:
        for proj in p_list:
            if proj.status == 0:
                ass_roles = {}
                for r in proj.roles:
                    potential = checkRole(r, skills, proj)
                    if potential != None:    
                        ass_roles[r] =  potential
                if len(ass_roles) == len(proj.roles):
                    for ro in ass_roles.keys():
                        ass_roles[ro].curTitle = ro
                        ass_roles[ro].available = False
                    proj.contributers = ass_roles
                    proj.execute(DAY)
                    running_projects.append(proj)
    
        for proj in running_projects:
            proj.update()
            if proj.status == -1:
                finished_projects.append(proj)
                running_projects.remove(proj)

        if len(running_projects) == 0:
            FLAG += 1
            print(FLAG)
        
        if FLAG > 10 or len(finished_projects) == len(p_list):
            FLAG = 0

        DAY += 1
    print("Writing File No. " + str(i+1))
    write_file(finished_projects, i)