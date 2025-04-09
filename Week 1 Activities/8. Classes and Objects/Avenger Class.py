class Avenger:
    def __init__(self, name, age, gender, super_power, weapon, is_leader=False):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon
        self.is_leader = is_leader

    def get_info(self):
        return f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nSuper Power: {self.super_power}\nWeapon: {self.weapon}"

    def is_leader(self):
        return self.leader_status

# Create instances of Avengers
super_heroes = [
    Avenger("Captain America", 100, "Male", "Super Strength", "Shield", is_leader=True),
    Avenger("Iron Man", 50, "Male", "Technology", "Armor"),
    Avenger("Black Widow", 35, "Female", "Superhuman", "Batons"),
    Avenger("Hulk", 50, "Male", "Unlimited Strength", "No Weapon"),
    Avenger("Thor", 1500, "Male", "Super Energy", "Mjölnir"),
    Avenger("Hawkeye", 45, "Male", "Fighting Skills", "Bow and Arrows")
]

# Display information about each superhero
for hero in super_heroes:
    print(hero.get_info())
    print(f"Is Leader: {hero.is_leader}")
    print("-" * 30)
