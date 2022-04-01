import pickle

class Actions:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def summ(self, a, b):
        print(a+b)

test_object = Actions(1, 2)

with open('file2', 'wb') as f:
    pickle.dump(test_object, f)

with open('file2', 'rb') as f:
    loaded = pickle.load(f)

loaded.summ(12, 8)
