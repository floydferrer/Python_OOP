from random import randint
import linecache

class SerialGenerator:
    def __init__(self, start):
        self.start = start
        self.counter = start
    
    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.start + 1}>"

    def generate(self):
        self.counter += 1
        return self.counter

    def reset(self):
        self.counter = self.start


class WordFinder:
    def __init__(self, file):
        self.file = file
        counter = 0
        self.f = open(self.file)
        for line in self.f:
            counter += 1
        print(f'{counter} words read')
        self.f.seek(0)
    
    def random(self):
        self.f.seek(0)
        line = linecache.getline(self.file, randint(1, len(self.f.readlines())))
        return line.strip()

class SpecialWordFinder(WordFinder):
    def __init__(self, file):
        super().__init__(file)

    def random(self):
        self.f.seek(0)
        line = linecache.getline(self.file, randint(1, len(self.f.readlines())))
        while line.strip() == '' or '#' in line:
            self.f.seek(0)
            line = linecache.getline(self.file, randint(1, len(self.f.readlines())))
        return line.strip()