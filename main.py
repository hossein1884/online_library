from app.api.models.book import Book
from app.api.models.author import Author
from app.api.models.esrb import Esrb
from app.api.models.language import Language
from app.api.models.resource import Resource
from app.api.models.publisher import Publisher
from app.api.models.genre import Genre
from app.api.models.translator import Translator

es1=Esrb(id=1,name="+18")
ge1=Genre(id=1,name="horror")
l1=Language(id=1,name="french")
re1=Resource(id=1,title="jafa abad",type="google",establish_date="1234")
tr1=Translator(id=1,national_code="123456",name="jafar",last_name="mamdi",grade="Doctor")
p1=Publisher(id=1,name="ali",address="every",phone_number="123345",fax_number="12345678",email="gafar@gamil.com",establish_date="acva")
au1=Author(id=1,national_code="123456",name="jafar",last_name="mamdi",grade="Doctor",birthday="fsfww")

b1=Book(1,"book1","americans","",es1,p1,[re1],[au1],[tr1],[ge1],[l1])
print(b1)