import re
import sys
from pathlib import Path


def get_verb_regex() -> str:
    """Регулярное выражение для поиска глаголов"""

    """
    Глагол может заканчиваться на:
    (ет, ит, ут, ют, ат, ят + [е] ИЛИ ть) + [ся, сь]
    """

    return r"\w+([еиуюая]те?|ть)(с[яь])?\b"


def get_adverb_regex() -> str:
    """Регулярное выражение для поиска наречий"""

    """
    Наречие может заканчиваться на о, е, и, а, я, у
    """

    return r"\w+[оеаяу]\b"


def get_space_regex() -> str:
    """Регулярное выражение для нахождения общего контекста"""

    """
    Любые символы кроме точки и запятой
    Потому что между связанными наречием и глаголом могут быть другие слова, а точки и запятые редко
    """

    return r"[^.,]+?"


def get_combined_regex() -> str:
    """Регулярное выражения для поиска пар глаголов с наречиями"""

    verb = get_verb_regex()
    adverb = get_adverb_regex()
    space = get_space_regex()

    # (глагол + пространство + наречие) или (наречие + пространство + глагол)
    return rf"({verb}{space}{adverb}|{adverb}{space}{verb})"


def main(file_path: Path):
    pattern = get_combined_regex()

    print("-" * 32)
    print(
        f"Собранный паттерн: {pattern}\nКоличество символов в паттерне: {len(pattern)}"
    )
    print("-" * 32, "\n")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        print(f"- Файл {file_path} не найден")
        return

    matches: list[str] = re.findall(pattern, text, flags=re.IGNORECASE)
    print("- Найденные пары:")
    print("Полная фраза -- Пара")
    for match in matches:
        full_phrase = match[0]
        first, last = full_phrase.split()[0], full_phrase.split()[-1]
        print(f"{full_phrase} -- {first} {last}")


if __name__ == "__main__":
    arg = Path("text.txt")

    if len(sys.argv) > 1:
        arg = Path(sys.argv[-1])

    main(arg)


"""
Можно улучшить эти регулярные выражения:
- Улучшить захват глаголов и наречий, например, добавить минимальную длину для наречия
- Сделать, чтобы ненужные группы не захватывались (:?)
- Захватывать глагол и наречие отдельно, чтобы выражение отдавало готовую пару
- Добавить в символы разделители контекста(точка и запятая) восклицательный и вопросительный знаки
- Улучшить разделение контекста ограничением длины между глаголом и наречием

Но, тогда я бы перешел лимит в 100 байт
"""
