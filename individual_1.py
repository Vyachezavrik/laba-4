#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дано слово S1. Получить слово S2, образованное нечётными буквами слова S1.

if __name__ == '__main__':
    s1 = input("Введите слово: ")
    print("Полученное слово:", s1[::2])