from .application import Application
from ..documents.text_document import TextDocument

class TextEditor(Application):
    def _create_document(self, name: str) -> TextDocument:
        return TextDocument(name)
