"""
Question:
Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

"""
import zlib
import sys

s = "hello world!hello world!hello world!hello world!"
print(f'Original:{s}, size: {sys.getsizeof(s)}')

a = zlib.compress(s.encode())
print(f'Compressed:{a}, size:{sys.getsizeof(a)}')

d = zlib.decompress(a).decode()
print(f'Decompressed: {d}')