import sys

raw = sys.stdin.read()

lines = len(raw.splitlines())
words = len(raw.split())
chars = len(raw)

print(lines, words, chars)