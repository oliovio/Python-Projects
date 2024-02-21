import tkinter as tk

def on_click(event):
    global equation
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(equation.get()))
            equation.set(result)
        except Exception as e:
            equation.set("Error")
            equation_field.update()
    elif text == "C":
        equation.set("")
    else:
        equation.set(equation.get() + text)
    equation_field.update()

root = tk.Tk()
root.title("Calculator")

equation = tk.StringVar()
equation_field = tk.Entry(root, textvariable=equation, justify='right', font=('arial', 20, 'bold'))
equation_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, sticky="nsew")

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

for i, button in enumerate(buttons):
    btn = tk.Button(root, text=button, font=('arial', 20, 'bold'), width=4, height=2)
    btn.grid(row=(i//4)+1, column=i%4, sticky="nsew")
    btn.bind("<Button-1>", on_click)

# Make the grid cells expandable
for i in range(4):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
