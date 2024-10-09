from typemasterka.utils import load_json

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter


class Analyzer:
    def __init__(self, stats_dict_path: str) -> None:
        self.__stats_dict = load_json(
            stats_dict_path)

    def run(self) -> None:
        if not self.__stats_dict:
            print("Your stats dictionary is empty, exiting...")
            return
        print(
            "Enter the character you wish to see the histogram of, or 'confusion' to see the confusion matrix:")
        print("(To exit, type 'exit' or 'quit')")

        while (1):
            cmd = input(">>>")
            if not self.__handle_cmd(cmd):
                break

    def __handle_cmd(self, cmd: str) -> bool:
        if cmd in ['exit', 'quit']:
            return False
        elif len(cmd) == 1:
            self.__draw_char_hist(cmd)
        elif len(cmd) == 0:
            pass
        elif cmd == 'confusion':
            self.__draw_confusion_matrix()
        else:
            print(f'Unknown option: {cmd}')
        return True

    def __draw_confusion_matrix(self) -> None:
        data = self.__stats_dict
        letters = sorted(set(data.keys()).union(*data.values()))

        matrix = np.zeros((len(letters), len(letters)))

        for i, key in enumerate(letters):
            if key in data:
                counter = Counter(data[key])
                total = sum(counter.values())
                for j, letter in enumerate(letters):
                    matrix[i, j] = counter[letter] / total if total > 0 else 0

        plt.figure(figsize=(8, 6))
        sns.heatmap(matrix, annot=True, cmap="Blues",
                    xticklabels=letters, yticklabels=letters)
        plt.xlabel("Letter typed")
        plt.ylabel("Letter assigned")
        plt.show()

    def __draw_char_hist(self, char: str) -> None:
        assert (len(char) == 1)
        data = self.__stats_dict
        if char not in data:
            print(
                f'You have no statistics about character \'{char}\' yet.')
            return
        letter_counts = Counter(data[char])

        sorted_letters = sorted(
            letter_counts.items(), key=lambda x: x[1], reverse=True)
        letters, counts = zip(*sorted_letters)

        plt.figure(figsize=(8, 6))
        plt.bar(letters, counts, color='skyblue')
        plt.title(
            f'Characters typed while \'{char}\' assigned')
        plt.xlabel("Letters")
        plt.ylabel("Frequency")
        plt.show()
