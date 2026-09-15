import re
import sys
from pathlib import Path

VERB_REGEX = r"([A-Za-z]*(?:ет|ит))"
ADVERB_REGEX = r""

REGEX = r""


def main(file_path: Path):
    with open(file_path, "r") as file:
        text = file.read()
        result = re.search(VERB_REGEX, text)
        
        print(result.group(0))


if __name__ == "__main__":
    arg = Path("text.txt")

    if len(sys.argv) > 1:
        arg = Path(sys.argv[-1])

    main(arg)
