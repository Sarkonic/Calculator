import tkinter
import tkinter as tk

window = tk.Tk()
window.geometry("250x400")

greeting = tk.Label(text="Calculator")

num1 = tk.Button(
    text="1",
    bg="black",
    fg="white",
    width=4,
    height=2
)

num2 = tk.Button(
    text="2",
    bg="black",
    fg="white",
    width=4,
    height=2
)

num3 = tk.Button(
    text="3",
    bg="black",
    fg="white",
    width=4,
    height=2
)

num4 = tk.Button(
    text="4",
    bg="black",
    fg="white",
    width=4,
    height=2
)

num5 = tk.Button(
    text="5",
    bg="black",
    fg="white",
    width=4,
    height=2
)

num6 = tk.Button(
    text="6",
    bg="black",
    fg="white",
    width=4,
    height=2
)

num7 = tk.Button(
    text="7",
    bg="black",
    fg="white",
    width=4,
    height=2
)

plus = tk.Button(
    text="+",
    bg="black",
    fg="white",
    width=4,
    height=2
)

num8 = tk.Button(
    text="8",
    bg="black",
    fg="white",
    width=4,
    height=2
)

num9 = tk.Button(
    text="9",
    bg="black",
    fg="white",
    width=4,
    height=2
)

num0 = tk.Button(
    text="0",
    bg="black",
    fg="white",
    width=4,
    height=2
)

minus = tk.Button(
    text="-",
    bg="black",
    fg="white",
    width=4,
    height=2
)

mult = tk.Button(
    text="x",
    bg="black",
    fg="white",
    width=4,
    height=2
)

clear = tk.Button(
    text="CLEAR",
    bg="black",
    fg="white",
    width=12,
    height=2
)

enter = tk.Button(
    text="ENTER",
    bg="black",
    fg="white",
    width=12,
    height=2
)

entry = tk.Entry(width=50)
answer = tk.Entry(width=50)

entry.place(x=0, y=0)
answer.place(x=0, y=15)
num1.place(x=0, y=30)
num2.place(x=40, y=30)
num3.place(x=80, y=30)
num4.place(x=120, y=30)
num5.place(x=160, y=30)
plus.place(x=200, y=30)
num6.place(x=0, y=80)
num7.place(x=40, y=80)
num8.place(x=80, y=80)
num9.place(x=120, y=80)
num0.place(x=160, y=80)
minus.place(x=200, y=80)
mult.place(x=200, y=130)
clear.place(x=0, y=130)
enter.place(x=100, y=130)


def clean(event):
    entry.delete(0, 99)
    answer.delete(0,99)


def press1(event):
    entry.insert(99, "1")


def press0(event):
    entry.insert(99, "0")


def press2(event):
    entry.insert(99, "2")


def press3(event):
    entry.insert(99, "3")

def press4(event):
    entry.insert(99, "4")

def press5(event):
    entry.insert(99, "5")

def press6(event):
    entry.insert(99, "6")

def press7(event):
    entry.insert(99, "7")

def press8(event):
    entry.insert(99, "8")

def press9(event):
    entry.insert(99, "9")

def pressPlus(event):
    entry.insert(99, "+")

def pressMinus(event):
    entry.insert(99, "-")

def pressMult(event):
    entry.insert(99, "*")




#define a precedence of operators
def getPrecedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*':
        return 2

def isOperand(c):
    return c.isdigit()

def isOperator(c):
    return c == '+' or c == '-' or c == '*'

def isEmpty(stack):
    return len(stack) == 0

def peek(stack):
    return stack[len(stack)-1]

def infixToPostFix(infix):
    stack = []
    postfix = ''

    #scan the string from left to right
    for c in infix:
        if isOperand(c):    #if we have an operand, add it to the postfix string
            postfix+=c
        else: #check if stack is empty, then compare precedence
            if isEmpty(stack) or (getPrecedence(c) > getPrecedence(peek(stack))):
                stack.append(c)
            else: #go through stack and pop whatever is high precedence
                for s in stack:
                    if getPrecedence(s) >= getPrecedence(c):
                        postfix+=stack.pop(len(stack)-1)
                stack.append(c)
    #any remaining operators in the stack get popped
    i=len(stack)
    while i != 0:
        postfix+=stack.pop()
        i=i-1
    #answer.insert(99, postfix)  #insert the postfix (as a test, delete this and call evaluate function)
    entry.delete(0,99)          #delete the text in the entry
    answer.insert(99,evaluate(postfix))


def evaluate(postfix):
    #create a stack to store operands
    stack = []
    for c in postfix:
        if isOperand(c):
            stack.append(c)
        if isOperator(c):
            num2=stack.pop()
            num1=stack.pop()
            ans = str(eval(num1 + c + num2))
            stack.append(ans)
    return stack.pop()





#bind enter button to this function so it can "listen"
def on_change(event):
    infixToPostFix(entry.get())

#------------------------------------------------------------------
# Bind the event func to num1
num1.bind("<Button-1>", press1)
num0.bind("<Button-1>", press0)
num2.bind("<Button-1>", press2)
num3.bind("<Button-1>", press3)
num4.bind("<Button-1>", press4)
num5.bind("<Button-1>", press5)
num6.bind("<Button-1>", press6)
num7.bind("<Button-1>", press7)
num8.bind("<Button-1>", press8)
num9.bind("<Button-1>", press9)
plus.bind("<Button-1>", pressPlus)
minus.bind("<Button-1>", pressMinus)
mult.bind("<Button-1>", pressMult)

clear.bind("<Button-1>", clean)

enter.bind("<Button-1>", on_change)
#------------------------------------------------------------------

window.mainloop()
