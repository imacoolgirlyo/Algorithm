from hashlib import sha256

word = input()
print(sha256(word.encode('utf-8')).hexdigest())
