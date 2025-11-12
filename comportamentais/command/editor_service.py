class EditorService:
    def open(self, path: str) -> None:
        print(f"Abrindo {path}...")

    def save(self, path: str) -> None:
        print(f"Salvando em {path}...")

    def print_doc(self) -> None:
        print("Imprimindo documento atual...")