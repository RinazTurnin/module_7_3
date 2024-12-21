import re


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_word = {}
        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as file:
                file_lines = file.read()
                file_without_punctuation = re.sub(r'[,!.]', '', file_lines.lower())
                all_word[name] = file_without_punctuation.split()
        return all_word

    def find(self, word):
        counter = 1
        new_dict = {}
        for name, words in self.get_all_words().items():
            for i in words:
                if i != word.lower():
                    counter += 1
                else:
                    new_dict[name] = counter
                    break
        return new_dict

    def count(self, word):
        counter = 0
        new_dict = {}
        for name, words in self.get_all_words().items():
            for i in words:
                if i == word.lower():
                    counter += 1
                new_dict[name] = counter
        return new_dict


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
