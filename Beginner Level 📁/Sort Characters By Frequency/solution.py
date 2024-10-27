from collections import Counter

def frequencySort(s: str) -> str:
    #  Count the frequency of each character
    freq_count = Counter(s)
    
    #  Sort characters by frequency in descending order
    sorted_chars = sorted(freq_count.keys(), key=lambda x: freq_count[x], reverse=True)
    
    #  Build the result string based on the sorted order
    result = ''.join(char * freq_count[char] for char in sorted_chars)
    
    return result
