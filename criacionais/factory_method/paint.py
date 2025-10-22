import Document, Application

class Drawing(Document):
    def __init__(self):
        self._name = None
        self._contet = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def rename(self, name):
        self.__name = name
    
    @property
    def content(self):
        return self.__content

    @content.setter
    def redraw(self, content):
        self.__content = content
        
    def Open(self):
        print("")

class Paint(Application):
    
    def new_document(): ...
        
    def create_document(): ...