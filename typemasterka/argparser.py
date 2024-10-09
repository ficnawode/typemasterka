import argparse
import string


class ArgParser:
    def __init__(self) -> None:
        parser = argparse.ArgumentParser(
            description="The Typemasterka CLI - practice typing, or visualize your typing statistics")

        parser.add_argument(
            '--input', type=str, default='stats.json', help=f"The statsistics file to read/write - 'stats.json' by default")
        parser.add_argument('--charset', type=str, default='lowercase',
                            help='Determines the character subset to practice typing. Choose from: lowercase (default), uppercase, letters, numbers, punctuation, parentheses, all. Other options are treated as custom character sets.')
        parser.add_argument('--analyze', action='store_true', default=False,
                            help='Turn on analysis mode instead of typing practice')

        self.__args = parser.parse_args()

    @property
    def stats_dict_path(self) -> str:
        return self.__args.input

    @property
    def character_subset(self) -> str:
        char_type_str = self.__args.charset
        return self.__determine_character_subset(char_type_str)

    @property
    def is_in_analysis_mode(self) -> bool:
        return self.__args.analyze

    @staticmethod
    def __determine_character_subset(charset: str) -> str:
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
