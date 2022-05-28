class Contributor:
    # class variable
    contributors = 0
    
    # constructor
    def __init__(self, name=None, skills=None):
        self.name = name
        self.skills = skills
        self.available = True
        self.curTitle = ""
        
        Contributor.contributors += 1
        
    def improve(self, project):
        if self.skills[self.curTitle] <= project.roles[self.curTitle]:
            self.skills[self.curTitle] += 1
            
        # free this contributor
        self.curTitle = ""
        self.available = True