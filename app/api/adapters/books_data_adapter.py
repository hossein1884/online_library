from app.api.models.book import Book
from .authors_data_adapter import AuthorsDataAdapter
from .resources_data_adapter import ResourcesDataAdapter
from .translators_data_adapter import TranslatorsDataAdapter
from .languages_data_adapter import LanguagesDataAdapter
from .genres_data_adapter import GenresDataAdapter
from app.database.db_manager import cn, cur


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

