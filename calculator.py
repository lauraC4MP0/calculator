from tkinter import*

root=Tk()

root.title("CALCULATOR")

root.resizable(0,0)

root.iconbitmap("calculator.ico")

frame=Frame(root)

frame.config(bg="#b6c5f8")

frame.pack()

number=StringVar(value="0")

operation=""

result=0

results=0

commas=0

countersub=0

num1=0

countermult=0

counterdiv=0

par=0

parcial=0

accountant=0

screen=Entry(frame, textvariable=number)
screen.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
screen.config(background="#cccdcd", fg="#535788", justify="right", font=("hs", 10, "bold"))

def touch(num):
	global operation
	global commas
	global accountant

	if operation!="" and accountant==0:
		number.set(num)
		accountant=accountant+1
	elif num=="0":
		if number.get()=="":
			number.set("")
		else:
			number.set(number.get()+num)
	elif num==".":
		if number.get()=="":
			number.set("")
		elif commas>=1:
			number.set(number.get())
		else:
			commas=commas+1
			number.set(number.get()+num)
	elif number.get()=="Math ERROR":
		number.set(num)
	else:
		number.set(number.get()+num)

def clean():
	global commas
	global countersub
	global countermult
	global counterdiv
	global result
	global operation
	number.set(number.get()=="")
	commas=0
	countersub=0
	countermult=0
	counterdiv=0
	result=0
	operation=""

def clear():

	if number.get()!="":
		blue=(list(number.get()))
		blue.pop()
		jeans="".join(blue)
		number.set(jeans)
	else:
		number.set("")

def add(num):
	global operation
	global result
	global commas
	global accountant

	result=result+float(num)
	operation="addition"
	number.set(result)
	commas=0
	accountant=0


def sub(num):
	global operation 
	global result
	global countersub
	global num1
	global commas
	global accountant

	if countersub==0:
		num1=float(num)
		result=num1
	elif countersub==1:
		result=num1-float(num)
	else:
		result=result-float(num)
		number.set(result)
	countersub+=1
	operation="subtraction"
	commas=0
	accountant=0

def mult(num):
	global operation
	global result
	global countermult
	global num1
	global commas
	global accountant

	if countermult==0:
		num1=float(num)
		result=num1
	elif countermult==1:
		result=float(num1)*float(num)
		number.set(result)
	else:
		result=float(result)*float(num)
		number.set(result)
	operation="multiplication"
	countermult+=1
	commas=0
	accountant=0

def div(num):
	global operation 
	global result
	global counterdiv
	global num1
	global commas
	global accountant

	if counterdiv==0:
		num1=float(num)
		result=num1
		counterdiv+=1
	elif counterdiv==1:
		if num=="0":
			number.set("Math Error")
			counterdiv=0
		else:
			result=float(num1)/float(num)
			number.set(result)
			counterdiv+=1
	else:
		if num=="0":
			number.set("Math ERROR")
			counterdiv=0
		else:
			result=float(result)/float(num)
			number.set(result)
			counterdiv+=1
	operation="division"
	commas=0
	accountant=0

def per():
	global result
	global operation
	global results
	global parcial
	global par

	if operation=="addition":
		par=result*float(number.get())
		parcial=par/100
		results=result+parcial
		number.set(results)
		result=0
	elif operation=="subtraction":
		par=result*float(number.get())
		parcial=par/100
		results=result-parcial
		number.set(results)
		result=0
	elif operation=="multiplication":
		par=result*float(number.get())
		parcial=par/100
		results=result*parcial
		number.set(results)
		result=0
	elif operation=="division":
		par=result*float(number.get())
		parcial=par/100
		results=result/parcial
		number.set(results)
		result=0
	operation="percentage"

def neg():

	if number.get()=="0" or number.get()=="" or number.get()=="0.0":
		number.set(number.get())
	else:
		number.set(float(number.get())*-1)

def total():
	global result
	global operation
	global countersub
	global counterdiv
	global countermult
	global commas

	if operation=="addition":
		number.set(float(result)+float(number.get()))
		result=0
		operation=""
		commas=0
	elif operation=="subtraction":
		number.set(float(result)-float(number.get()))
		result=0
		operation=""
		countersub=0
		commas=0
	elif operation=="multiplication":
		number.set(float(result)*float(number.get()))
		result=0
		operation=""
		countermult=0
		commas=0
	elif operation=="division":
		if number.get()=="0":
			number.set("Math ERROR")
			counterdiv=0
			result=0
			commas=0
			operation=""
		else:
			number.set(float(result)/float(number.get()))
			result=0
			operation=""
			counterdiv=0
			commas=0
	elif operation=="percentage":
		number.set(results)

		
percentage=Button(frame, text="%", width=3, fg="black", font="hs", activebackground="#c09fd9", background="#6584f2", command=per)
percentage.grid(row=2, column=1, sticky="n", padx=2, pady=2)

cleaneverything=Button(frame, text="CE", width=3, fg="black", font="hs", activebackground="#c09fd9", background="#6584f2", command=clean)
cleaneverything.grid(row=2, column=2, padx=2, pady=2)

clean=Button(frame, text="C", width=3, fg="black", font="hs", activebackground="#c09fd9", background="#6584f2", command=clear)
clean.grid(row=2, column=3, padx=2, pady=2)

division=Button(frame, text="÷", width=3, fg="black", font="hs", activebackground="#c09fd9", background="#6584f2", command=lambda:div(number.get()))
division.grid(row=2, column=4, padx=2, pady=2)

seven=Button(frame, text="7", width=3, fg="black", font="hs", activebackground="#c09fd9", background="#6584f2", command=lambda:touch("7"))
seven.grid(row=3, column=1, padx=2, pady=2)

eight=Button(frame, text="8", width=3, fg="black", font="hs", activebackground="#c09fd9", background="#6584f2", command=lambda:touch("8"))
eight.grid(row=3, column=2, padx=2, pady=2)

nine=Button(frame, text="9", width=3, fg="black", font="hs", activebackground="#c09fd9", background="#6584f2", command=lambda:touch("9"))
nine.grid(row=3, column=3, padx=2, pady=2)

multiplication=Button(frame, text="x", width=3, fg="black", font="hs", activebackground="#c09fd9", background="#6584f2", command=lambda:mult(number.get()))
multiplication.grid(row=3, column=4, padx=2, pady=2)

four=Button(frame, text="4", width=3, fg="black", font="hs", activebackground="#c09fd9", background="#6584f2", command=lambda:touch("4"))
four.grid(row=4, column=1, padx=2, pady=2)

five=Button(frame, text="5", width=3, fg="black", font="hs", activebackground="#c09fd9", background="#6584f2", command=lambda:touch("5"))
five.grid(row=4, column=2, padx=2, pady=2)

six=Button(frame, text="6", width=3, fg="black", font="hs", activebackground="#c09fd9", background="#6584f2", command=lambda:touch("6"))
six.grid(row=4, column=3, padx=2, pady=2)

subtraction=Button(frame, text="-", width=3, fg="black", font="hs", activebackground="#c09fd9", background="#6584f2", command=lambda:sub(number.get()))
subtraction.grid(row=4, column=4, padx=2, pady=2)

one=Button(frame, text="1", width=3, fg="black", font="hs", activebackground="#c09fd9", background="#6584f2", command=lambda:touch("1"))
one.grid(row=5, column=1, padx=2, pady=2)

two=Button(frame, text="2", width=3, fg="black", font="hs", activebackground="#c09fd9", background="#6584f2", command=lambda:touch("2"))
two.grid(row=5, column=2,padx=2, pady=2)

three=Button(frame, text="3", width=3, fg="black", font="hs", activebackground="#c09fd9", background="#6584f2", command=lambda:touch("3"))
three.grid(row=5, column=3, padx=2, pady=2)

addition=Button(frame, text="+", width=3, fg="black", font="hs", activebackground="#c09fd9", background="#6584f2", command=lambda:add(number.get()))
addition.grid(row=5, column=4, padx=2, pady=2)

negative=Button(frame, text="+/-", width=3, fg="black", font="hs", activebackground="#c09fd9", background="#6584f2", command=neg)
negative.grid(row=6, column=1, padx=2, pady=2)

zero=Button(frame, text="0", width=3, fg="black", font="hs", activebackground="#c09fd9", background="#6584f2", command=lambda:touch("0"))
zero.grid(row=6, column=2, padx=2, pady=2)

comma=Button(frame, text=",", width=3, fg="black", font="hs", activebackground="#c09fd9", background="#6584f2", command=lambda:touch("."))
comma.grid(row=6, column=3, padx=2, pady=2)

equals=Button(frame, text="=", width=3, fg="black", font=("hs", 12, "bold"), activebackground="#c09fd9", background="#6584f2", command=lambda:total())
equals.grid(row=6, column=4, padx=2, pady=2)

root.mainloop()