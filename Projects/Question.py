# here, we define the question class. it contains the question prompt and the answer

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer