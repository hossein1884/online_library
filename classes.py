import sqlite3

cn = sqlite3.connect("books.db")
cur=cn.cursor()


class Author:
    id:int=int()
    national_code:str=str()
    name:str=str()
    last_name:str=str()
    birthday:str=str()
    grade:str=str()
    def __str__(self):
        return f"\033[31m id:\033[0m {self.id},\033[31m national_code:\033[0m {self.national_code},\033[31m name:\033[0m {self.name},\033[31m last_name:\033[0m {self.last_name},\033[31m birthday:\033[0m {self.birthday},\033[31m grade:\033[0m {self.grade}"


class Translator:
    id:int=int()
    national_code:str=str()
    name:str=str()
    last_name:str=str()
    grade:str=str()
    def __str__(self):
        return f"\033[31m id:\033[0m {self.id},\033[31m national_code:\033[0m {self.national_code},\033[31m name:\033[0m {self.name},\033[31m last_name:\033[0m {self.last_name},\033[31m birthday:\033[0m {self.birthday},\033[31m grade:\033[0m {self.grade}"

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

class Resource:
    id:int=int()
    title:str=str()
    type:str=str()
    establish_date:str=str()
    def __str__(self):
        return f"\033[31m id:\033[0m {self.id},\033[31m title:\033[0m {self.title},\033[31m type:\033[0m {self.type},\033[31m establish_date:\033[0m {self.establish_date}"

class Esrb:
    id:int=int()
    name:str=str()
    def __str__(self):
        return f"\033[31m id:\033[0m {self.id},\033[31m name:\033[0m {self.name}"

class Genre:
    id:int=int()
    name:str=str()
    def __str__(self):
        return f"\033[31m id:\033[0m {self.id},\033[31m name:\033[0m {self.name}"

class Language:
    id:int=int()
    name:str=str()
    def __str__(self):
        return f"\033[31m id:\033[0m {self.id},\033[31m name:\033[0m {self.name}"

class Book:
    id:int=int()
    name:str=str()
    title:str=str()
    description:str=str()
    esrb_rating:Esrb=None
    publisher:Publisher=None
    resources:list[Resource]=list()
    authors:list[Author]=list
    translators:list[Translator]=list()
    genreses:list[Genre]=list()
    languages:list[Language]=list()
    










class AuthorsDataAdapter:
    @staticmethod
    def get_all()->list:
        authors=[]
        cn=sqlite3.connect("students.db")
        cur=cn.cursor()
        auths=cur.execute("SELECT * FROM authors")

        for auth in auths:
            authors.append(Author(auth[0],auth[1],auth[2],auth[3],auth[4],auth[5]))
        return authors
    




class TranslatorsDataAdapter:
    @staticmethod
    def get_all()->list:
        translators=[]
        cn=sqlite3.connect("students.db")
        cur=cn.cursor()
        transls=cur.execute("SELECT * FROM translators")

        for transl in transls:
            translators.append(Translator(transl[0],transl[1],transl[2],transl[3],transl[4]))
        return translators
    



class PublishersDataAdapter:
    @staticmethod
    def get_all()->list:
        publishers=[]
        cn=sqlite3.connect("students.db")
        cur=cn.cursor()
        puplis=cur.execute("SELECT * FROM publishers")

        for pupli in puplis:
            publishers.append(Publisher(pupli[0],pupli[1],pupli[2],pupli[3],pupli[4],pupli[5],pupli[6]))
        return publishers
    




class ResourcesDataAdapter:
    @staticmethod
    def get_all()->list:
        resources=[]
        cn=sqlite3.connect("students.db")
        cur=cn.cursor()
        resors=cur.execute("SELECT * FROM resources")

        for resor in resors:
            resources.append(Resource(resor[0],resor[1],resor[2],resor[3]))
        return resources
    



class EsrbsDataAdapter:
    @staticmethod
    def get_all()->list:
        esrbs=[]
        cn=sqlite3.connect("students.db")
        cur=cn.cursor()
        esrbses=cur.execute("SELECT * FROM esrb_ratings")

        for esrbse in esrbses:
            esrbs.append(Esrb(esrbse[0],esrbse[1]))
        return esrbs





class GenresDataAdapter:
    @staticmethod
    def get_all()->list:
        genres=[]
        cn=sqlite3.connect("students.db")
        cur=cn.cursor()
        genreses=cur.execute("SELECT * FROM genres")

        for genrese in genreses:
            genres.append(Genre(genrese[0],genrese[1]))
        return genres
    



class LanguagesDataAdapter:
    @staticmethod
    def get_all()->list:
        Languages=[]
        cn=sqlite3.connect("students.db")
        cur=cn.cursor()
        Langs=cur.execute("SELECT * FROM languages")

        for Lang in Langs:
            Languages.append(Language(Lang[0],Lang[1]))
        return Languages


