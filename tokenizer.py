import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
from langdetect import detect


class DocumentCounter:
    document: str
    select_language: dict = {'es': 'spanish', 'en': 'english'}
    keywords: list[tuple]

    def __init__(self, document: str) -> None:
        self.document = document
        language: str = self.detect_language()
        self.keywords = self.create_keywords(language)

    def detect_language(self) -> str:
        return detect(self.document)

    def create_keywords(self, language: str = 'es') -> list[tuple]:
        words = word_tokenize(self.document)
        language = self.select_language[language]
        stopwords_list = set(stopwords.words(language))
        filter_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stopwords_list]

        counter_words = Counter(filter_words)
        keywords = counter_words.most_common(40)
        return keywords

    def get_keywords(self) -> list[tuple]:
        return self.keywords
