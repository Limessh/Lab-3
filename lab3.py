import tkinter as tk
from tkinter import messagebox
import random
import string
import pygame
import time


def cancel():
    window.destroy()

pygame.mixer.init()
def play_music():
    pygame.mixer.music.load('01.mp3')
    pygame.mixer.music.play(-1)

def generate_key():
    user_num = kod_entry.get()
    if len(user_num) != 6:
        messagebox.showerror("Ошибка ввода", "Введите 6-значное число.")
        return
    generate_key_button.place_forget() 
    key_button.place_forget()
    num1 = user_num[:3]
    num2 = user_num[3:]
    random_letters1 = ''.join(random.choices(string.ascii_uppercase, k=2))
    random_letters2 = ''.join(random.choices(string.ascii_uppercase, k=2))
    num3 = str(int(num1) + int(num2)).zfill(4)
    key = f'{num1}{random_letters1}-{num2}{random_letters2} {num3}'
    status_label.place (relx=0.5, rely=0.9,anchor='center') 
    blink_animation('Генерация ключа...', 3)
    generate_key_button.place(relx=0.5, rely=0.9, anchor='center')
    key_button.place(relx=0.5, rely=0.9, anchor='center')
    kod_entry.delete(0, tk.END)
    kod_entry.insert(0, key)
    status_label.place_forget()


def blink_animation(text, duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        status_label.config(text=text)
        window.update()
        time.sleep(0.5)
        status_label.config(text="")
        window.update()
        time.sleep(0.5)
    status_label.config(text="") 

window = tk.Tk()
window.title('My app')
window.geometry('596x380')
bg_img = tk.PhotoImage(file='images lab3.png')

label_bg = tk.Label(window, image=bg_img)
label_bg.place(x=0, y=0, relwidth=1, relheight=1)

status_label = tk.Label(window, font=("Helvetica", 15, "italic"), bg='DarkViolet')
status_label.place (relx=0.5, rely=0.9,anchor='center')
blink_animation('Запуск программы...', 3)
status_label.place_forget()

kod_start = tk.Label(window, text='Введите 6-значный код:', font=('Consolas', 20), bg ='DarkViolet',fg='MistyRose', justify='center')
kod_start.place(relx=0.5, rely=0.28, anchor='center')
kod_entry = tk.Entry(window, width=20, font=('Verdana', 16),bg ='DarkViolet',fg='MistyRose', justify='center')
kod_entry.place(relx=0.5, rely=0.38, anchor='center')

key_button = tk.Label(window, width=36, height=3, text='', bg ='DarkViolet', justify='center')
key_button.place(relx=0.5, rely=0.9, anchor='center')
generate_key_button = tk.Button(window, text='Сгенерировать ключ',  font=('Consolas', 30),fg='DarkViolet', justify='center', command=generate_key)
generate_key_button.place(relx=0.5, rely=0.9, anchor='center')

play_music()
window.mainloop()
