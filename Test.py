import random

words = ["Bulle", "Saft", "Kaka", "Läsk", "Isglass"]
dict = {}

for i in range(300):

    random_word = random.choice(words) # hovra på .choice och se vad den gör
    
    if random_word in dict:
        dict[random_word] += 1
    else:
        dict[random_word] = 1

print(dict)
print(f"\"Bulle\" förekommer {dict["Bulle"]} gånger.")




