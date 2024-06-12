#Biodiversity Project
#Aiden Krahn
#April 18th, 2024

import random
from colorama import Fore #the color change doesn't work in the terminal :(
#how this works:
#

class Organism: #every time this runs, it will make a new creature with different attributes
    def __init__(self,name):
        self.name = str(name)#name randomly generated, show later
        self.female_population = random.randint(1,100)#number of males/females is random
        self.male_population = random.randint(1,100)
        self.males = [] #this list will contain separate lists that contain the dna of individuals
        self.females = []
        for x in range(0, self.male_population):
            x = gene_maker()#find gene maker function to see how we generated dna
            self.males.append(x)
            
        for x in range(0, self.female_population):
            x = gene_maker()
            self.females.append(x)
        self.population = (len(self.males) + len(self.females))#this is just so we can count total population
        self.gave_birth = [] #used later in makebaby
        self.birthed = [] #used later in makebaby
        self.mutated = [] #used later in makebaby
        self.dead = 0 #used to count how many died over many generations
        self.fecundity = 100 #I couldn't think of more relevant genetic traits than fecundity and survival
        self.survival = 100 #these are the rates in which babies are born / how well they can survive
        
    def generation(self):
        self.make_baby()#first thing they do is make babies
        y = 0
        tracking = [0,0,0,0,0,0] #tracks how many of which gene is there
        self.fecundity = 100
        self.survival = 100 #resets every generation so that it doesn't compound
        for x in range(0,len(self.males)): #only checks males because doing both would double this section of code. 
            if "a" in self.males[y]: #checks if it has the "a" gene
                if self.survival > 50: #if it's lower than 50, it's could cause random number to be out of range and ruin the code when things start dying
                    self.survival += 2 #increasing the rate of survival ensures the number is not below a certain threshold
                    tracking[0] += 1 #in other words, number big is good
                    print(tracking)
                
            if "s" in self.males[y]: #same process as "a"
                if self.survival > 50:
                    self.survival -= 2
                    tracking[1] += 1
                    print(tracking)
                
            if "d" in self.males[y]:
                if self.fecundity > 50:
                    self.fecundity += 2
                    tracking[2] += 1
                    print(tracking)
                
            if "f" in self.males[y]:
                if self.fecundity > 50:
                    self.fecundity -= 1
                    tracking[3] += 1
                    print(tracking)
                
            if "g" in self.males[y]:
                if self.fecundity > 50:
                    self.fecundity -= 1
                    tracking[4] += 1
                    print(tracking)
                    
            if "h" in self.males[y]:
                if self.fecundity > 50:
                    self.fecundity += 5
                    tracking[5] += 1
                    print(tracking)
            y += 1
                
        y = 0
        for x in range(0, len(self.males)):
            if "m" in self.males[y]: #if it has "m" gene, more likely to die
                kenny = random.randint(1,50)
                
            else:
                kenny = random.randint(1,self.survival) #otherwise, likelihood to die is based on genes
                
            if kenny <= 25:
                self.males.pop(y) #remove from list
                print("A male ",self.name," has died")
                self.dead += 1
            
            else:
                y += 1
            
        y = 0
        for x in range(0,len(self.females)): #same thing as males
            if "m" in self.females[y]:
                kenny = random.randint(1,50)
                
            else:
                kenny = random.randint(1,self.survival)
                
            if kenny <= 25:
                self.females.pop(y)
                print("A female ",self.name, " has died")
                self.dead += 1
                
            else:
                y += 1
                
        if len(self.males) > 100: #if there are too many in the population, random chance to wipe out large portions of population
            apocachance = random.randint(1,4)
            if apocachance == 1:
                self.apocalypse()
                
        print(f"Male Population of {self.name}: ",len(self.males)) #print how many males/females in terminal
        print(f"Female Population of {self.name}: ",len(self.females))
        for x in range(0, len(self.males)):
            if "m" in self.males[x]:
                self.mutated.append(self.males[x]) #count mutated population
                
        for x in range(0,len(self.females)):
            if "m" in self.females[x]:
                self.mutated.append(self.females[x])
                
        print(f"mutated Population of {self.name}: ",len(self.mutated))
        self.mutated = []#resets list
        print(f"Overall Population of {self.name}: ",(len(self.males) + len(self.females)))
        print(f"There are {self.dead} dead.")
        print(f"The genetic distribution is: {tracking}")
        print(f"Chance of survival: {self.survival}, Chance of making a new baby: {self.fecundity}")
        
                
        
    def make_baby(self):
        while len(self.males) > 0 and len(self.females) > 0:#while there are still men and women who can have babies
            random.shuffle(self.males)#shuffle the list
            random.shuffle(self.females)
            father = self.males[0]#take the first from the list
            mother = self.females[0]
            self.gave_birth.append(self.females.pop(0))#remove the mother from list so she can't have two babies
            maybebaby = random.randint(1,self.fecundity)#chance of having a baby
            if maybebaby >= 25:#if successful
                baby = []
                for x in range(0,4):
                    kenny = random.randint(1,2)#random
                    if kenny == 1:
                        baby.append(father[x])#passes genes to baby from father
                        
                    elif kenny == 2:
                        baby.append(mother[x])#or mother
                        
                if father[0] == mother[0] or father[1] == mother[1] or father[2] == mother[2] or father[3] == mother[3]:
                    baby.append('m') #if father and mother share genetics, baby will be mutated
                    
                self.birthed.append(baby) #add baby to list to be added to population later
                
            for x in range(0, len(self.birthed)):#gender reveal party
                kenny = random.randint(1,2)
                if kenny == 1:
                    self.males.append(self.birthed.pop(0))#remove baby from birthed list, add to male list
                    print(f"A male {self.name} has been born")
                    
                else:
                    self.females.append(self.birthed.pop(0))#same thing but add to female list
                    print(f"A female {self.name} has been born")
                
        for x in range(0,len(self.gave_birth)):
            self.females.append(self.gave_birth.pop(0))
            
    def apocalypse(self):
        print(f"""{Fore.RED}AN APOCALYPSE IS OCCURING!!{Fore.BLACK}-----------------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------""")
        y = 0#I added a lot of hyphens so that it would be easy to see when it happened while text was scrolling past
        for x in range(0, round((len(self.males)/4)*3)): #removes 6 / 7 of the population
            self.males.pop(0)
            print("A male ",self.name," has died")
            self.dead += 1
            
        y = 0
        for x in range(0,round((len(self.females)/4)*3)):
            self.females.pop(0)
            print("A female ",self.name, " has died")
            self.dead += 1
            
        

#the next 13 lines are dedicated to naming random animals based on vowels, consonants, and syllables. 
def generate_syllable():
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    syllable = random.choice(consonants) + random.choice(vowels) #takes a vowel and a consonant, slaps them together
    return syllable

def generate_animal_name(syllable_count): #for the number of syllables, adds syllables together
    name = ''.join([generate_syllable() for _ in range(syllable_count)])
    return name.capitalize()

def generate_random_animal_names(num_names, syllable_count): #if you had multiple animal names, this is how you would separate them
    animal_names = [generate_animal_name(syllable_count) for _ in range(num_names)]
    return animal_names
    

def gene_maker():
    letters = "asdfghmpppp" #from list of letters...
    first = random.choice(letters)#take a random one
    second = random.choice(letters)
    third = random.choice(letters)
    fourth = random.choice(letters)
    genes = [first, second, third, fourth] #add to list of genes
    return genes

print("""Welcome to the Genetics Simulator!
We've created a new creature with a new name, population, and genetics
As the test progresses, the species will make babies and die
If the genetics of the parents overlap, there will be mutations that cause more death
How long can a small population live before the species fails? Let's find out!""")
organisms = []
if __name__ == "__main__":
    syllable_count = random.randint(2,4) #random number of syllables for name
    random_animal_names = generate_random_animal_names(2, syllable_count) #make a random name
    for name in random_animal_names:
        organisms.append(name)#list of organism names
    print(organisms)
    play = True
    generations = 0 #count number of generations have passed
    Herbivore = Organism(organisms[0]) #define the creature with the variable name
    #Carnivore = Organism(organisms[0])  I planned to have two different creatures living together simultaneously, but one was enough
    #print(Herbivore.males)
    #print(Herbivore.females)
    while play == True: #run simulation until NO or extinction
        Herbivore.generation() #runs the generation
        generations += 1 #count the generations
        print(f"There have been {generations} generations")
        endorno = input("Type 'NO' to quit, else press ENTER")
        if endorno == "NO": # if you type NO, it ends
            play = False
            
        else: #anything else will continue simulation
            play = True
            
        if (len(Herbivore.males) + len(Herbivore.females)) == 0: #if there are none left, stop simulation and jump to end
            print("EXTINCT")
            play = False
    
print("You are done playing")