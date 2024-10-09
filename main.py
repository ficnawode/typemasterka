from typemasterka import typemasterka
from typemasterka import tm_analyzer
import string


if __name__ == "__main__":
    analyze = True

    if analyze:
        app = tm_analyzer.Analyzer("stats.json")
    else:
        app = typemasterka.App(string.ascii_lowercase, "stats.json")
    app.run()
