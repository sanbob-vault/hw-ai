import sys
from pathlib import Path

import matplotlib.pyplot as pp
import numpy as np


def main(file_path: Path):

    data = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                data.append([float(x) for x in line.split()])

    except FileNotFoundError:
        print(f"- Файл {file_path} не найден")
        return

    data = np.array(data)

    s1 = pp.hist(
        data[:, 0],
        density=True,
        cumulative=True,
        histtype="step",
        bins=range(-1000, 1000),
    )
    s2 = pp.hist(
        data[:, 1],
        density=True,
        cumulative=-1,
        histtype="step",
        bins=range(-1000, 1000),
    )

    pp.subplot(2, 1, 1)
    a1 = np.array(s1[0])
    a2 = np.array(s2[0])
    c2 = np.array(s2[1])
    print(a1, a2)

    pp.plot(c2[:-1], a1 + a2)

    idx = np.argmin(a1 + a2)
    print(c2[idx])
    pp.show()


if __name__ == "__main__":
    arg = Path("data/classify_ldiff.dat")

    if len(sys.argv) > 1:
        arg = Path(sys.argv[-1])

    main(arg)
