import random

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

if __name__ == "__main__":
    num_names = 5
    syllable_count = 2
    random_animal_names = generate_random_animal_names(num_names, syllable_count)
    print("Random Animal Names:")
    for name in random_animal_names:
        print(name)