import tkinter as tk
import pygame
import sys
import os

pygame.mixer.init()

# minimal helper for PyInstaller
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def play_sound():
    sound1 = pygame.mixer.Sound(resource_path("flashbang.mp3"))
    sound2 = pygame.mixer.Sound(resource_path("femboy_friday.mp3"))
    sound1.play()
    sound2.play()

root = tk.Tk()

root.title("fmb")
root.attributes("-fullscreen", True)
root.geometry("1920x1080")

photo = tk.PhotoImage(file=resource_path("femboy_jumpscare.png"))
label = tk.Label(root, image=photo)
label.pack(fill="both", expand=True)

root.after(50, play_sound)

root.mainloop()
