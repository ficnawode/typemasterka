from typemasterka import typemasterka, analyzer, argparser


if __name__ == "__main__":
    p = argparser.ArgParser()

    if p.is_in_analysis_mode:
        app = analyzer.Analyzer(p.stats_dict_path)
    else:
        app = typemasterka.App(p.character_subset, p.stats_dict_path)
    app.run()
