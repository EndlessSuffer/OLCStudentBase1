'''
Task 4 - 2023 Paper - Development of Program
Open the file SPLIT_SENTENCE.py. You will see the following function that 
takes a string of words, passed as the parameter word_string, splits it 
into individual words and stores these words in a list. 
It returns the list of words. 

You can assume the string does not contain punctuation marks.
'''
def split_sentence(word_string):
    list_sentence = word_string.split(" ")
    return list_sentence
print(split_sentence("pine on pizza"))

#Task 4.1
def check_list(word,sentence):
    checked=False
    list_sentence= split_sentence(sentence.lower())

    # if word in list_sentence:
    for i in list_sentence:
        if i == word.lower():
            checked =True
    if checked==True:
        return "Yes"
    else:
        return "No"
#print(check_list("apple","The tree holds an "))

#Task 4.2
def reverse_sentence(sentence):
    list_sentence=split_sentence(sentence)
    completed=""
    for i in list_sentence:
        completed= i +" "+completed
    return completed
#print(reverse_sentence("apple is healthy for people"))

#Task 4.3
sentence=input("Type the sentence you want: ")
word=input("Type the word you want to search: ")
def functions(word,sentence):
    print(split_sentence(sentence))
    print(reverse_sentence(sentence))
    if check_list(word,sentence) == "Yes":
        print(f"The {word} is found.")
    else:
        print(f"The {word} is not found.")
functions(word,sentence)