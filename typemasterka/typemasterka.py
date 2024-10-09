import tkinter as tk
import random

from typemasterka import utils


class App:
    def new_letter(self):
        return random.choice(self.character_subset)

    def add_char_to_dict(self, char: str):
        if char not in self.stats_dict:
            self.stats_dict[char] = []
        self.stats_dict[self.current_letter] += char

    def check_key(self, event):
        print(type(event))
        event_char = event.char
        self.add_char_to_dict(event_char)

        if event_char == self.current_letter:
            self.update_letter()

    def update_letter(self):
        self.current_letter = self.new_letter()
        self.set_letter_label(self.current_letter)

    def set_letter_label(self, new_char: str):
        assert (len(new_char) == 1)
        self.letter_label.config(text=new_char)

    def __init__(self, character_subset, stats_dict_path: str) -> None:
        self.character_subset = character_subset

        self.current_letter = self.new_letter()
        self.stats_dict_path = stats_dict_path
        self.stats_dict = utils.load_json(self.stats_dict_path)

        self.root = tk.Tk()
        self.root.title("Type the Letter")
        self.root.geometry("300x200")

        self.root.bind("<KeyPress>", self.check_key)

        self.letter_label = tk.Label(
            self.root, text=self.current_letter, font=("Helvetica", 72))
        self.letter_label.pack(expand=True)

    def run(self):
        self.root.mainloop()
        utils.dump_json(self.stats_dict_path, self.stats_dict)
