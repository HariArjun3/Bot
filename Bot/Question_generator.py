def question_generator(self, skills):
    self.questions = [question_generation(skill) for skill in skills]
    que = []
    for i in range(len(self.questions)):
        que.append(self.questions[i])
    return que