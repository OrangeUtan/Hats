import csv
from collections import defaultdict
from pathlib import Path


def get_locales_from_csvfile(csvfile: Path):
    strings_prefix = csvfile.name.removesuffix("csv")

    with csvfile.open("r", encoding="utf-8") as f:
        reader = csv.reader(f, dialect=csv.excel)
        header = next(reader)
        locale_names = header[1:]

        locales = defaultdict(dict)
        for row in reader:
            string = strings_prefix + row[0]
            for i, translation in enumerate(row[1:]):
                locales[locale_names[i]][string] = translation

    return locales


def get_locales_from_csvfiles(*csvfiles: Path):
    locales = defaultdict(dict)
    for file in csvfiles:
        for locale, strings in get_locales_from_csvfile(file).items():
            locales[locale].update(strings)

    return locales
