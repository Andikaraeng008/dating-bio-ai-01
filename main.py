import os

TEXT = "Looking for someone who texts back slower than me, because at 3 a.m. I have already planned our wedding, named the kids, and debugged your attachment style."


def main():
    assert 1 <= len(TEXT) <= 180 and TEXT.strip(), "gate: 1-180 chars, not whitespace-only"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
