class Animal:
    species = "mammals"

    def __init__(self, name):
        self.name = name
    
    def hello(self):
        print(f"Hello, my name is {self.name} and I am a {self.species}.")

    def change_species(cls, new_species):
        cls.species = new_species

cat = Animal("Whiskers")
cat.hello()
cat.change_species("feline")
cat.hello()
