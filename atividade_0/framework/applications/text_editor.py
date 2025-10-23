from .application import Application
from framework.documents.text_document import TextDocument

class TextEditor(Application):
    def create_document(self, name: str):
        return TextDocument(name)
