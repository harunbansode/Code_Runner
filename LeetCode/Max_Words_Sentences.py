from typing import List

def mostWordsFound(sentences: List[str]) -> int:
    space_word = []
    for i in range(0, len(sentences)):
        total_words = sentences[i].count(' ') + 1
        space_word.append(total_words)
    return max(space_word)
sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
print(mostWordsFound(sentences))