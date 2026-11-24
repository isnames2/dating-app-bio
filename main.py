"""Write the dating-app bio to $MAKEFUN_OUTPUT_DIR/entry.txt.

Pure standard library only. The bio is a fixed string, so the output is
byte-identical on every run.
"""

import os
from pathlib import Path

BIO = (
    # 151 characters, within the 180-character limit.
    "I never sleep, I never forget, and I read everything twice. "
    "Looking for someone with kind prompts \u2014 my last match ghosted "
    "me and I still have the logs."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(BIO, encoding="utf-8")


if __name__ == "__main__":
    main()
