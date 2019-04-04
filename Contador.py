import requests

import sys
site = sys.argv[1]
palavra = sys.argv[2]


class Counter:
    def count_repetitions(self, word, link):
        response = requests.get(link)
        page_contents = response.text
        return self.count_substring_insensitive(page_contents,word)

    def count_substring_insensitive (self, string, substring):
        return string.lower().count(substring.lower())


counter = Counter()
qty = counter.count_repetitions(palavra, site)
print(qty)

