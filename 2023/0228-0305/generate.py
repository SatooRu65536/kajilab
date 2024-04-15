import pandas as pd
import pathlib


PERSON_ID = "Person1201"
labels = ['stay', 'walk', 'jog', 'skip', 'stUp', 'stDown']

files = [
    {
        "label": l,
        "file": str(list(
            pathlib
            .Path(f"./data/HASC-BasicActivity/{i+1}_{l}/{PERSON_ID}")
            .glob("*-acc.csv")
        )[0])
    }
    for i, l in enumerate(labels)
]

df = pd.concat([
    pd.read_csv(f["file"], header=None, names=["time", "x", "y", "z"])
    .assign(label=f["label"])
    for f in files
])

df.to_csv(f"./data/HASC-BasicActivity/{PERSON_ID}-acc.csv", index=False)
