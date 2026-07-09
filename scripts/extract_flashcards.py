"""
Extract Anki flashcard data from YellowVault → decks.json for Quartz static site.
Parses ::: (vocabulary, bidirectional) and :: (grammar, one-way) lines.
Output: quartz/static/flashcards/vhs-decks.json
"""
import json, re, os
from pathlib import Path
from datetime import datetime

ANKI_DIR = Path(r"C:\Vaults\YellowVault\03_INFORMATIONEN\05_PROGRAMS\14_ANKI\01_DATABASE")
OUTPUT_DIR = Path(r"C:\Users\DELLPHOTO\OneDrive\Documents\GitHub\quartz-garden\quartz\static\flashcards")
OUTPUT_FILE = OUTPUT_DIR / "vhs-decks.json"

VOCAB_RE = re.compile(r'^(.+?)\s*:::\s*(.+?)(?:\s*▸\s*(.+))?$')
GRAMMAR_RE = re.compile(r'^(.+?)\s*::\s*(.+)$')

def parse_note(filepath: Path) -> dict | None:
    """Parse one Anki markdown note into structured deck data."""
    text = filepath.read_text(encoding="utf-8")
    lines = text.split("\n")

    # Extract frontmatter
    fm = {}
    in_fm = False
    for line in lines:
        if line.strip() == "---":
            if not in_fm:
                in_fm = True
                continue
            else:
                break
        if in_fm:
            if ":" in line:
                key, _, val = line.partition(":")
                fm[key.strip()] = val.strip()

    date_str = fm.get("date", "")
    deck_name = fm.get("cards-deck", "")

    # Extract H1 title
    title = ""
    for line in lines:
        if line.startswith("# ") and not line.startswith("## "):
            title = line[2:].strip()
            break

    if not title:
        title = filepath.stem

    vocab_pairs = []
    grammar_cards = []

    current_section = ""
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith("## ") or line.startswith("# "):
            current_section = line.lstrip("#").strip()
            continue

        # Try vocab first (:::) - only if line has content and no leading #
        if ":::" in line and not line.startswith("#"):
            m = VOCAB_RE.match(line)
            if m and m.group(1) and m.group(2):
                de_term = m.group(1).strip()
                en_term = m.group(2).strip()
                example = m.group(3).strip() if m.group(3) else ""
                # Clean up the English part - remove repeated German term
                en_clean = en_term.split("—")[0].strip().rstrip(",").rstrip(";")
                # Remove "▸" prefix from example
                if example.startswith("▸"):
                    example = example[1:].strip()
                vocab_pairs.append({
                    "de": de_term,
                    "en": en_clean,
                    "example": example,
                    "section": current_section
                })

        # Try grammar (::) - only single ::, not :::
        elif "::" in line and ":::" not in line and not line.startswith("#"):
            m = GRAMMAR_RE.match(line)
            if m and m.group(1) and m.group(2):
                front = m.group(1).strip()
                back = m.group(2).strip()
                grammar_cards.append({
                    "front": front,
                    "back": back,
                    "section": current_section
                })

    if not vocab_pairs and not grammar_cards:
        return None

    return {
        "id": re.sub(r'[^a-z0-9-]', '', title.lower().replace(" ", "-").replace("·", "-"))[:60],
        "title": title,
        "date": date_str,
        "deck": deck_name,
        "vocab_pairs": vocab_pairs,
        "grammar_cards": grammar_cards,
        "total_vocab": len(vocab_pairs),
        "total_grammar": len(grammar_cards)
    }


def main():
    decks = []
    md_files = sorted(ANKI_DIR.glob("*.md"))

    for fp in md_files:
        if fp.name.startswith("."):
            continue
        deck = parse_note(fp)
        if deck and deck["vocab_pairs"]:
            decks.append(deck)
            print(f"  ✓ {deck['title']}: {deck['total_vocab']} vocab + {deck['total_grammar']} grammar")

    # Sort by date descending
    decks.sort(key=lambda d: d["date"], reverse=True)

    output = {
        "generated": datetime.now().isoformat(),
        "source": str(ANKI_DIR),
        "total_decks": len(decks),
        "total_vocab_pairs": sum(d["total_vocab"] for d in decks),
        "total_grammar_cards": sum(d["total_grammar"] for d in decks),
        "decks": decks
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\n✅ Written {OUTPUT_FILE}")
    print(f"   {output['total_decks']} decks, {output['total_vocab_pairs']} vocab pairs, {output['total_grammar_cards']} grammar cards")


if __name__ == "__main__":
    main()
