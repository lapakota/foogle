import os
import re


class ReverseIndex:
    def __init__(self, path):
        self.path = path
        self.filenames = self.get_all_txt()
        self.documents_count = len(self.filenames)
        self.words = {}

    def make_reverse_index(self):
        words = self.transform_files()
        indexes = self.make_indexes(words)
        self.words = self.full_reverse_index(indexes)
        return self.words

    def transform_files(self):
        files_to_words = {}
        pattern = re.compile(r'[\W_]+')
        for file in self.filenames:
            with open(file, 'r', encoding="utf-8") as f:
                lower_text = f.read().lower()
                text_without_spaces = pattern.sub(' ', lower_text)
                files_to_words[file] = text_without_spaces.split()
        return files_to_words

    def make_indexes(self, files):
        total = {}
        for filename in files.keys():
            total[filename] = self.index_file(files[filename])
        return total

    @staticmethod
    def index_file(words):
        result = {}
        for index, word in enumerate(words):
            if word in result.keys():
                result[word].append(index)
            else:
                result[word] = [index]
        return result

    @staticmethod
    def full_reverse_index(words_with_pos):
        total_index = {}
        for filename in words_with_pos.keys():
            for word in words_with_pos[filename].keys():
                if word in total_index.keys():
                    if filename in total_index[word].keys():
                        total_index[word][filename].extend(words_with_pos[filename][word][:])
                    else:
                        total_index[word][filename] = words_with_pos[filename][word]
                else:
                    total_index[word] = {filename: words_with_pos[filename][word]}
        return total_index

    def get_all_txt(self):
        result = []
        for c_dir, dirs, files in os.walk(self.path):
            for file in files:
                if file.endswith("txt"):
                    result.append(os.path.join(c_dir, file))
        return result
