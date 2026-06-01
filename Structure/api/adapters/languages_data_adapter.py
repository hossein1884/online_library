from models.language import Language

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

