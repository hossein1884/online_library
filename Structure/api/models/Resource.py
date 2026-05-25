class Resource:
    id:int=int()
    title:str=str()
    type:str=str()
    establish_date:str=str()
    def __str__(self):
        return f"\033[31m id:\033[0m {self.id},\033[31m title:\033[0m {self.title},\033[31m type:\033[0m {self.type},\033[31m establish_date:\033[0m {self.establish_date}"
    
    def __eq__(self,other):
        return self.id==other

    def __init__(self,id,title,type,establish_date):
        self.id=id
        self.title=title
        self.type=type
        self.establish_date=establish_date
