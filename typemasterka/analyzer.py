from typemasterka.utils import load_json

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter


class Analyzer:
    def __init__(self, stats_dict_path):
        self.stats_dict = load_json(
            stats_dict_path)

    def __draw_confusion_matrix(self):
        data = self.stats_dict
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

        pass

    def __draw_char_hist(self, char):
        data = self.stats_dict
        if char not in data:
            print(
                f'Characters typed while \'{char}\' assigned')
            return
        letter_counts = Counter(data[char])

        sorted_letters = sorted(
            letter_counts.items(), key=lambda x: x[1], reverse=True)
        letters, counts = zip(*sorted_letters)

        plt.figure(figsize=(8, 6))
        plt.bar(letters, counts, color='skyblue')
        plt.title(f"Frequency of Letters Under Key '{
            char}' (Descending)")
        plt.xlabel("Letters")
        plt.ylabel("Frequency")
        plt.show()

    def __handle_cmd(self, cmd):
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

    def run(self):
        if not self.stats_dict:
            print("Your stats dictionary is empty, exiting...")
            return
        print(
            "Enter the character you wish to see the histogram of, or 'confusion' to see the confusion matrix:")
        print("(To exit, type 'exit' or 'quit')")

        while (1):
            cmd = input(">>>")
            if not self.__handle_cmd(cmd):
                break
