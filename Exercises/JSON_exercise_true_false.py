import json
import requests
import pprint 
import html
url = "https://opentdb.com/api.php?amount=1&category=12&difficulty=easy&type=boolean"

endGame = ""
c_answers = 0
w_answers = 0

while endGame != "quit":
    r = requests.get(url)
    
    question_txt = json.loads(r.text)
    pprint.pprint(question_txt)

    question = (question_txt['results'][0]['question'])
    answer1 = (question_txt['results'][0]['incorrect_answers'])
    answer2 = (question_txt['results'][0]['correct_answer'])
    
    print(html.unescape(question + "\n"))
    
    x = input("Type your answer: true or false: ", )
    
    if  x.lower() == answer2.lower():
        print("Nice, Your're right ")
        c_answers += 1
    if x.lower() != answer2.lower():
        print("Sorry, wrong answer")
        w_answers += 1
    endGame = (input("Do you want to play again? Type 'quit' to exit, or press enter to play again: "))
        


