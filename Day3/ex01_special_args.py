def get_summary(*args):
    # print(f'{type(args) = }')
    # print(f'{args = }')
    args = [a for a in args if type(a) in (int, float) ]
    s = sum(args)
    c = len(args)
    a = s/c
    return {"count": c, "sum": s, "average": a}


def main():
    print(f'{get_summary(123, 456, 748)}')
    print(f'{get_summary(12, 45)}')
    print(f'{get_summary(10, 20, 30, 40, 50, 60)}')
    print(f'{get_summary(10, 20, 'vinod', 44.5, 50, 'kumar', 49, 59)}')


if __name__ == '__main__':
    main()