#wordplay
#cannot do all vowels
import re

end_ime = r'(\w*ime\b)'
ave234 = r'(\b.ave\w*)'
letters_rstlne = r'\w*[rstlne]+\w*'
no_vowels = r'\b([^aeiou\s]+)\b'
all_vowels = r''

with open("wordlist.txt", "r+") as myfile:
    wl = myfile.read()
    cnt=0
    with_all_vowels = []
    for word in wl:
        cnt+=1
        if re.search(r'a+', word) and re.search(r'e+', word) and re.search(r'i+', word) and re.search(r'o+', word) and re.search(r'u+', word):
            with_all_vowels.append(word)
    ime = re.findall(end_ime, wl)
    ave = re.findall(ave234, wl)
    rstlne = re.findall(letters_rstlne, wl)
    without_vowels = re.findall(no_vowels, wl)
    percentage = len(rstlne)/cnt*100
    print(f"words which ends with ime: {ime}")
    print(f"words whose second, third, and fourth letters are ave: {ave}")
    print(len(rstlne))
    print(f"{percentage:.2f}%")
    print(f"words with no vowels: {without_vowels}")
    print(f"words contain all vowels: {with_all_vowels}")


