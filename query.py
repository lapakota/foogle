import re

from reverse_index import ReverseIndex


class Query:
    def __init__(self, directory):
        self.indexes = ReverseIndex(directory).make_reverse_index()

    @staticmethod
    def prepare_query(text):
        pattern = re.compile(r'[\W_]+')
        text = text.lower()
        return re.sub(pattern, ' ', text).split()
