word = input("Enter a word: ")

for letter in word:
    print(letter)

print("Numbered letters:")
number = 1
for letter in word:
    print(f"{number}. {letter}")
    number += 1

print(f"The word has {len(word)} letters.")
