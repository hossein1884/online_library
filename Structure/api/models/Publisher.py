class Publisher:
    id:int=int()
    name:str=str()
    address:str=str()
    phone_number:str=str()
    fax_number:str=str()
    email:str=str()
    establish_date:str=str()
    def __str__(self):
        return f"\033[31m id:\033[0m {self.id},\033[31m name:\033[0m {self.name},\033[31m address:\033[0m {self.address},\033[31m phone_number:\033[0m {self.phone_number},\033[31m fax_number:\033[0m {self.fax_number},\033[31m email:\033[0m {self.email},\033[31m establish_date:\033[0m {self.establish_date}"

    def __init__(self,id,name,address,phone_number,fax_number,email,establish_date):
        self.id=id  
        self.name=name 
        self.address=address 
        self.phone_number=phone_number 
        self.fax_number=fax_number
        self.email=email
        self.establish_date=establish_date

    def __eq__(self,other):
        return self.id==other
