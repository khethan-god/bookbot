def number_of_words(text):
    words = text.split()
    return len(words)

def frequency(text):
    # convert the text into lowercase
    text = text.lower()
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq

def sort_on(d):
    return d['num']

def chars_dict_to_sorted_list(freq):
    sorted_list = []
    for ch in freq:
        sorted_list.append({'char': ch, 'num': freq[ch]})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list