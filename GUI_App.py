#    GUI Program for chatbot

import tkinter as tk
import random
window = tk.Tk()


# functions
'''def phrase_generator():
    phrase = ["Hello  ","Hi  ","Greetings  ","Olla  "]

    name = str(entry1.get())

    return phrase[random.randint(0,3)] +    name

def display():
    #greeting = phrase_generator()

    greetings_dis = tk.Text(master= window, height=20,width=40)
    greetings_dis.grid(column=0,row=10)

    greetings_dis.insert(tk.END,greeting)
'''    

window.title("Developer Chat bot")
#title.grid(column=0,row=20)
window.geometry("800x700")

# Print Text
lab1 = tk.Label(text = "Chat Bot Creation", font= ("Courier New",30))
lab1.grid(column= 100,row = 0)

label1 = tk.Label(text="Select the category from the list", font=("Times New Roman", 20))
label1.grid(column=0, row=3)

'''
master = tk.Tk()

listbox = tk.Listbox(master)
listbox.pack()

listbox.insert("a list entry")

for item in ["one", "two", "three", "four"]:
    listbox.insert(item)
'''


# Print Button
entry1 = tk.Entry()
entry1.grid(column=0, row = 5)


but1 = tk.Button(text="Select from the list")
but1.grid(column=0, row=7)



window.mainloop()





'''
Created by : SANTHOSH KUMAR
'''