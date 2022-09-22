#if a word starts with a consonant move 
# the first letter(s) of the word, till 
# you reach a vowel, to the end of the word
# and add "ay" to the end.
# have -> avehay, cram -> amcray...
#if a word starts with a vowel add "yay"
# to the end of the word. 
# ate-> ateyay, apple-> appleyay...

vowels = 'aeuio'

a = str(input())
b = list(a)

def find_index(a):
    cnt = 0
    for i in a:
        if i in vowels:
            return cnt
        cnt += 1

index = find_index(a)
