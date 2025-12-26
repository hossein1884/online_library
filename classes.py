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

    def __init__(self,id,national_code,name,last_name,birthday,grade):
        self.id=id 
        self.national_code=national_code 
        self.name=name 
        self.last_name=last_name 
        self.birthday=birthday 
        self.grade=grade 
    

class Translator:
    id:int=int()
    national_code:str=str()
    name:str=str()
    last_name:str=str()
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

class Resource:
    id:int=int()
    title:str=str()
    type:str=str()
    establish_date:str=str()
    def __str__(self):
        return f"\033[31m id:\033[0m {self.id},\033[31m title:\033[0m {self.title},\033[31m type:\033[0m {self.type},\033[31m establish_date:\033[0m {self.establish_date}"
    
    def __eq__(self,other):
        return self.id==other.id

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

class Genre:
    id:int=int()
    name:str=str()
    def __str__(self):
        return f"\033[31m id:\033[0m {self.id},\033[31m name:\033[0m {self.name}"

    def __init__(self,id,name):
        self.id=id
        self.name=name

class Language:
    id:int=int()
    name:str=str()
    def __str__(self):
        return f"\033[31m id:\033[0m {self.id},\033[31m name:\033[0m {self.name}"

    def __init__(self,id,name):
        self.id=id
        self.name=name

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






class BooksDataAdapter:
    @staticmethod
    def get_all()->list:
        books=[]
        boks=cur.execute("SELECT * FROM books")
        data_nn=cur.execute("SELECT id,name,title,description,esrb_rating_id,publisher_id,author_id,translator_id,resource_id,language_id,genre_id FROM books INNER JOIN book_author ON books.id=book_author.book_id INNER JOIN book_translator ON book_author.book_id=book_translator.book_id INNER JOIN book_resource ON book_translator.book_id=book_resource.book_id INNER JOIN book_language ON book_resource.book_id=book_language.book_id INNER JOIN book_genre ON book_language.book_id=book_genre.book_id;")
        resources=ResourcesDataAdapter.get_all()
        authors=AuthorsDataAdapter.get_all()
        translators=TranslatorsDataAdapter.get_all()
        genres=GenresDataAdapter.get_all()
        languages=LanguagesDataAdapter.get_all()
        for book in boks:
            
            res=[resource for id in [dt[8] for dt in data_nn if dt[0]==book[0]] for resource in resources if resource==id]
            aut=[author for id in [dt[6] for dt in data_nn if dt[0]==book[0]] for author in authors if author==id]
            tra=[translator for id in [dt[7] for dt in data_nn if dt[0]==book[0]] for translator in translators if translator==id]
            gen=[genre for id in [dt[10] for dt in data_nn if dt[0]==book[0]] for genre in genres if genre==id]
            lan=[language for id in [dt[9] for dt in data_nn if dt[0]==book[0]] for language in languages if language==id]

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



class AuthorsDataAdapter:
    @staticmethod
    def get_all()->list:
        authors=[]
        auths=cur.execute("SELECT * FROM authors")

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



class TranslatorsDataAdapter:
    @staticmethod
    def get_all()->list:
        translators=[]
        transls=cur.execute("SELECT * FROM translators")

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



class PublishersDataAdapter:
    @staticmethod
    def get_all()->list:
        publishers=[]
        puplis=cur.execute("SELECT * FROM publishers")

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



class ResourcesDataAdapter:
    @staticmethod
    def get_all()->list:
        resources=[]
        resors=cur.execute("SELECT * FROM resources")

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



class EsrbsDataAdapter:
    @staticmethod
    def get_all()->list:
        esrbs=[]
        esrbses=cur.execute("SELECT * FROM esrb_ratings")

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



class GenresDataAdapter:
    @staticmethod
    def get_all()->list:
        genres=[]
        genres=cur.execute("SELECT * FROM genres")

        for genrese in genres:
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



class LanguagesDataAdapter:
    @staticmethod
    def get_all()->list:
        Languages=[]
        Langs=cur.execute("SELECT * FROM languages")

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



b1=BooksDataAdapter.get_all()
print(b1)