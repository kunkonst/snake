from tkinter import *
from keyboard import is_pressed
window = Tk()  
menu = Menu(window)
menu.add_command(label='Заново')
window.config(menu=menu)
window.title("Змейка 1")
window.geometry('640x480')
field = Canvas(window, width=630, height=475, bg='black')
field.pack()
snake = [[1, 10]]
for i in snake:
    field.create_rectangle(i[0], i[1], (i[0]+1)*10, (i[1]+1)*10, fill='green')

while not is_pressed('down'):
    if is_pressed('up'):
        snake.append(snake[0])
        snake[0][1] -= 1
        print(snake[0])
#lbl = Label(window, text="Привет")  
#lbl.grid(column=0, row=0) 
window.mainloop()