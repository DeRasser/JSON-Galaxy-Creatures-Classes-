import json

class Galaxy:
    def __init__(self, name, species):
        self.name = name
        self.species = [Species(**s) for s in species]

class Species:
    def __init__(self, name, avg_lifetime, creatures):
        self.name = name
        self.avg_lifetime = avg_lifetime
        self.creatures = [Creature(**c) for c in creatures]

    def find_by_status(self, status):
        return [c for c in self.creatures if c.status == status]

class Creature:
    def __init__(self, id, name, age, status):
        self.id = id
        self.name = name
        self.age = age
        self.status = status

    def is_healthy(self):
        return self.status == "healthy"

    def to_human_ages(self):
        return f"{self.age / 10} human years old"

class Light:
    def __init__(self, galaxies):
        self.galaxies = [Galaxy(**g) for g in galaxies]

    def find_all_by_status(self, status):
        result = []
        for g in self.galaxies:
            for sp in g.species:
                for c in sp.find_by_status(status):
                    result.append((c, sp.name, g.name))
        return result

print("Hello! This program will separate weak and healthy creatures in all galaxies that exist")
with open("galaxy.json", "r") as f:
    data = json.load(f)

light = Light(data["galaxies"])
st = input("Enter the status you want to find creatures by(weak or healthy): ")
st = st.lower()

sprt_crt = light.find_all_by_status(st)
for i in range(len(sprt_crt)):
    print(f"Creature {i+1} found! Creature '{sprt_crt[i][0].name}' by id:{sprt_crt[i][0].id} that refers to '{sprt_crt[i][1]}' species is {sprt_crt[i][0].age} years old ({sprt_crt[i][0].to_human_ages()}). Its status: {sprt_crt[i][0].status}\nIt is situated in Galaxy '{sprt_crt[i][2]}'.")

