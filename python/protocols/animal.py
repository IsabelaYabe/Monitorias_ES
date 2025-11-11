from typing import Protocol
from abc import ABC, abstractmethod


class Walker(Protocol):
    def walk(self, distance: float) -> None:
        """Make the entity walk a certain distance."""
        ...

    def stop(self) -> None:
        """Make the entity stop moving."""
        ...

class Talker(Protocol):
    def speak(self, message: str) -> None:
        """Make the entity speak a message."""
        ...

    def listen(self) -> str:
        """Make the entity listen and return the heard message."""
        ...

class Swimmer(Protocol):
    def swim(self, distance: float) -> None:
        """Make the entity swim a certain distance."""
        ...

    def dive(self, depth: float) -> None:
        """Make the entity dive to a certain depth."""
        ...

class Animal(ABC):
    def __init__(self, phyla: str, species: str) -> None:
        self.phyla = phyla
        self.species = species

    @abstractmethod
    def info(self) -> str:
        """Return information about the animal."""
        pass
    
    @abstractmethod
    def habitat(self) -> str:
        """Return the habitat of the animal."""
        pass
    
class Mammal(Animal):
    def __init__(self, phyla, species, sound: str = "generic sound") -> None:
        super().__init__(phyla, species)
        self.sound = sound

    def info(self) -> str:
        return f"This is a {self.species} from the {self.phyla} phyla."

    def habitat(self):
        return "Various habitats including forests, grasslands, and urban areas."
    
    def walk(self, distance: float) -> None:
        print(f"The {self.species} walks {distance} meters.")

    def stop(self) -> None:
        print(f"The {self.species} stops walking.")

    def speak(self, message: str) -> None:
        print(f"The {self.species} says: {message}")
        print(f"It usually makes a sound like: {self.sound}")

    def listen(self) -> str:
        return f"The {self.species} is listening."  
    
class Fish(Animal):
    def __init__(self, phyla, species, color: str) -> None:
        super().__init__(phyla, species)
        self.color = color

    def info(self) -> str:
        return f"This is a {self.species} from the {self.phyla} phyla."

    def habitat(self):
        return "Aquatic environments including freshwater and marine habitats."
    
    def swim(self, distance: float) -> None:
        print(f"The {self.species} swims {distance} meters.")

    def dive(self, depth: float) -> None:
        print(f"The {self.species} dives to a depth of {depth} meters.")
    
    def coloration(self) -> str:
        return f"The {self.species} has a beautiful {self.color} coloration."

def main() -> None:
    elephant = Mammal(phyla="Chordata", species="Elephant", sound="trumpet")
    print(elephant.info())
    print(elephant.habitat())
    elephant.walk(100)
    elephant.speak("Hello there!")
    print(elephant.listen())
    elephant.stop()

    salmon = Fish(phyla="Chordata", species="Salmon")
    print(salmon.info())
    print(salmon.habitat())
    salmon.swim(200)
    salmon.dive(30)

if __name__ == "__main__":
    main()