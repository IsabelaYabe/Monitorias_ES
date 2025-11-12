import json
from dataclasses import dataclass

from game import factory, loader

@dataclass
class Sorcerer:
    name: str

    def make_a_noise(self) -> None:
         print("Aaaaargh!")

@dataclass
class Wizard:
    name: str

    def make_a_noise(self) -> None:
         print("Boohh!")

@dataclass
class Witcher:
    name: str

    def make_a_noise(self) -> None:
         print("Hmmm...")
    

def main() -> None:
    import os

    # register a couple of character types
    factory.register("sorcerer", Sorcerer)
    factory.register("wizard", Wizard)
    factory.register("witcher", Witcher)

    path = os.path.join("plugin", "level.json")
    with open(path) as file:    
        data = json.load(file)

        # load the plugins
        loader.load_plugins(data["plugins"])

        # create the characters
        characters = [factory.create(item) for item in data["characters"]]
        
        for character in characters:
            print(character, end="\t")
            character.make_a_noise()

if __name__ == "__main__":
    main()