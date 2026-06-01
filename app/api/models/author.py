class Author:
    id:int=int()
    national_code:str=str()
    name:str=str()
    last_name:str=str()
    birthday:str=str()
    grade:str=str()
    def __str__(self):
        return f"\033[31m id:\033[0m {self.id},\033[31m national_code:\033[0m {self.national_code},\033[31m name:\033[0m {self.name},\033[31m last_name:\033[0m {self.last_name},\033[31m birthday:\033[0m {self.birthday},\033[31m grade:\033[0m {self.grade}"

    def __init__(self,id,national_code,name,last_name,birthday,grade):
        self.id=id 
        self.national_code=national_code 
        self.name=name 
        self.last_name=last_name 
        self.birthday=birthday 
        self.grade=grade 
    
    def __eq__(self,other):
        return self.id==other
