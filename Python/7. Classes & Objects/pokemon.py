# Write code below 💖

# Define your class
class Pokemon:
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught

    def speak(self):
        print(self.name * 2)

    def display_details(self):
        print(f"Entry Number: {self.entry}")
        print(f"Name: {self.name}")
        print(f"Type: {', '.join(self.types)}")
        print(f"Description: {self.description}")
        if self.is_caught:
            print(f"{self.name} has already been caught!")
        else:
            print(f"{self.name} has not been caught yet.")

charmander = Pokemon(4, "Charmander", ["Fire"], "The flame on its tail...", False)
pikachu = Pokemon(25, "Pikachu", ["Electric"], "It has small electric sacs...", True)
bulbasaur = Pokemon(1, "Bulbasaur", ["Grass"], "For some time after its birth...", False)

charmander.speak()
pikachu.display_details()
bulbasaur.display_details()