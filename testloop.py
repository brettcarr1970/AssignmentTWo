import random


class mass:

    def __init__(self):
        visited =[False, False, True, False]
        while not all(visited):
            i = random.randint(0, 3)
            visited[i] = True
            print(i)
        print(visited)
c = mass()
c
