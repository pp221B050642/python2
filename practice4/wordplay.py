class Wordplay:
    def __init__(self, words):
        self.words = words
    def words_with_length(self, length):
        valid_words = []
        for i in self.words:
            if len(i)==length:
                valid_words.append(i)
        return valid_words
    def starts_with(self, s):
        valid_words = []
        for i in self.words:
            if i[0]==s:
                valid_words.append(i)
        return valid_words
    def ends_with(self, s):
        valid_words = []
        for i in self.words:
            if i[-1]==s:
                valid_words.append(i)
        return valid_words
    def palindromes(self):
        valid_words = []
        for i in self.words:
            if i == i[::-1]:
                valid_words.append(i)
        return valid_words
    def only(self, L):
        valid_words = []
        for i in self.words:
            answer = True
            for j in L:
                if j not in i:
                    answer = False
            if answer == True:
                valid_words.append(i)
        return valid_words
    def avoids(self, L):
        valid_words = []
        for i in self.words:
            answer = True
            for j in L:
                if j in i:
                    answer = False
            if answer == True:
                valid_words.append(i)
        return valid_words

w = ['game', 'huppuh', 'hope', 'hunter', 'sink', 'talk', 'shine', 'lime', 'gun', 'type']

play = Wordplay(w)
n = int(input())
print(play.words_with_length(n))
s1 = input()
print(play.starts_with(s1))
s2 = input()
print(play.ends_with(s2))
print(play.palindromes())
l1 = 'gn'
print(play.only(l1))
l2 = 'amgsinkl'
print(play.avoids(l2))














