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
