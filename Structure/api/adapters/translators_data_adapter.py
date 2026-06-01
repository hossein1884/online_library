from models.translator import Publisher

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
