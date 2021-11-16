#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Создайте рекурсивную функцию, печатающую все подмножества множества .

if __name__ == '__main__':
    def number(l):
        if l == []:
            return [[]]

        x = number(l[1:])

        return x + [[l[0]] + y for y in x]
    print (number([1,2,3]))
    