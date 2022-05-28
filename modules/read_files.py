from __init__ import dirname
from modules.contributer import Contributor
from modules.project import Project

def get_numbers(file):
    c_no, p_no = file.readline()[:-1].split(" ")
    return int(c_no), int(p_no)

def fill_contributer(file):
    name, s_no = file.readline()[:-1].split(" ")
    skills = {}
    for _ in range(int(s_no)):
        s_name, lvl = file.readline()[:-1].split(" ")
        skills[s_name] = int(lvl)
    return Contributor(name, skills)

def fill_project(file):
    name, dur, score, bb, r_no = file.readline()[:-1].split(" ")
    roles = {}
    for _ in range(int(r_no)):
        s_name, lvl = file.readline()[:-1].split(" ")
        roles[s_name] = int(lvl)
    return Project(name, int(dur), int(score), int(bb), roles)

def get_files(path, files):
    for i in range(len(files)):
        with open(path + '/' + files) as file:
            c_no, p_no = get_numbers(file)

            c_list = []
            p_list = []

            for _ in range(int(c_no)):
                c_list.append(fill_contributer(file))

            for _ in range(int(p_no)):
                p_list.append(fill_project(file))

            return c_list, p_list