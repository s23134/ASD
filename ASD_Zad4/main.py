from huffman import remove_non_alpha, count_frequencies, build_huffman_tree, generate_codes, encode_text

def main():
    text = input("Podaj tekst: ")
    text = remove_non_alpha(text)

    frequencies = count_frequencies(text)
    sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1])

    huffman_tree = build_huffman_tree(frequencies)

    codes = {}
    generate_codes(huffman_tree, '', codes)

    print("Znak\tLiczba wystąpień\tKodowanie")
    for char, freq in sorted_frequencies:
        print(f"{char}\t{freq}\t\t\t{codes[char]}")

    encoded_text = encode_text(text, codes)
    print("Zakodowany tekst:", encoded_text)

if __name__ == "__main__":
    main()