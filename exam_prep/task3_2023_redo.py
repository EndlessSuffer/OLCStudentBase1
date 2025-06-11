#Answer for debugging

import random
questions = 10
answer_list = []
correct = 0
incorrect = 0
total_mark = 0
for x in range(questions): #unnecessary -1
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    print("What is", num1, "+", num2, "?")
    user_answer = int(input())    #missing integer
    answer=num1 +num2 #missing variable answer
    if user_answer == answer:
        if num1 > 25 and num2 > 25:   # and function
            total_mark = total_mark + 2
        else:
            total_mark = total_mark + 1
        answer_list = answer_list + ["Correct"]     #wrong positioning and wrong quotation
    else:
        answer_list = answer_list + ["Incorrect"]
list_length = len(answer_list)  #unnecessary -1 and wrong minus sign
for i in range(list_length):
    if answer_list[i] == "Correct":   #wrong variable x the variable is i
        correct = correct + 1        # add 1 not minus 1
if correct  == 1:     #correct no message
    message = "answer."
else:
    message = "answers."
print("Your total mark is", total_mark, "and you had", correct, message)