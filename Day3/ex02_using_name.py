from ex01_special_args import get_summary


if __name__ == '__main__':
    nums = []
    while True:
        num = input('Enter a number (0 to stop): ')
        if num == '0':
            break

        if num.isdigit():
            num = int(num)
            nums.append(num)
        else:
            print(f'non-int given; skipping.')

    print(f'Summary = {get_summary(*nums)}')
