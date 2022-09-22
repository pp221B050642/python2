#function that returns a determinant of a given matrix

a = str(input())
a1 = list(a.split())
b = str(input())
b1 = list(b.split())
c = str(input())
c1 = list(c.split())

def det(a1, b1, c1):
    coset1 = int(a1[0]) *(int(b1[1])*int(c1[2])-int(b1[2])*int(c1[1]))
    coset2 = int(b1[0]) *(int(a1[1])*int(c1[2])-int(a1[2])*int(c1[1]))
    coset3 = int(c1[0]) *(int(a1[1])*int(b1[2])-int(a1[2])*int(b1[1]))
    answer = coset1-coset2+coset3
    print(answer)

det(a1, b1, c1)

