import sys
import string

S = input()

for i in string.ascii_lowercase:
    print(S.find(i), end=" ")
