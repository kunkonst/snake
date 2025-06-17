from tkinter import *
from random import *


class SimpleSnake:
    def __init__(self):
        # Создание окна
        self.root = Tk()
        self.root.title("Простая змейка")
        
        self.caption = Label(self.root, text="Счёт: 0", font=("Arial", 14), fg="Black", bg="White")
        self.caption.pack(pady=5)

        self.canvas = Canvas(self.root, width=400, height=400, bg="black")
        self.canvas.pack() # размещаем холст в окне
        
        # Параметры игры
        self.snake = [[randint(0, 19), randint(0, 19), "Right"]]  # начальная позиция змейки и другие параметры игры
        self.direction = "Right"
        self.old_direction = "Right"
        self.food = [randint(0, 19), randint(0, 19)]
        if self.food[0] == self.snake[0][0] and self.food[1] == self.snake[0][1]:
            self.create_food()
        self.food_eaten = True 
        self.speed = 260

        # Управление
        self.canvas.focus_set() # фокус на холсте, чтобы он мог получать события клавиатуры
        self.canvas.bind("<Key>", self.change_direction)
        
        # Запуск игры
        self.game_loop()
        self.root.mainloop()
        
    def change_direction(self, event):
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            self.direction = event.keysym
        """Изменяет направление змейки"""
        #print("Нажата клавиша", event.keysym)
  
    def rgb_to_hex(self, r, g, b):
        return f'#{r:02x}{g:02x}{b:02x}'

    def create_food(self):
        self.food = [randint(0, 19), randint(0, 19)]
        for segment in self.snake:
            if self.food[0] == segment[0] and self.food[1] == segment[1]:
                self.create_food()
                    
    def move_snake(self):
                
        if self.snake[0][0] == self.food[0] and self.snake[0][1] == self.food[1]:
            self.food_eaten = True
            length = len(self.snake)
            #print("съедено")
            if self.speed > 30:
                self.speed -= 3
            else:
                self.speed = 30
            self.caption.config(text=f"Счёт: {len(self.snake)}")
            if self.snake[length - 1][2] == "Right":
                self.snake.append([self.snake[length - 1][0] - 1, self.snake[length - 1][1], "Right"])
            elif self.snake[length - 1][2] == "Left":
                self.snake.append([self.snake[length - 1][0] + 1, self.snake[length - 1][1], "Left"])
            elif self.snake[length - 1][2] == "Up":
                self.snake.append([self.snake[length - 1][0], self.snake[length - 1][1] + 1, "Up"])
            elif self.snake[length - 1][2] == "Down":
                self.snake.append([self.snake[length - 1][0], self.snake[length - 1][1] - 1, "Down"])
            #print("snake append", self.snake)
            
        #print("1 old_direction = ", self.snake[0][2], "direction = ", self.direction)
        if self.snake[0][2] != self.direction:
            self.old_direction = self.snake[0][2]
            self.snake[0][2] = self.direction
   
        if len(self.snake) > 1: 
            for i in range(len(self.snake)-1, 0, -1):
                #print("len(self.snake) = ", len(self.snake), "i = ", i)
                self.snake[i][0] = self.snake[i-1][0]
                self.snake[i][1] = self.snake[i-1][1]
                self.snake[i][2] = self.snake[i-1][2]
           
        
        if self.direction == "Right" and self.old_direction != "Left":
            self.snake[0][0] += 1
        elif self.direction == "Left" and self.old_direction != "Right":
            #print("2 old_direction = ", self.old_direction, "direction = ", self.direction)
            self.snake[0][0] -= 1
        elif self.direction == "Up" and self.old_direction != "Down":
            self.snake[0][1] -= 1
        elif self.direction == "Down" and self.old_direction != "Up":
            self.snake[0][1] += 1
    
        if self.direction == "Right" and self.old_direction == "Left":
            self.snake[0][0] -= 1
        elif self.direction == "Left" and self.old_direction == "Right":
            self.snake[0][0] += 1
        elif self.direction == "Up" and self.old_direction == "Down":
            self.snake[0][1] += 1
        elif self.direction == "Down" and self.old_direction == "Up":
            self.snake[0][1] -= 1

        for i in range(len(self.snake)):
            if self.snake[i][0] > 19:
                self.snake[i][0] = 0
            elif self.snake[i][0] < 0:
                self.snake[i][0] = 19
            if self.snake[i][1] > 19:
                self.snake[i][1] = 0
            elif self.snake[i][1] < 0:
                self.snake[i][1] = 19
            #self.snake[i] = self.snake[i-1][::]

        if len(self.snake) > 4:
            for i in range(1,len(self.snake)):
                if self.snake[0][0] == self.snake[i][0] and self.snake[0][1] == self.snake[i][1]:
                    print("Финальный счёт: ", len(self.snake))
                    print("Игра окончена")
                    self.root.quit()

        self.canvas.focus_set()
        
        
        """Двигает змейку"""
    
    def draw(self):
        self.canvas.delete("all")
        box_color = self.rgb_to_hex(0, 255, 0)
        i = 0
        step = 255 // len(self.snake)
        for segment in self.snake:
            box_color = self.rgb_to_hex(0, 255-i*step, i*step) # цвет змейки   
            i += 1
            #print("i = ", i, "box_color = ", box_color)
            self.canvas.create_rectangle(segment[0] * 20, segment[1] * 20, (segment[0] + 1) * 20, (segment[1] + 1) * 20, fill = box_color)
        if self.food_eaten:
            self.create_food()
                
                
            self.food_eaten = False
        self.canvas.create_rectangle(self.food[0] * 20, self.food[1] * 20, (self.food[0] + 1) * 20, (self.food[1] + 1) * 20, fill = "red")
        #print(self.snake)

 
    def game_loop(self):
        """Главный игровой цикл"""
        self.move_snake()
        self.draw()
               
        
        # Повторить через 200 миллисекунд
        if len(self.snake) > 0:  # если игра не окончена
            #print("speed = ", self.speed)
            self.root.after(self.speed, self.game_loop)

game = SimpleSnake()