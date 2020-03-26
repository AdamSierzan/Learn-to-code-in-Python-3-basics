import pprint
import json
import requests
import html
import random


url = ("https://opentdb.com/api.php?amount=1&category=15&difficulty=easy&type=multiple")

endGame  = ""

score_correct = 0
score_incorrect = 0
while endGame != "quit":
    r = requests.get(url)
    if (r.status_code != 200):
       endGame = input("Something's wrong with the connection, press enter to try again, or type quit to exit")
    else:
        valid_data = False

        answer_number  = 1

        question_txt = json.loads(r.text)
        pprint.pprint(question_txt)
    

        question = question_txt['results'][0]['question']
    
        correct_answer = question_txt['results'][0]['correct_answer']
        answers = question_txt['results'][0]['incorrect_answers']
        
        answers.append(correct_answer)
        random.shuffle(answers)
        
        print(html.unescape(question + "\n"))
        
        for answer in answers:
            print(str(answer_number) + ". " + html.unescape(answer))
            answer_number +=1
        
        while valid_data == False:
            user_answer = input("\nChoose the number of the right answer: ")
            try:
                user_answer = int(user_answer)
                if user_answer > len(answers) or user_answer <= 0:
                    print("Invalid answer")
                else:
                    valid_data = True
            except: 
                print("Use numbers only!")
        
        user_answer = answers[int(user_answer)-1]
 
        
        if user_answer == correct_answer:
            print("Nice you're right, man, the correct answer is: ", html.unescape(correct_answer) )
            score_correct =+ 1
        else:
            print("Sorry, you're wrong, the correct answet is: ",html.unescape(correct_answer) )
            score_incorrect += 1
        print("")
        print("#####################")
        print("Your score table: ")
        print("Correct answers:", score_correct)
        print("Incorrect answers: ", score_incorrect)
        print('#####################')
        print("")
        endGame = input(print("Do you want to play again? Type enter, to play again, or 'quit' to exit: "))
print("\n Thanks for playing, the number of correct answers is:", score_correct,"." "The number of incorrect answers is: ", score_incorrect)