from abc import ABC, abstractmethod

class  Document(ABC):
    def __init__(self, path: str):
        self.path = path
    
    @abstractmethod
    def extract_title(self) -> str: ...

    @abstractmethod
    def extract_authors(self) -> list[str]: ...

class ArticleDocument(Document):
    def extract_title(self):
       title = self.path["title"] 
       return title 

    def extract_authors(self):
        authors = self.path["authors"]
        return authors

    def extract_doi(self):
        doi = self.path["DOI"]
        return doi

class BookDocument(Document):
    def extract_title(self):
        title = self.path["title"] 
        return title  
    def extract_authors(self):
        authors = self.path["authors"]
        return authors

class DocumentCreator(ABC):
    def __init__(self):
        self.open = None
        self.title = None
        self.authors = None

    def _validate_title_authors(self) -> bool:
        if self.title == "" or self.title is None:
            raise ValueError("O documento é inválido!")
        if len(self.authors) < 1 or self.authors is None:
            raise ValueError("O documento é inválido!")
        return True

    @abstractmethod
    def create_document(self, path) -> Document: ...

    @abstractmethod
    def _validate(self) -> bool: ...

class DefaultDocumentCreator(DocumentCreator):        
    def _validate(self):
        return self._validate_title_authors()

    def create_document(self, path) -> Document:
        document = BookDocument(path)
        self.title = document.extract_title()
        self.authors = document.extract_authors()
        print(f"Create book: \ntitle:{"self.title"}\nAuthors {self.authors}")
        self._validate()
        self.open = True
        return document

class AticleDocumentCreator(DocumentCreator):    
    def __init__(self):
        self.doi: str = None

    def _validate(self):
        self._validate_title_authors()
        if self.doi == "" or self.doi is None:
            raise ValueError("O documento não é válido")
        return True
    def create_document(self, path) -> Document:
        document = BookDocument(path)
        self.title = document.extract_title()
        self.authors = document.extract_authors()
        self.doi = document.extract_doi()
        self.open = True

if __name__ == "__main__":
    article = {"title": "artigo", "authors": ["A", "B"], "DOI": "111.11"}
    book = {"title": "livro", "authors": ["A", "C"]}

    book_create = DefaultDocumentCreator()
    book_create.create_document(book)

    book_create = DefaultDocumentCreator()
    book_create.create_document(book)
