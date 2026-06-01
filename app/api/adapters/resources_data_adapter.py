from app.api.models.resource import Resource

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
