# a simple code that asks multichoice questions and returns the users score at the end
from Question import Question
question_prompts = [
    "Who killed Joel?\n(a)Owen\n(b)Mel\n(c)Abby\n(d)Tommy\n",
    "Who went with Ellie to get revenge?\n(a)Jesse\n(b)Dina\n(c)Tommy\n(d)Maria\n",
    "Who is the leader of the WLF?\n(a)Isaiah\n(b)Seth\n(c)David\n(d)Danny\n\n"
]

questions = [
    Question(question_prompts[0], 'c'),
    Question(question_prompts[1], 'b'),
    Question(question_prompts[2], 'a'),
]

def start_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print('Your score is ' + str(score) + '/' + str(len(questions)))

start_test(questions)