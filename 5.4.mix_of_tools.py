from itertools import chain


def interleave(*iterable):
    print(list(chain(*zip(*iterable))))
