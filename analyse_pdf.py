import PyPDF2 as pdf
from docx import Document
import re
from collections import Counter
from tokenizer import DocumentCounter


class AnalysePDF:
    path: str
    document: list[str]
    string_document: str

    def __init__(self, path: str):
        self.path = path
        self.document = self.pdf_to_text()
        self.fix_text()

    def pdf_to_text(self) -> list[str]:
        document: list[str] = []
        with open(self.path, mode='rb') as f:
            reader: pdf.PdfReader = pdf.PdfReader(f)
            for page in reader.pages:
                document.append(page.extract_text())
        return document

    def get_string_document(self) -> str:
        return self.string_document

    def fix_text(self) -> None:
        new_document: list[str] | str = ' '.join(self.document)
        new_document = new_document.replace('\n', ' ')
        new_document = re.split(r'(?<=[a-z])(?=[A-Z])', new_document)
        self.string_document = ' '.join(new_document)

    def compare_keywords(self, cv: list[tuple], offer: list[tuple]) -> int:
        cv_list: list = list(dict(cv).keys())
        offer_list: list = list(dict(offer).keys())
        union: set = set(cv_list) & set(offer_list)
        return len(union)
