# Parent Class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery = battery  # in %
    
    def make_call(self, contact):
        print(f"{self.brand} {self.model} is calling {contact}... 📞")
    
    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        print(f"Battery charged. Current battery: {self.battery}% 🔋")
    
    def install_app(self, app):
        print(f"Installing {app} on {self.brand} {self.model} 📲")

# Child Class (Inheritance)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system):
        super().__init__(brand, model, storage, battery)
        self.cooling_system = cooling_system
    
    def play_game(self, game):
        if self.battery > 10:
            print(f"Playing {game} on {self.model} 🎮 with {self.cooling_system} cooling.")
            self.battery -= 10
        else:
            print("Battery too low to play! ⚠️")

# Example Usage
phone1 = Smartphone("Samsung", "Galaxy S24", 256, 80)
phone1.make_call("Alice")
phone1.charge(15)
phone1.install_app("WhatsApp")

gaming_phone = GamingPhone("Asus", "ROG 7", 512, 60, "Liquid Cooling")
gaming_phone.play_game("PUBG")
gaming_phone.charge(30)

# Base Class
class Vehicle:
    def move(self):
        print("Vehicle is moving...")

# Subclasses
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Example Usage
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()  # Polymorphism: same method, different behavior
