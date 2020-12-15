#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дано предложение. Поменять местами его первое и последнее слова.

if __name__ == '__main__':

    a = input("Введите предложение: ")
    word = a.split()
    word[0], word[-1] = word[-1], word[0]
    print(' '.join(word))