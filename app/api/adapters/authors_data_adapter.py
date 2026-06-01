from models.author import Author

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
