#Answer for debugging

import random
questions = 10 
answer_list = []
correct = 0
incorrect = 0
total_mark = 0
for x in range(questions): #11. Should not minus 1 from questions
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    answer=num1 +num2 #3. Missing variable
    print("What is", num1, "+", num2, "?")
    user_answer = int(input())#7.input must convert to integer
    if user_answer == answer: 
        if num1 > 25 and num2 > 25: #9. should be and condition
            total_mark = total_mark + 2
        else:
            total_mark = total_mark + 1
        answer_list = answer_list + ["Correct"] #1.Fixed wrong quotation, 8.wrong placement out of if position
    else:
        answer_list = answer_list + ["Incorrect"]
list_length = len(answer_list) #-1 #2.FIxed wrong minus sign,#4 fixed answer list
for i in range(list_length):
    if answer_list[i] == "Correct":  #10. variable should be i not x
        correct = correct + 1 # 6. not addi ng properly
if correct  == 1:  #5.message variable is wrong replaced with correct
    message = "answer."
else:
    message = "answers."
print("Your total mark is", total_mark, "and you had", correct, message)