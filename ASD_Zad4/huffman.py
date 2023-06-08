from collections import Counter
import heapq

class HuffmanNode:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def remove_non_alpha(text): # usuwanie spacji i znaków, które nie są literami alfabetu
    return ''.join(char for char in text if char.isalpha())

def count_frequencies(text): # oblicza częstotliwość wystąpień każdego znaku w tekście
    frequencies = Counter(text)
    return frequencies

def build_huffman_tree(frequencies): # tworzy drzewo Huffmana na podstawie częstotliwości znaków
    heap = []
    for char, freq in frequencies.items():
        heapq.heappush(heap, HuffmanNode(char, freq))

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def generate_codes(root, current_code, codes): # genereuje kodowanie Huffmana dla każdego znaku na podstawie drzewa Huffmana
    if root.char:
        codes[root.char] = current_code
    else:
        generate_codes(root.left, current_code + '0', codes)
        generate_codes(root.right, current_code + '1', codes)

def encode_text(text, codes): # koduje tekst na podstawie kodowania Huffmana
    encoded_text = ''.join(codes[char] for char in text)
    return encoded_text