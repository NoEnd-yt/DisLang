#!/usr/bin/env python3

from sys import argv

class Token():
    def __init__(self, tokenString):
        self.tokenString = tokenString


def Lexer(line: str):
    tokenList = line.split(" ")


def main():
    if len(argv) > 1:
        file = open(argv[1], mode='r')
        lines = file.readlines()
        file.close()

if __name__ == "__main__":
    main()
