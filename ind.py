#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":

    m = int(input())
    n = int(input())

    def a(m, n):
        if m > 0:
            if n > 0:
                return a(m - 1, a(m, n - 1))
            else:
                return a(m - 1, 1)
        return n + 1

    print(a(m, n))
