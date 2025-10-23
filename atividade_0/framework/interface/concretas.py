from interface_factory import InterfaceFactory
from window_cursor import Window, Cursor

class WindowsWindow(Window):
    def draw(self):
        print("Janela estilo Windows desenhada.")

class WindowsCursor(Cursor):
    def move(self):
        print("Cursor padrão Windows movido.")

class WindowsInterface(InterfaceFactory):
    def create_window(self):
        return WindowsWindow()
    def create_cursor(self):
        return WindowsCursor()
