import re
import sys


# Matches common US phone formats with optional +1/1 country code.
# Area code and exchange must start with 2-9 (NANP rules).
PHONE_RE = re.compile(
    r"""
    (?<!\d)                        # no leading digit
    (?:\+?1[\s\-.])?               # optional country code: +1, 1, 1-, 1.
    (?:
        \(([2-9]\d{2})\)           # (NXX) with parens
        |
        ([2-9]\d{2})               # NXX without parens
    )
    [\s\-.]                        # separator
    ([2-9]\d{2})                   # exchange (NXX)
    [\s\-.]                        # separator
    (\d{4})                        # subscriber
    (?!\d)                         # no trailing digit
    """,
    re.VERBOSE,
)


def find_phones(text):
    results = []
    for match in PHONE_RE.finditer(text):
        area = match.group(1) or match.group(2)
        exchange = match.group(3)
        subscriber = match.group(4)
        normalized = f"({area}) {exchange}-{subscriber}"
        results.append((match.start(), match.group().strip(), normalized))
    return results


def main():
    if len(sys.argv) < 2:
        print("Usage: python phone.py <file> [file ...]")
        sys.exit(1)

    for path in sys.argv[1:]:
        try:
            with open(path, encoding="utf-8", errors="replace") as f:
                text = f.read()
        except OSError as e:
            print(f"Error reading {path}: {e}", file=sys.stderr)
            continue

        matches = find_phones(text)
        if not matches:
            print(f"{path}: no phone numbers found")
        else:
            print(f"{path}: {len(matches)} phone number(s) found")
            for pos, raw, normalized in matches:
                print(f"  char {pos:>6}: {raw!r:25} -> {normalized}")


if __name__ == "__main__":
    main()
