import sqlite3
import tkinter as tk
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

    def __init__(self,id,national_code,name,last_name,birthday,grade):
        self.id=id 
        self.national_code=national_code 
        self.name=name 
        self.last_name=last_name 
        self.birthday=birthday 
        self.grade=grade 
    
    def __eq__(self,other):
        return self.id==other

class Translator:
    id:int=int()
    national_code:str=str()
    name:str=str()
    last_name:str=str()
    grade:str=str()
    def __str__(self):
        return f"\033[31m id:\033[0m {self.id},\033[31m national_code:\033[0m {self.national_code},\033[31m name:\033[0m {self.name},\033[31m last_name:\033[0m {self.last_name},\033[31m grade:\033[0m {self.grade}"

    def __init__(self,id,national_code,name,last_name,grade):
        self.id=id 
        self.national_code=national_code 
        self.name=name 
        self.last_name=last_name 

        self.grade=grade

    def __eq__(self,other):
        return self.id==other

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


class Esrb:
    id:int=int()
    name:str=str()
    def __str__(self):
        return f"\033[31m id:\033[0m {self.id},\033[31m name:\033[0m {self.name}"

    def __init__(self,id,name):
        self.id=id
        self.name=name

    def __eq__(self,other):
        return self.id==other

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

class Language:
    id:int=int()
    name:str=str()
    def __str__(self):
        return f"\033[31m id:\033[0m {self.id},\033[31m name:\033[0m {self.name}"

    def __init__(self,id,name):
        self.id=id
        self.name=name

    def __eq__(self,other):
        return self.id==other

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
    genres:list[Genre]=list()
    languages:list[Language]=list()
    def __init__(self,id,name,title,description,esrb_rating,publisher,resources,authors,translators,genres,languages):
        self.id=id
        self.name=name
        self.title=title
        self.description=description
        self.esrb_rating=esrb_rating
        self.publisher=publisher
        self.resources=resources
        self.authors=authors
        self.translators=translators
        self.genres=genres
        self.languages=languages

    def __str__(self):
        return f"id: {self.id},resources: {self.languages},authors: {self.authors},translators: {self.translators},genres: {self.genres},languages: {self.languages}"







class BooksDataAdapter:
    @staticmethod
    def get_all()->list:
        books=[]
        boks=cur.execute("SELECT * FROM books").fetchall()
        data_nn=cur.execute("SELECT id,name,title,description,esrb_rating_id,publisher_id,author_id,translator_id,resource_id,language_id,genre_id FROM books LEFT JOIN book_author ON books.id=book_author.book_id LEFT JOIN book_translator ON book_author.book_id=book_translator.book_id LEFT JOIN book_resource ON book_translator.book_id=book_resource.book_id LEFT JOIN book_language ON book_resource.book_id=book_language.book_id LEFT JOIN book_genre ON book_language.book_id=book_genre.book_id;").fetchall()
        resources=ResourcesDataAdapter.get_all()
        authors=AuthorsDataAdapter.get_all()
        translators=TranslatorsDataAdapter.get_all()
        genres=GenresDataAdapter.get_all()
        languages=LanguagesDataAdapter.get_all()
        for book in boks:
            res=[resource for id in set([dt[8] for dt in data_nn if dt[0]==book[0]]) for resource in resources if resource==id]
            aut=[author for id in set([dt[6] for dt in data_nn if dt[0]==book[0]]) for author in authors if author==id]
            tra=[translator for id in set([dt[7] for dt in data_nn if dt[0]==book[0]]) for translator in translators if translator==id]
            gen=[genre for id in set([dt[10] for dt in data_nn if dt[0]==book[0]]) for genre in genres if genre==id]
            lan=[language for id in set([dt[9] for dt in data_nn if dt[0]==book[0]]) for language in languages if language==id]

            books.append(Book(book[0],book[1],book[2],book[3],book[4],book[5],res,aut,tra,gen,lan))
        
        return books
    
    @staticmethod
    def delete(id:int)->bool:
        if id in cur.execute("SELECT id FROM books"):
            cur.execute(f"DELETE FROM book_author where book_id={id}")

            cur.execute(f"DELETE FROM book_translator where book_id={id}")

            cur.execute(f"DELETE FROM book_resource where book_id={id}")

            cur.execute(f"DELETE FROM book_language where book_id={id}")

            cur.execute(f"DELETE FROM book_genre where book_id={id}")

            cur.execute(f"DELETE FROM books where id={id}")

            cn.commit()
            return True
        return False
    @staticmethod
    def search(title:str="",author_name:str="",publisher_name:str="",translator_name:str="",genre_name:str="")->list:

        sql="SELECT * FROM books"
        where=""
        if title:
            where+=f" name LIKE '{title}'"
        
        if author_name:
            # author_id=cur.execute(f"SELECT id FROM authors WHERE name LIKE '{author_name}'").fetchall()[0][0]
            author_ids=set(author.id for author in AuthorsDataAdapter.search(author_name))
            where+=f" AND author_id IN '{author_ids}'"
            sql+=f" LEFT JOIN book_author ON books.id=book_author.book_id"
        
        if publisher_name:
            # publisher_id=cur.execute(f"SELECT id FROM publishers WHERE name LIKE '{publisher_name}'").fetchall()[0][0]
            publisher_ids=set(publisher.id for publisher in PublishersDataAdapter.search(f"{publisher_name}"))
            where+=f" AND publisher_id IN '{publisher_ids}'"
            
        
        if translator_name:
            # translator_id=cur.execute(f"SELECT id FROM translators WHERE name LIKE '{translator_id}'").fetchall()[0][0]
            translator_ids=set(translator.id for translator in TranslatorsDataAdapter.search(f"{translator_name}"))
            where+=f" AND translator_id IN '{translator_ids}'"
            sql+=" LEFT JOIN book_translator ON books.id=book_translator.book_id"

        if genre_name:
            # genre_id=cur.execute(f"SELECT id FROM genres WHERE name LIKE '{genre_name}'").fetchall()[0][0]
            genre_ids=set(genre.id for genre in GenresDataAdapter.search(f"{genre_name}") )
            where+=f" AND genre_id LIKE '{genre_ids}'"
            sql+=" LEFT JOIN book_genre ON books.id=book_genre.book_id"
        
        return cur.execute(f"{sql} WHERE {where.strip(" AND") if where[:4]==" AND" else where} ").fetchall()






class AuthorsDataAdapter:
    @staticmethod
    def get_all()->list:
        authors=[]
        auths=cur.execute("SELECT * FROM authors").fetchall()

        for auth in auths:
            authors.append(Author(auth[0],auth[1],auth[2],auth[3],auth[4],auth[5]))
        return authors
    @staticmethod
    def insert(author:Author)->Author:
        sql=f"INSERT INTO authors (national_code, name, last_name, birthday, grade) VALUES ('{author.national_code}','{author.name}','{author.last_name}','{author.birthday}','{author.grade}')"
        cur.execute(sql)
        cn.commit()
        author.id=cur.lastrowid
        return author   
    @staticmethod
    def delete(id:int)->bool:
        if id in cur.execute("SELECT id FROM books"):
            cur.execute(f"DELETE FROM authors where id={id}")
            cn.commit()
            return True
        return False
    @staticmethod
    def search(name:str,family:str)->list:
        return [Author(auth[0],auth[1],auth[2],auth[3],auth[4],auth[5]) for auth in cur.execute(f"SELECT * FROM authors WHERE authors.name LIKE '{name}%' AND authors.last_name LIKE '{family}%';").fetchall()]


class TranslatorsDataAdapter:
    @staticmethod
    def get_all()->list:
        translators=[]
        transls=cur.execute("SELECT * FROM translators").fetchall()

        for transl in transls:
            translators.append(Translator(transl[0],transl[1],transl[2],transl[3],transl[4]))
        return translators
    @staticmethod
    def insert(translator:Translator)->Translator:
        sql=f"INSERT INTO translators (national_code, name, last_name, birthday, grade) VALUES ('{translator.national_code}','{translator.name}','{translator.last_name}','{translator.birthday}','{translator.grade}')"
        cur.execute(sql)
        cn.commit()
        translator.id=cur.lastrowid
        return translator    
    @staticmethod
    def delete(id:int)->bool:
        if id not in cur.execute("SELECT translator_id FROM book_translator"):
            cur.execute(f"DELETE FROM translators where id={id}")
            cn.commit()
            return True
        return False
    @staticmethod
    def search(name:str,family:str)->list:
        return [Translator(trans[0],trans[1],trans[2],trans[3],trans[4]) for trans in cur.execute(f"SELECT * FROM translators WHERE translators.name LIKE '{name}%' AND translators.last_name LIKE '{family}%';").fetchall()]


class PublishersDataAdapter:
    @staticmethod
    def get_all()->list:
        publishers=[]
        puplis=cur.execute("SELECT * FROM publishers").fetchall()

        for pupli in puplis:
            publishers.append(Publisher(pupli[0],pupli[1],pupli[2],pupli[3],pupli[4],pupli[5],pupli[6]))
        return publishers
    @staticmethod
    def insert(publisher:Publisher)->Publisher:
        sql=f"INSERT INTO publishers (name, address, phone_number, fax_number, email, establish_date) VALUES ('{publisher.name}','{publisher.address}','{publisher.phone_number}','{publisher.fax_number}','{publisher.email}','{publisher.establish_date}')"
        cur.execute(sql)
        cn.commit()
        publisher.id=cur.lastrowid
        return publisher    
    @staticmethod
    def delete(id:int)->bool:
        if id not in cur.execute("SELECT publisher_id FROM books"):
            cur.execute(f"DELETE FROM publishers where id={id}")
            cn.commit()
            return True
        return False
    @staticmethod
    def search(name:str)->list:
        return [Publisher(publish[0],publish[1],publish[2],publish[3],publish[4],publish[5],publish[6]) for publish in cur.execute(f"SELECT * FROM publishers WHERE publishers.name LIKE '{name}%';").fetchall()]



class ResourcesDataAdapter:
    @staticmethod
    def get_all()->list:
        resources=[]
        resors=cur.execute("SELECT * FROM resources").fetchall()

        for resor in resors:
            resources.append(Resource(resor[0],resor[1],resor[2],resor[3]))
        return resources
    @staticmethod
    def insert(resource:Resource)->Resource:
        sql=f"INSERT INTO publishers (title, type, establish_date) VALUES ('{resource.title}','{resource.type}','{resource.establish_date}')"
        cur.execute(sql)
        cn.commit()
        resource.id=cur.lastrowid
        return resource
    @staticmethod
    def delete(id:int)->bool:
        if id not in cur.execute("SELECT resource_id FROM book_resource"):
            cur.execute(f"DELETE FROM resources where id={id}")
            cn.commit()
            return True
        return False
    @staticmethod
    def search(title:str)->list:
        return [Resource(resource[0],resource[1],resource[2],resource[3]) for resource in cur.execute(f"SELECT * FROM resources WHERE resources.name LIKE '{title}%';").fetchall()]



class EsrbsDataAdapter:
    @staticmethod
    def get_all()->list:
        esrbs=[]
        esrbses=cur.execute("SELECT * FROM esrb_ratings").fetchall()

        for esrbse in esrbses:
            esrbs.append(Esrb(esrbse[0],esrbse[1]))
        return esrbs
    
    @staticmethod
    def insert(esrb:Esrb)->Esrb:
        sql=f"INSERT INTO esrb_ratings (name) VALUES ('{esrb.name}')"
        cur.execute(sql)
        cn.commit()
        esrb.id=cur.lastrowid
        return esrb 
    
    @staticmethod
    def delete(id:int)->bool:
        if id not in cur.execute("SELECT esrb_rating_id FROM books"):
            cur.execute(f"DELETE FROM esrb_ratings where id={id}")
            cn.commit()
            return True
        return False

    @staticmethod
    def search(name:str)->list:
        return [Esrb(esrb[0],esrb[1]) for esrb in cur.execute(f"SELECT * FROM esrb_ratings WHERE esrb_ratings.esrb_name LIKE '{name}%';").fetchall()]


class GenresDataAdapter:
    @staticmethod
    def get_all()->list:
        genres=[]
        gen=cur.execute("SELECT * FROM genres").fetchall()

        for genrese in gen:
            genres.append(Genre(genrese[0],genrese[1]))
        return genres
    @staticmethod
    def insert(genre:Genre)->Genre:
        sql=f"INSERT INTO genres (name) VALUES ('{genre.name}')"
        cur.execute(sql)
        cn.commit()
        genre.id=cur.lastrowid
        return genre  
    @staticmethod
    def delete(id:int)->bool:
        if id not in cur.execute("SELECT genre_id FROM book_genre"):
            cur.execute(f"DELETE FROM genres where id={id}")
            cn.commit()
            return True
        return False
    @staticmethod
    def search(name:str)->list:
        return [Genre(genre[0],genre[1]) for genre in cur.execute(f"SELECT * FROM genres WHERE genres.name LIKE '{name}%';").fetchall()]
    @staticmethod
    def update(genre:Genre)->None:
        cur.execute(f"UPDATE genres set name='{genre.name}' WHERE id={int(genre.id)};")
        cn.commit()


class LanguagesDataAdapter:
    @staticmethod
    def get_all()->list:
        Languages=[]
        Langs=cur.execute("SELECT * FROM languages").fetchall()

        for Lang in Langs:
            Languages.append(Language(Lang[0],Lang[1]))
        return Languages
    @staticmethod
    def insert(language:Language)->Language:
        sql=f"INSERT INTO esrb_ratings (name) VALUES ('{language.name}')"
        cur.execute(sql)
        cn.commit()
        language.id=cur.lastrowid
        return language 
    @staticmethod
    def delete(id:int)->bool:
        if id not in cur.execute("SELECT language_id FROM book_language"):
            cur.execute(f"DELETE FROM languages where id={id}")
            cn.commit()
            return True
        return False
    @staticmethod
    def search(name:str)->list:
        return [Language(language[0],language[1]) for language in cur.execute(f"SELECT * FROM languages WHERE languages.name LIKE '{name}%';").fetchall()]









