from lib.sentence2vec import Sentence2Vec


class QanatovSolver:
    def __init__(self, path='./data/Qanatov_solver.model'):
        self.model = Sentence2Vec(path)



    def get_similarity(self, question, choice):
        return self.model.similarity(question, choice)
