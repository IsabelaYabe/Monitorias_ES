from .framework import TextEditor, WindowsInterface, MacInterface

def main():
    windows_interface = WindowsInterface()
    app = TextEditor(windows_interface)

    print("--- Creating a document ---")
    doc = app.new_document(name="atividade")
    doc.content = "Conteúdo da atividade"
    doc.font = "Arial"
    doc.font_size = 14

    print("--- Saving the document ---")
    doc.save()    

    print("--- Modifying the document ---")
    doc.content = "Conteúdo modificado da atividade"
    doc.font_size = 16
    print(f"Modified content: {doc.content}")
    print(f"Font: {doc.font}")
    print(f"Font size: {doc.font_size}")

    print("--- Reverting the document ---")
    doc.revert()
    print(f"Reverted content: {doc.content}")
    print(f"Font: {doc.font}")
    print(f"Font size: {doc.font_size}")

    print("--- Closing the document ---")
    app.close_document("atividade")

if __name__ == "__main__":
    main()