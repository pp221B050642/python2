from tkinter import *
import math

calculator = Tk()
calculator.title("Scientific Calculator")
calculator.geometry("360x280")

display = StringVar() 
operator = ''

txtDisplay = Entry(calculator, font=('Helvetica',20),bg='grey',fg='white', textvariable=display, bd = 20,width=21,justify=RIGHT)
txtDisplay.grid()
txtDisplay.insert(0,"0")

f = Frame(calculator)
f.grid()
f2 = Frame(calculator)
f2.grid()

#calculations
def enter(n):
    global operator
    operator += str(n)
    display.set(operator)
def clear_all():
    global operator
    operator = ''
    display.set('0')
def clear():
    global operator
    noperator = operator[:-1]
    operator = noperator
    display.set(operator)
def sign_change():
    global operator
    if operator[0]=='-':
        answer = operator[1:]
    else:
        answer = '-'+operator
    operator = answer
    display.set(answer)
def factorial():
    global operator
    answer = str(math.factorial(int(operator)))
    operator = answer
    display.set(answer)
def equal():
    global operator
    answer = str(eval(operator))
    operator = answer
    display.set(answer)
def percent():
    global operator
    answer = str(eval(operator+'/100'))
    operator = answer
    display.set(answer)
def sin_func():
    global operator
    answer = str(math.sin((float(operator))))
    operator = answer
    display.set(answer)
def cos_func():
    global operator
    answer = str(math.cos((float(operator))))
    operator = answer
    display.set(answer)
def tan_func():
    global operator
    answer = str(math.tan((float(operator))))
    operator = answer
    display.set(answer)
def square():
    global operator
    answer = str(eval(operator+'**2')) 
    operator = answer
    display.set(answer)
def squareroot():
    global operator
    answer = str(eval(operator+'**(1/2)')) 
    operator = answer
    display.set(answer)
def eexp():
    global operator
    answer = str(math.e**int(operator))
    operator = answer
    display.set(answer)
def sinh_func():
    global operator
    answer = str(math.sinh((float(operator))))
    operator = answer
    display.set(answer)
def cosh_func():
    global operator
    answer = str(math.cosh((float(operator))))
    operator = answer
    display.set(answer)
def tanh_func():
    global operator
    answer = str(math.tanh((float(operator))))
    operator = answer
    display.set(answer)
def naturallog():
    global operator
    answer = str(math.log(int(operator)))
    operator = answer
    display.set(answer)
def logarithm10():
    global operator
    answer = str(math.log(int(operator), 10))
    operator = answer
    display.set(answer)
def radians():
    global operator
    answer = str(math.radians(float(operator)))
    operator = answer
    display.set(answer)


#buttons
adding = Button(f,width = 5, height = 2, text = '+', bg = 'orange', foreground='white', command=lambda:enter('+')).grid(column = 9, row = 4)
subs = Button(f,width = 5, height = 2, text = '-', bg = 'orange', foreground='white', command=lambda:enter('-')).grid(column = 9, row = 3)
equalbtn = Button(f2,width = 5, height = 2, text = '=', bg = 'orange', foreground='white', command=lambda:equal()).grid(column = 9, row = 1)
mult = Button(f,width = 5, height = 2, text = '*', bg = 'orange', foreground='white', command=lambda:enter('*')).grid(column = 9, row = 2)
div = Button(f,width = 5, height = 2, text = '/', bg = 'orange', foreground='white', command=lambda:enter('/')).grid(column = 9, row = 1)
perc = Button(f,width = 5, height = 2, text = '%', bg = 'dark grey', command=lambda:percent()).grid(column = 8, row = 1)
plusminus = Button(f,width = 5, height = 2, text = '+/-', bg = 'dark grey', command=lambda:sign_change()).grid(column = 7, row = 1)
ac = Button(f,width = 5, height = 2, text = 'AC', bg = 'dark grey', command = lambda:clear_all()).grid(column = 6, row = 1)
c = Button(f,width = 5, height = 2, text = 'C', bg = 'dark grey', command=lambda:clear()).grid(column = 5, row = 1)
point = Button(f2,width = 5, height = 2, text = '.', bg = 'grey', command=lambda:enter('.')).grid(column = 8, row = 1)
n0 = Button(f2,width = 12, height = 2, text = '0', bg = 'grey', command=lambda:enter('0')).grid(column = 7, row = 1)
n1 = Button(f,width = 5, height = 2, text = '1', bg = 'grey', command=lambda:enter('1')).grid(column = 6, row = 4)
n2 = Button(f,width = 5, height = 2, text = '2', bg = 'grey', command=lambda:enter('2')).grid(column = 7, row = 4)
n3 = Button(f,width = 5, height = 2, text = '3', bg = 'grey', command=lambda:enter('3')).grid(column = 8, row = 4)
n4 = Button(f,width = 5, height = 2, text = '4', bg = 'grey', command=lambda:enter('4')).grid(column = 6, row = 3)
n5 = Button(f,width = 5, height = 2, text = '5', bg = 'grey', command=lambda:enter('5')).grid(column = 7, row = 3)
n6 = Button(f,width = 5, height = 2, text = '6', bg = 'grey', command=lambda:enter('6')).grid(column = 8, row = 3)
n7 = Button(f,width = 5, height = 2, text = '7', bg = 'grey', command=lambda:enter('7')).grid(column = 6, row = 2)
n8 = Button(f,width = 5, height = 2, text = '8', bg = 'grey', command=lambda:enter('8')).grid(column = 7, row = 2)
n9 = Button(f,width = 5, height = 2, text = '9', bg = 'grey', command=lambda:enter('9')).grid(column = 8, row = 2)
ebtn = Button(f,width = 5, height = 2, text = 'e', bg = 'grey', command=lambda:enter(str(math.exp(1)))).grid(column = 5, row = 2)
log10 = Button(f,width = 5, height = 2, text = 'log_10', bg = 'grey', command=lambda:logarithm10()).grid(column = 5, row = 3)
tan = Button(f,width = 5, height = 2, text = 'tan', bg = 'grey', command=lambda:tan_func()).grid(column = 5, row = 4)
npi = Button(f2,width = 5, height = 2, text = 'pi', bg = 'grey', command=lambda:enter(int(math.pi))).grid(column = 6, row = 1)
rad = Button(f,width = 5, height = 2, text = 'Rad', bg = 'grey', command=lambda:radians()).grid(column = 4, row = 1)
expe= Button(f,width = 5, height = 2, text = 'e^x', bg = 'grey',command=lambda:eexp()).grid(column = 4, row = 2)
ln = Button(f,width = 5, height = 2, text = 'ln', bg = 'grey', command=lambda:naturallog() ).grid(column = 4, row = 3)
cosin = Button(f,width = 5, height = 2, text = 'cos', bg = 'grey', command=lambda:cos_func()).grid(column = 4, row = 4)
sqroot = Button(f2,width = 5, height = 2, text = 'x^(1/2)', bg = 'grey', command=lambda:squareroot()).grid(column = 5, row = 1)
factorialbtn = Button(f,width = 5, height = 2, text = 'x!', bg = 'grey', command=lambda:factorial()).grid(column = 3, row = 1)
degy = Button(f,width = 5, height = 2, text = 'x^y', bg = 'grey', command=lambda:enter('**')).grid(column = 3, row = 2)
degovery = Button(f,width = 5, height = 2, text = 'x^(1/y)', bg = 'grey', command=lambda:enter('**(1/')).grid(column = 3, row = 3)
sinus = Button(f,width = 5, height = 2, text = 'sin', bg = 'grey', command=lambda:sin_func()).grid(column = 3, row = 4)
xsquare = Button(f2,width = 5, height = 2, text = 'x^2', bg = 'grey', command=lambda:square()).grid(column = 4, row = 1)
tanh = Button(f,width = 5, height = 2, text = 'tanh', bg = 'grey', command=lambda:tanh_func()).grid(column = 0, row = 1)
sinh = Button(f,width = 5, height = 2, text = 'sinh', bg = 'grey', command=lambda:sinh_func()).grid(column = 0, row = 2)
cosinh = Button(f,width = 5, height = 2, text = 'cosh', bg = 'grey', command=lambda:cosh_func()).grid(column = 0, row = 3)
obrace = Button(f,width = 5, height = 2, text = '(', bg = 'grey', command=lambda:enter('(')).grid(column = 0, row = 4)
cbrace = Button(f2,width = 5, height = 2, text = ')', bg = 'grey', command=lambda:enter(')')).grid(column = 0, row = 1)


calculator.mainloop()