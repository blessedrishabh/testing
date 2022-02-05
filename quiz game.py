import requests as req
import json
import pprint
import random
import html

score_correct = 0
score_incorrect = 0

url = "https://opentdb.com/api.php?amount=1&category=21&difficulty=medium&type=multiple"
endgame = ""
while endgame != "quit":
    r = req.get(url)
    if(r.status_code != 200):
        endgame = input('Sorry! There is some problem in retriving the data')
    else:
        answer_number = 1
        data = json.loads(r.text)
        question = data['results'][0]['question']
        answers = data['results'][0]['incorrect_answers']
        correct_answers = data['results'][0]['correct_answer']
        answers.append(correct_answers)
        random.shuffle(answers)

        print(html.unescape(question) + '\n')
        for answer in answers:
            print(str(answer_number)+":  " + html.unescape(answer))
            answer_number = answer_number + 1
        user_answer = input("\n your answer: ")
        user_answer = answers[int(user_answer) - 1]
        if user_answer == correct_answers:
            print('\ncongratulation! you answered coorectly')
            score_correct += 1
        else:
            print('\nincorrect answer')
            score_incorrect += 1
       
        endgame = input('Do you wanna play again press "enter" or press "quit" to quit the game')
print('you answered '+str(score_correct)+' correctly')
print('you answered '+str(score_incorrect)+' incorrectly')
