class Dog:
    name = str()
    gender = str()
    
    def __init__(self, name, gender):
        self.name  = str(name)
        self.gender = str(gender)

puffy = Dog("puffy", "Boy")