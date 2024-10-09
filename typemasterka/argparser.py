import argparse
import string


class ArgParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description="The Typemasterka CLI - practice typing, or visualize your typing statistics")

        self.parser.add_argument(
            '--input', type=str, default='stats.json', help=f"The statsistics file to read/write - 'stats.json' by default")
        self.parser.add_argument('--charset', type=str, default='lowercase',
                                 help='Determines the character subset to practice typing. Choose from: lowercase (default), uppercase, letters, numbers, punctuation, parentheses, all. Other options are treated as custom character sets.')
        self.parser.add_argument('--analyze', action='store_true', default=False,
                                 help='Turn on analysis mode instead of typing practice')

    @staticmethod
    def determine_character_subset(charset):
        charset_dict = {
            'lowercase': string.ascii_lowercase,
            'uppercase': string.ascii_uppercase,
            'letters': string.ascii_letters,
            'numbers': string.digits,
            'punctuation': string.punctuation,
            'parentheses': '()[]{}<>',
            'all': string.printable
        }

        if charset in charset_dict:
            return charset_dict[charset]
        else:
            print(f"Using custom character set: {charset}")
            return charset

    @property
    def stats_dict_path(self):
        return self.args.input

    @property
    def character_subset(self):
        char_type_str = self.args.charset
        return self.determine_character_subset(char_type_str)

    @property
    def is_in_analysis_mode(self):
        return self.args.analyze

    def parse(self):
        self.args = self.parser.parse_args()
