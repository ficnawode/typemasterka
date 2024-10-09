import tkinter as tk
import random

from typemasterka import utils


class App:
    def __init__(self, character_subset: str, stats_dict_path: str) -> None:
        self.__character_subset = character_subset
        self.__current_letter = self.__new_letter()
        self.__stats_dict_path = stats_dict_path
        self.__stats_dict = utils.load_json(self.__stats_dict_path)

        self.__root = tk.Tk()
        self.__root.title("Type the Letter")
        self.__root.geometry("300x200")
        self.__root.bind("<KeyPress>", self.__check_key)

        self.__letter_label = tk.Label(
            self.__root, text=self.__current_letter, font=("Helvetica", 72))
        self.__letter_label.pack(expand=True)

    def run(self) -> None:
        self.__root.mainloop()
        utils.dump_json(self.__stats_dict_path, self.__stats_dict)

    def __new_letter(self) -> str:
        return random.choice(self.__character_subset)

    def __set_letter_label(self, new_char: str) -> None:
        assert (len(new_char) == 1)
        self.__letter_label.config(text=new_char)

    def __update_letter(self) -> None:
        self.__current_letter = self.__new_letter()
        self.__set_letter_label(self.__current_letter)

    def __add_char_to_dict(self, char: str) -> None:
        if self.__current_letter not in self.__stats_dict:
            self.__stats_dict[self.__current_letter] = []
        self.__stats_dict[self.__current_letter] += char

    def __check_key(self, event: tk.Event) -> None:
        event_char = event.char
        self.__add_char_to_dict(event_char)
        if event_char == self.__current_letter:
            self.__update_letter()
