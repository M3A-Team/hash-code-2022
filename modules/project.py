from modules.contributer import Contributor

class Project:
    # class variable
    projects = 0
    
    # constructor
    def __init__(self, name=None, duration=None, points=None, bbd=None, roles=None):
        self.name = name
        self.duration = duration
        self.points = points
        self.bbd = bbd
        self.roles = roles
        self.status = 0
        self.s_day = 0
        self.day = 0
        self.contributers = {}
        
        Project.projects += 1

    def execute(self, day):
        self.s_day = day
        self.day = day
        self.status = 1

    def update(self):
        if self.day < self.s_day + self.duration:
            self.day += 1
        else:
            self.status = -1
            for r, c in self.contributers.items():
                c.improve(self)