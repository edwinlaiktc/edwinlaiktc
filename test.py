import sys

if '__main__' == __name__:
    kwargs = dict(x.split('=', 1) for x in sys.argv[1:] if x.find('=') != -1)
    args = list(x for x in sys.argv[1:] if x.find('=') == -1)

    print(args)
    print(kwargs)

    exit(0);
