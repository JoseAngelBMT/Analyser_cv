import tkinter as tk
from tkinter import filedialog
from analyse_pdf import AnalysePDF
from tokenizer import DocumentCounter
from linkedIn_offer import ParserLinkedIn


def select_file() -> str:
    file_path = filedialog.askopenfilename(filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
    return file_path


def main() -> None:
    path: str = select_file()
    analyse = AnalysePDF(path)
    document: str = analyse.get_string_document()

    cv = DocumentCounter(document)
    key_cv: list[tuple] = cv.get_keywords()

    linkedin = ParserLinkedIn(
        "url")
    text: str = linkedin.get_text()
    offer = DocumentCounter(text)
    key_offer: list[tuple] = offer.get_keywords()

    score: int = analyse.compare_keywords(key_cv, key_offer)
    print(f"Score: {score}")


if __name__ == '__main__':
    main()
