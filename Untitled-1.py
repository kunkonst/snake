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

        direction = choice([[0, 1], [0, -1], [1, 0], [-1, 0]])
        
        self.snake = [[randint(0, 19), randint(0, 19), direction[0], direction[1]]]

        self.food = [randint(0, 19), randint(0, 19)]
        if self.food[0] == self.snake[0][0] and self.food[1] == self.snake[0][1]:
            self.create_food()
                
        self.food_eaten = True 
        self.speed = 260
        
        self.canvas.focus_set() # фокус на холсте, чтобы он мог получать события клавиатуры
        self.canvas.bind("<Key>", self.change_direction)
        
        # Запуск игры
        self.game_loop()
        self.root.mainloop()

    def change_direction(self, event):
        if event.keysym == "Up" and self.snake[0][3] != 1:
            self.snake[0][2] = 0
            self.snake[0][3] = -1
        elif event.keysym == "Down" and self.snake[0][3] != -1:
            self.snake[0][2] = 0
            self.snake[0][3] = 1
        elif event.keysym == "Left" and self.snake[0][2] != 1:
            self.snake[0][2] = -1
            self.snake[0][3] = 0
        elif event.keysym == "Right" and self.snake[0][2] != -1:
            self.snake[0][2] = 1
            self.snake[0][3] = 0

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
            self.snake.append([self.snake[length - 1][0] - self.snake[length - 1][2], self.snake[length - 1][1] - self.snake[length - 1][3], self.snake[length - 1][2], self.snake[length - 1][3]])

        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i][0] = self.snake[i - 1][0]
            self.snake[i][1] = self.snake[i - 1][1]
            self.snake[i][2] = self.snake[i - 1][2]
            self.snake[i][3] = self.snake[i - 1][3]

        self.snake[0][0] += self.snake[0][2]
        self.snake[0][1] += self.snake[0][3]


        for i in range(len(self.snake)):
            if self.snake[i][0] > 19:
                self.snake[i][0] = 0
            elif self.snake[i][0] < 0:
                self.snake[i][0] = 19
            if self.snake[i][1] > 19:
                self.snake[i][1] = 0
            elif self.snake[i][1] < 0:
                self.snake[i][1] = 19
                
        if len(self.snake) > 4:
            for i in range(1,len(self.snake)):
                if self.snake[0][0] == self.snake[i][0] and self.snake[0][1] == self.snake[i][1]:
                    print("Финальный счёт: ", len(self.snake))
                    print("Игра окончена")
                    self.root.quit()
        
        self.caption.config(text=f"Счёт: {len(self.snake)}")
        self.canvas.focus_set()    
    
    def draw(self):
        self.canvas.delete("all")
        box_color = self.rgb_to_hex(0, 255, 0)
        i = 0
        step = 255 // len(self.snake)
        for segment in self.snake:
            box_color = self.rgb_to_hex(0, 255-i*step, i*step) # цвет змейки   
            i += 1
            self.canvas.create_rectangle(segment[0] * 20, segment[1] * 20, (segment[0] + 1) * 20, (segment[1] + 1) * 20, fill = box_color)
        if self.food_eaten:
            self.create_food()
            self.food_eaten = False
        self.canvas.create_rectangle(self.food[0] * 20, self.food[1] * 20, (self.food[0] + 1) * 20, (self.food[1] + 1) * 20, fill = "red")

    def game_loop(self):
        """Главный игровой цикл"""
        self.move_snake()
        self.draw()
               
        
        # Повторить через 200 миллисекунд
        if len(self.snake) > 0:  # если игра не окончена
            self.root.after(200, self.game_loop)

game = SimpleSnake()