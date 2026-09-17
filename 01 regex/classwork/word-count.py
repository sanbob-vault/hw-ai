import re
import sys
from collections import Counter
from pathlib import Path


def main(file_path: Path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        print(f"- Файл {file_path} не найден")
        return

    pattern = r"(\w+(?:\s|.|,|\!|\?))"
    result = re.findall(pattern, text)
    c = Counter([word[:-1].lower() for word in result])
    print(c.most_common(10))


if __name__ == "__main__":
    arg = Path("f2.txt.utf")

    if len(sys.argv) > 1:
        arg = Path(sys.argv[-1])

    main(arg)
