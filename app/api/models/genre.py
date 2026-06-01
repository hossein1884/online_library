class Genre:
    id:int=int()
    name:str=str()
    def __str__(self):
        return f"\033[31m id:\033[0m {self.id},\033[31m name:\033[0m {self.name}"

    def __init__(self,id,name):
        self.id=id
        self.name=name

    def __eq__(self,other):
        return self.id==other
