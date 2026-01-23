from framework.text_editor import TextEditor
from framework.interface.concretas import WindowsInterfaceFactory, MacInterfaceFactory

def main():
    win = WindowsInterfaceFactory()
    mac = MacInterfaceFactory()

    # Singleton
    app1 = TextEditor(win)
    app2 = TextEditor(win)
    print("Singleton:", app1 is app2)  # True

    # Se tentar trocar UI depois: deve falhar (aceite do RF-05)
    try:
        TextEditor(mac)
    except ValueError as e:
        print("Troca de UI bloqueada:", e)

    # Abstract Factory (na prática, a UI é definida na primeira criação)
    app1.show_ui()

    # Multiton (Document)
    d1 = app1.new_document("notes")
    d2 = app1.new_document("notes")
    print("Multiton doc:", d1 is d2)  # True

    # Save/Revert (Memento)
    d1.write("A")
    d1.save()
    d1.write("B")
    d1.revert()
    print("Depois do revert:", d1.read())  # A

if __name__ == "__main__":
    main()
