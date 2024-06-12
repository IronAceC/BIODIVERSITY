#Biodiversity Project
#Aiden Krahn
#April 18th, 2024

import random
#how this works:
#the environment will have a random amount of food, water, and environmental danger
#animals will have hunger stats, cannibals, herbivores, or omnivores, defenses,

class Organism:
    def __init__(self,name):
        self.name = name
        self.female_population = random.randint(1,10)
        self.male_population = random.randint(1,10)
        self.males = []
        self.females = []
        for x in range(0, self.male_population):
            x = gene_maker()
            self.males.append(x)
            
        for x in range(0, self.female_population):
            x = gene_maker()
            self.females.append(x)
        self.population = (len(self.males) + len(self.females))
        self.gave_birth = []
        self.birthed = []
        
    def generation(self):
        self.make_baby()
        for x in range(0, len(self.males)):
            if "m" in self.males[x]:
                kenny = random.randint(1,12)
                
            else:
                kenny = random.randint(1,20)
                
            if kenny == 1:
                self.males.pop(x)
                print("A male has died")
                x -= 1
            
        for x in range(0,len(self.females)):
            if "m" in self.females[x]:
                kenny = random.randint(1,12)
                
            else:
                kenny = random.randint(1,20)
                
            if kenny == 1:
                self.females.pop(x)
                print("A female has died")
                x -= 1
        
    def make_baby(self):
        while len(self.males) > 0 and len(self.females) > 0:
            random.shuffle(self.males)
            random.shuffle(self.females)
            father = self.males[0]
            mother = self.females[0]
            self.gave_birth.append(self.females.pop(0))
            baby = []
            for x in range(0,len(father)):
                kenny = random.randint(1,2)
                if kenny == 1:
                    baby.append(father[x])
                    
                elif kenny == 2:
                    baby.append(mother[x])
                    
            if father[0] == mother[0] or father[1] == mother[1] or father[2] == mother[2] or father[3] == mother[3]:
                baby.append('m')
            
        for x in range(0, len(self.birthed)):#gender reveal party
            kenny = random.randint(1,2)
            if kenny == 1:
                self.males.append(self.birthed.pop(0))
                print("A baby dude has been born")
                
            else:
                self.females.append(self.birthed.pop(0))
                print("A baby dudette has been born")
                
        for x in range(0,len(self.gave_birth)):
            self.females.append(self.gave_birth.pop(0))
        

def simulate_population_growth(organism, initial_population, generations):
    population = initial_population
    print(f"Initial population of {organism.name}: {population}")

    for generation in range(1, generations + 1):
        births = 0
        deaths = 0

        for _ in range(population):
            if random.random() < organism.birth_rate:
                births += 1
            if random.random() < organism.death_rate:
                deaths += 1
        
        population += births - deaths
        print(f"Generation {generation}: Population = {population} (+{births}, -{deaths})")
        
#the next 27 lines are dedicated to naming random animals based on vowels, consonants, and syllables. 
def generate_syllable():
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    syllable = random.choice(consonants) + random.choice(vowels)
    return syllable

def generate_animal_name(syllable_count):
    name = ''.join([generate_syllable() for _ in range(syllable_count)])
    return name.capitalize()

def generate_random_animal_names(num_names, syllable_count):
    animal_names = [generate_animal_name(syllable_count) for _ in range(num_names)]
    return animal_names
    
def generate_syllable():
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    syllable = random.choice(consonants) + random.choice(vowels)
    return syllable

def generate_animal_name(syllable_count):
    name = ''.join([generate_syllable() for _ in range(syllable_count)])
    return name.capitalize()

def generate_random_animal_names(num_names, syllable_count):
    animal_names = [generate_animal_name(syllable_count) for _ in range(num_names)]
    return animal_names

def gene_maker():
    letters = "asdfghjkl"
    first = random.choice(letters)
    second = random.choice(letters)
    third = random.choice(letters)
    fourth = random.choice(letters)
    genes = [first, second, third, fourth]
    return genes

print("""Welcome to the Gene Emporium!
We've created a new creature with a new name, population, and genetics
As the test progresses, the species will make babies and die
If the genetics of the parents overlap, there will be mutations that cause more death
How long can a small population live before inbreeding kills them? Let's find out!""")
organisms = []
if __name__ == "__main__":
    # Define organism parameters (birth rate, death rate)
    syllable_count = random.randint(2,4)
    random_animal_names = generate_random_animal_names(1, syllable_count)
    for name in random_animal_names:
        organisms.append(name)
    print(organisms)
    play = True
    x = 0
    Animal = Organism(organisms[0]) 
    print(Animal.males)
    print(Animal.females)
    while play == True:
        Animal.generation()
        endorno = input("Type 'NO' to quit, else press ENTER")
        if endorno == "NO":
            play = False
            
        else:
            play = True
    