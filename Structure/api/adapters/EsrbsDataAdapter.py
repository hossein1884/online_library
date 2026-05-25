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

