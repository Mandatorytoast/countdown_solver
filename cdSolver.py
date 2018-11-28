from itertools import chain, combinations, permutations
import sys


file = open('wordlist.txt', 'r') #opens a list of english words
word_list = list(file) #saves each word into a list 

correct_words = [] #empty list to be filled with all the words that match 
letters = list(sys.argv[1]) #user inputs a string of characters

def powerset(iterable): #returns a powerset of the letters
    s = list(iterable)
    return list(map("".join, chain.from_iterable(combinations(s,r) for r in range(len(s) + 1))))

all_combinations = [] 

for i in powerset(letters): #uses the powerset to create a list of all the perumutations of the letters and adds them to the all_combinations list
    for variation in (list(map("".join, permutations(i)))):
        all_combinations.append(f'{variation}\n')

for i in list(set(word_list) & set(all_combinations)): #compares all the permutations with the word list and adds the matches to correct_words
    correct_words.append(i[:-1])

correct_words.sort(key=len, reverse=True) #sorts the correct words by length from highest to lowest

for i in correct_words: #prints all the correct words
    print(f'{len(i)}:{i}')

