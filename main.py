import tkinter

window = tkinter.Tk()

window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)
# window.minsize(width=500, height=300)

my_label = tkinter.Label(text="is equal to:")
my_label.grid(column=0, row=1)


Km = tkinter.Label(text="0")
Km.grid(column=1, row=1)
# my_label.config(text="New Text 2")


def button_clicked():
    new_text = input1.get()
    miles = float(new_text) * 1.60934
    Km["text"] = str(miles)


button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=3)

input1 = tkinter.Entry(width=7)
input1.grid(column=1, row=0)

Miles = tkinter.Label(text="Miles")
Miles.grid(column=2, row=0)

Km1 = tkinter.Label(text="Km")
Km1.grid(column=2, row=1)

window.mainloop()
