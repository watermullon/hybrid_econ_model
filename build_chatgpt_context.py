from __future__ import annotations

from pathlib import Path

from src.chatgpt_export import build_chatgpt_context


def main() -> None:
    root = Path(__file__).resolve().parent
    output_path = build_chatgpt_context(root)
    print(f"Wrote ChatGPT analysis context to {output_path}")


if __name__ == "__main__":
    main()
