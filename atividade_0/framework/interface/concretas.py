from .interface_factory import InterfaceFactory
from .window_cursor import Window, Cursor

class WindowsWindow(Window):
    def create_window(self):
        print("Windows window created")
class WindowsCursor(Cursor):
    def create_cursor(self):
        print("Windows cursor created")

class WindowsInterface(InterfaceFactory):
    def create_window(self):
        return WindowsWindow()
    def create_cursor(self):
        return WindowsCursor()


class MacWindow(Window):
    def create_window(self):
        print("Mac window created")
class MacCursor(Cursor):
    def create_cursor(self):
        print("Mac cursor created")

class MacInterface(InterfaceFactory):
    def create_window(self):
        return MacWindow()
    def create_cursor(self):
        return MacCursor()