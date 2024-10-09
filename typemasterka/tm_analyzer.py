from typemasterka.utils import load_json

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter


class Analyzer:
    def __init__(self, stats_dict_path):
        self.stats_dict = load_json(
            stats_dict_path)

    def draw_cov_matrix(self):
        data = self.stats_dict
        letters = sorted(set(data.keys()).union(*data.values()))

        # Step 2: Create a frequency matrix
        matrix = np.zeros((len(letters), len(letters)))

        # Step 3: Count frequencies of letters in each key's list
        for i, key in enumerate(letters):
            if key in data:
                counter = Counter(data[key])
                # Total occurrences of letters under this key
                total = sum(counter.values())
                for j, letter in enumerate(letters):
                    # Normalize by total count
                    matrix[i, j] = counter[letter] / \
                        total if total > 0 else 0

        # Step 4: Plot the heatmap
        plt.figure(figsize=(8, 6))
        sns.heatmap(matrix, annot=True, cmap="Blues",
                    xticklabels=letters, yticklabels=letters)
        plt.xlabel("Letter assigned")
        plt.ylabel("Letter typed")
        plt.show()

        pass

    def draw_char_hist(self, char):
        data = self.stats_dict
        if char not in data:
            print(
                f'Your stats dictionary contains no data about the character \'{char}\'')
            return
        letter_counts = Counter(data[char])

        # Step 3: Sort letters by frequency in descending order
        sorted_letters = sorted(
            letter_counts.items(), key=lambda x: x[1], reverse=True)
        letters, counts = zip(*sorted_letters)  # Unzip into two lists

        # Step 4: Create the bar plot
        plt.figure(figsize=(8, 6))
        plt.bar(letters, counts, color='skyblue')
        plt.title(f"Frequency of Letters Under Key '{
            char}' (Descending)")
        plt.xlabel("Letters")
        plt.ylabel("Frequency")
        plt.show()

    def run(self):
        if not self.stats_dict:
            print("Your stats dictionary is empty, exiting...")
            return
        print(
            "Enter the character you wish to see the histogram of, or \'covariance\' to see the covariance matrix:")
        print("(To exit, type 'exit' or 'quit')")

        while (1):
            current_cmd = input(">>>")
            if current_cmd in ['exit', 'quit']:
                return
            elif len(current_cmd) == 1:
                self.draw_char_hist(current_cmd)
            elif len(current_cmd) == 0:
                pass
            elif current_cmd == 'covariance':
                self.draw_cov_matrix()
            else:
                print(f'Unknown option: {current_cmd}')
