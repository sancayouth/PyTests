# -*- coding: utf-8 -*-


class Palindrome:

    def parseword(self, word):
        word = word.upper().replace(' ', '')
        return word == word[::-1]