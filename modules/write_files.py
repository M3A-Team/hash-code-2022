from __init__ import dirname

def write_file(finished_list, i):
    with open(dirname + '/output/output_no_' + str(i+1) + ".txt", 'w') as file:
        no = len(finished_list)
        file.write(str(no) + '\n')
        for j in range(no):
            file.write(finished_list[j].name + '\n')
            names = [c.name for c in finished_list[j].contributers.values()]
            file.write(" ".join(names) + '\n')


