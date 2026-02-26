def main():
    filename = input('Enter a filename to read: ')
    f1 = open(filename, encoding='utf-8')

    method_count = 0
    method_names = []
    for line in f1: # f1 itself is an iterable (one line at a time)
        # print(line, end='')
        if line.startswith('def '):
            method_count += 1
            method_names.append(line[4:line.index('(')])

    f1.close()  # otherwise, scope of memory leak
    print(f'The given file contains {method_count} method definitions')
    print(f'{method_names = }')

if __name__ == '__main__':
    main()
