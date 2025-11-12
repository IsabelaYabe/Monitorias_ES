from abc import ABC, abstractmethod
from typing import Optional

from editor_service import EditorService

class Command(ABC):
    @abstractmethod
    def execute(self) -> None: ...

class OpenCommand(Command):
    def __init__(self, svc: EditorService, path: str) -> None:
        self.svc = svc
        self.path = path        

    def execute(self) -> None:
        self.svc.open(self.path)

class SaveCommand(Command):
    def __init__(self, svc: EditorService, path: str) -> None:
        self.svc = svc
        self.path = path

    def execute(self) -> None:
        self.svc.save(self.path)

class PrintCommand(Command):
    def __init__(self, svc: EditorService) -> None:
        self.svc = svc

    def execute(self) -> None:
        self.svc.print_doc()

# ---- Invokers (UI) ----
class Button:
    def __init__(self, label: str) -> None:
        self.label = label
        self._command: Optional[Command] = None

    def bind(self, command: Command) -> None:
        self._command = command

    def click(self) -> None:
        if self._command:
            self._command.execute()

class Shortcut:
    def __init__(self, keys: str, command: Command) -> None:
        self.keys = keys
        self.command = command

    def press(self) -> None:
        self.command.execute()

if __name__ == "__main__":
    svc = EditorService()

    btn_open = Button("Abrir")
    btn_save = Button("Salvar")
    btn_print = Button("Imprimir")

    btn_open.bind(OpenCommand(svc, "dados.csv"))
    btn_save.bind(SaveCommand(svc, "relatorio.txt"))
    btn_print.bind(PrintCommand(svc))

    btn_open.click()
    btn_save.click()
    btn_print.click()

    btn_open.bind(OpenCommand(svc, "dados.json"))
    btn_open.click()

    ctrl_s = Shortcut("Ctrl+S", SaveCommand(svc, "relatorio.txt"))
    ctrl_s.press()
