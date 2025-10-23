from framework.applications import TextEditor
from framework.interface.mac_interface import MacInterface
from framework.interface.windows_interface import WindowsInterface

if __name__ == "__main__":
    app = TextEditor()
    interface = MacInterface() 

    doc1 = app.new_document("resumo.txt")
    doc1.content = "Anotações sobre padrões de projeto"
    doc1.save()

    window = interface.create_window()
    cursor = interface.create_cursor()

    window.draw()
    cursor.move()

    doc2 = app.new_document("resumo.txt")
    print(doc1 is doc2)
