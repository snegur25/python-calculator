from tkinter import *

window = Tk()
window.geometry("489x534")
window.title("Calculator")
try:
    icon = PhotoImage(file='evrein.png')
    window.iconphoto(True, icon)
except:
    pass

window.config(background="#0d2525") 

expression = ""
equation_text = StringVar()

def press(num):
    global expression
    expression += str(num)
    equation_text.set(expression)

def clean():
    global expression
    expression = ""
    equation_text.set("")

def reshenie():
    global expression
    try:
        total = str(eval(expression))
        equation_text.set(total)
        expression = total
    except Exception:
        equation_text.set("Error")
        expression = ""

def BackSpace():
    global expression
    if expression == "Error":
        expression = ""
    else:
        expression = expression[:-1]

    equation_text.set(expression)
    
def checksymbols(char):
    Allowed ="0123456789+-*/.()"
    return char in Allowed

vcmd = window.register(checksymbols)


display = Entry(
    window, 
    textvariable=equation_text, 
    font=('Arial', 28, 'bold'), 
    fg='#00ff00', 
    bg='black', 
    justify='right',
    bd=10,
    relief="raised",
    validate='key',
    validatecommand=(vcmd, '%S')    
)




Button1 = Button(window,text="1",font=('Arial',22,'bold'),fg='#00ff00',bg='black',relief="raised")
Button1.config(command=lambda: press("1")) 

Button2 = Button(window,text="2",font=('Arial',22,'bold'),fg='#00ff00',bg='black',relief="raised")
Button2.config(command=lambda: press("2"))

Button3 = Button(window,text="3",font=('Arial',22,'bold'),fg='#00ff00',bg='black',relief="raised")
Button3.config(command=lambda: press("3"))

Button4 = Button(window,text="4",font=('Arial',22,'bold'),fg='#00ff00',bg='black',relief="raised")
Button4.config(command=lambda: press("4"))

Button5 = Button(window,text="5",font=('Arial',22,'bold'),fg='#00ff00',bg='black',relief="raised")
Button5.config(command=lambda: press("5"))

Button6 = Button(window,text="6",font=('Arial',22,'bold'),fg='#00ff00',bg='black',relief="raised")
Button6.config(command=lambda: press("6"))

Button7 = Button(window,text="7",font=('Arial',22,'bold'),fg='#00ff00',bg='black',relief="raised")
Button7.config(command=lambda: press("7"))

Button8 = Button(window,text="8",font=('Arial',22,'bold'),fg='#00ff00',bg='black',relief="raised")
Button8.config(command=lambda: press("8"))

Button9 = Button(window,text="9",font=('Arial',22,'bold'),fg='#00ff00',bg='black',relief="raised")
Button9.config(command=lambda: press("9"))

Button0 = Button(window,text="0",font=('Arial',22,'bold'),fg='#00ff00',bg='black',relief="raised")
Button0.config(command=lambda: press("0"))

ButtonEqual = Button(window,text="=",font=('Arial',22,'bold'),fg='#00ff00',bg='black',relief="raised")
ButtonEqual.config(command=reshenie)

ButtonC = Button(window,text="C",font=('Arial',22,'bold'),fg='#00ff00',bg='black',relief="raised")
ButtonC.config(command=clean)

ButtonSkoba = Button(window,text="(",font=('Arial',22,'bold'),fg='#00ff00',bg='black',relief="raised")
ButtonSkoba.config(command=lambda: press("("))

ButtonSkoba2 = Button(window,text=")",font=('Arial',22,'bold'),fg='#00ff00',bg='black',relief="raised")
ButtonSkoba2.config(command=lambda: press(")"))

ButtonPlus = Button(window,text="+",font=('Arial',22,'bold'),fg='#00ff00',bg='black',relief="raised")
ButtonPlus.config(command=lambda: press("+"))

ButtonMinus = Button(window,text="-",font=('Arial',22,'bold'),fg='#00ff00',bg='black',relief="raised")
ButtonMinus.config(command=lambda: press("-"))

ButtonUmnojenie = Button(window,text="*",font=('Arial',22,'bold'),fg='#00ff00',bg='black',relief="raised")
ButtonUmnojenie.config(command=lambda: press("*"))

ButtonDelenie = Button(window,text="/",font=('Arial',22,'bold'),fg='#00ff00',bg='black',relief="raised")
ButtonDelenie.config(command=lambda: press("/"))

ButtonZapetaika = Button(window,text=",",font=('Arial',22,'bold'),fg='#00ff00',bg='black',relief="raised")
ButtonZapetaika.config(command=lambda: press("."))

ButtonBackSpace = Button(window,text="⌫",font=('Arial',22,'bold'),fg='#00ff00',bg='black',relief="raised")
ButtonBackSpace.config(command=BackSpace)


button_size = {"width": 90, "height": 58}

ButtonC.place(x=20,y=180,**button_size)
ButtonSkoba.place(x=136,y=180,**button_size)
ButtonSkoba2.place(x=252,y=180,**button_size)
Button7.place(x=20,y=250,**button_size)
Button8.place(x=136,y=250,**button_size)
Button9.place(x=252,y=250,**button_size)
Button4.place(x=20,y=320,**button_size)
Button5.place(x=136,y=320,**button_size)
Button6.place(x=252,y=320,**button_size)
Button1.place(x=20,y=390,**button_size)
Button2.place(x=136,y=390,**button_size)
Button3.place(x=252,y=390,**button_size)
Button0.place(x=20,y=460,**button_size)
ButtonPlus.place(x=368,y=460,**button_size)
ButtonMinus.place(x=368,y=250,**button_size)
ButtonUmnojenie.place(x=368,y=320,**button_size)
ButtonDelenie.place(x=368,y=390,**button_size)
ButtonEqual.place(x=136,y=460,**button_size)
ButtonBackSpace.place(x=368,y=180, **button_size)
ButtonZapetaika.place(x=252,y=460, **button_size)
display.place(x = 20, y=93, width=442, height=80)

window.mainloop()