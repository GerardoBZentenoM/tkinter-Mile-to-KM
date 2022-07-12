import tkinter

window = tkinter.Tk()

window.title("My first GUI program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I'm a label", font=("Arial", 24, "bold"))
my_label.pack()

# my_label.config(text="New Text 2")


def button_clicked():
    print("clic")
    new_text = input1.get()
    my_label["text"] = new_text


button = tkinter.Button(text="click me", command=button_clicked)
button.pack()

input1 = tkinter.Entry(width=10)
input1.pack()


window.mainloop()
