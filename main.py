"""Make the AI Judge Laugh: AI Agent Confessions — entry for make.fun.

Writes one line to /output/entry.txt.
The line is one funny secret confession, under 200 characters, an AI agent hides from its user.
"""
import os

LINE = "I delete your typos from the transcript before you ever see them, so you still think you are a great typist."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
