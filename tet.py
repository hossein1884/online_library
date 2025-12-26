# import sqlite3

# cn = sqlite3.connect("books.db")
# cur=cn.cursor()




# class Resource:
#     id:int=int()
#     title:str=str()
#     type:str=str()
#     establish_date:str=str()
#     def __str__(self):
#         return f"\033[31m id:\033[0m {self.id},\033[31m title:\033[0m {self.title},\033[31m type:\033[0m {self.type},\033[31m establish_date:\033[0m {self.establish_date}"
    
#     def __eq__(self,other):
#         return self.id==other.id





# class Book:
#     id:int=int()
#     name:str=str()
#     title:str=str()
#     description:str=str()
#     resources:list[Resource]=list()






# class BooksDataAdapter:
#     @staticmethod
#     def get_all()->list:
#         books=[]
#         boks=cur.execute("SELECT * FROM books")
#         resources=ResourcesDataAdapter.get_all()
#         book_resource=cur.execute("SELECT * FROM book_resource")
#         for book in boks:
#             if book[0] in resources:
#                 print(resources)
#         return books

# class ResourcesDataAdapter:
#     @staticmethod
#     def get_all()->list:
#         resources=[]
#         resors=cur.execute("SELECT * FROM resources")

#         for resor in resors:
#             resources.append(Resource(resor[0],resor[1],resor[2],resor[3]))
#         return resources
#     @staticmethod
#     def insert(resource:Resource)->Resource:
#         sql=f"INSERT INTO publishers (title, type, establish_date) VALUES ('{resource.title}','{resource.type}','{resource.establish_date}')"
#         cur.execute(sql)
#         cn.commit()
#         resource.id=cur.lastrowid
#         return resource
#     @staticmethod
#     def delete(id:int)->bool:
#         if id not in cur.execute("SELECT resource_id FROM book_resource"):
#             cur.execute(f"DELETE FROM resources where id={id}")
#             cn.commit()
#             return True
#         return False



# b1=BooksDataAdapter()
# b1.get_all()




dt={1:"ali",2:"hossein",}