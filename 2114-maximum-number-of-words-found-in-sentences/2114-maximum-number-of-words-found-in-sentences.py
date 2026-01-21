class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        word_count=[]
        for i in sentences:
            space=i.count(' ')
            words=space+1
            word_count.append(words)
        max_words=max(word_count)
        return max_words
