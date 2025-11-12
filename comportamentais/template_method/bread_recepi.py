from abc import ABC, abstractmethod

class BreadRecipe(ABC):
    def makeBread(self) -> None:
        self.prepareDough()
        self.bake()
        if self.doSlice():
            self.slice()

    def prepareDough(self) -> None:
        print(f"[1/3] Preparando massa ({self.getSize()}, grão: {self.getGrainType()}, forma: {self.getForm()})...")

    def bake(self) -> None:
        print("[2/3] Assando...")

    def slice(self) -> None:
        print("[3/3] Fatiando...")

    @abstractmethod
    def getSize(self) -> str: ...
    @abstractmethod
    def getGrainType(self) -> str: ...
    @abstractmethod
    def getForm(self) -> str: ...
    @abstractmethod
    def doSlice(self) -> bool: ...

class ItalianBreadRecipe(BreadRecipe):
    def getSize(self) -> str:
        return "grande"
    def getGrainType(self) -> str:
        return "trigo duro (sêmola)"
    def getForm(self) -> str:
        return "redondo (casca grossa)"
    def doSlice(self) -> bool:
        return False  

class SandwichBreadRecipe(BreadRecipe):  
    def getSize(self) -> str:
        return "médio"
    def getGrainType(self) -> str:
        return "trigo"
    def getForm(self) -> str:
        return "retangular (forma)"
    def doSlice(self) -> bool:
        return True   

if __name__ == "__main__":
    print("== Pão Italiano ==")
    BreadRecipeType = ItalianBreadRecipe()
    BreadRecipeType.makeBread()

    print("== Pão de Forma ==")
    BreadRecipeType = SandwichBreadRecipe()
    BreadRecipeType.makeBread()
