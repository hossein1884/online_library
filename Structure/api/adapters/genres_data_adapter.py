from models.genre import Genre

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
