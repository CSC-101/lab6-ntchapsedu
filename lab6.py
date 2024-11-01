import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1
#input is a list of books
#output is a list of books in title alphabetical order
#for each book compare it to the book to the left of it and if it's title is before then swap
#continue swapping until it's not less than the next title to the left
def selection_sort_books(books: list[data.Book])->list[data.Book]:
    for i in range(len(books)):
        temp = books[i]
        j = i-1
        while j>=0 and temp.title < books[j].title:
            books[j+1] = books[j]
            j -= 1
        books[j+1] = temp
    return books
# Part 2
#input a word in string form
#output a string with flipped case
#for each character check if it is upper or lowercase, if it has case set that letter for the opposite of whatever it is
#append each character to a new list, then return that list as joined with no spaces inbetween the join
def swap_case(word: str)->str:
    temp = list(word)
    new = []
    for i in temp:
        if i.islower():
            i = i.upper()
        elif i.isupper():
            i = i.lower()
        new.append(i)
    return ''.join(new)
# Part 3
#input is a str, a character, and another character
#output is the original string but with the input character swapped to the second input character
#for each character in the sentence if that character is the same as the input character swap it to the second character
#add that character, swapped or not, to a new list
#join that list with no space in between and return it
def str_translate(sentence: str,word1: str,word2:str)->str:
    temp = list(sentence)
    new = []
    for i in temp:
        if i == word1:
            i = word2
        new.append(i)
    return ''.join(new)

# Part 4
#input is a string with multiple words
#output is a dictionary with words and how many of that word appear in the input string
#for each word check against each word and if they are the same word add to a counter
#then add to a dictionary the word and the count of the counter
def histogram(sentence:str)->dict:
    splitup = sentence.split()
    dictionary = {}
    for i in splitup:
        temp = 0
        for j in splitup:
            if i == j:
                temp += 1
        dictionary[i] = temp
    return dictionary