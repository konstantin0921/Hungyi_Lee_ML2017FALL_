def read_words(filepath):
    """read all words from the file path and returns a list of all words

    filepath: String, indicates the location of file
    returns: a list, each element is a single word in the given file
    """
    with open(filepath, 'r') as f:
        content = f.read()
        words = content.split()
        return words

def ordering_and_count_words(words):
    """give each word a unique number according to the order it appears

    returns: a list of tuples, each tuple contains 3 elements, (word,numbering,count)
    """
    result = list()
    word_numbering_lookup = dict()
    word_count = dict()
    index = 0
    for word in words:
        if word not in word_numbering_lookup:
            word_numbering_lookup[word] = index
            word_count[word] = 1
            index += 1
        else:
            word_count[word] += 1

    reverse_lookup = [(numbering,word) for numbering, word in zip(word_numbering_lookup.values(), word_numbering_lookup.keys())]

    for numbering , word in sorted(reverse_lookup):
        result.append((word, numbering, word_count[word]))
    return result


def write_to_file(content, path):
    """write the content to the given path"""
    with open(path, 'w') as f:
        total = len(content)
        for i in range(total):
            w,n,c = content[i]
            f.write('{} {} {}'.format(w,n,c))
            if i != total - 1:
                f.write('\n')


def main():
    #test = ['ntu', 'ml', 'mlds', 'ml', 'ntu' ,'ntuee']
    #print(ordering_and_count_words(test))
    filepath = 'words.txt'
    words = read_words(filepath)
    content = ordering_and_count_words(words)
    write_to_file(content, 'Q1.txt')
if __name__ == '__main__':
    main()

