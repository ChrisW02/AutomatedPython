import numpy as np
import pyperclip

alice = "That is Alice's cat."
bob = "Say hi to Bob\'s mother."
print("Hello there!\nHow are you?\nI\'m doing fine.")
print(r"Hello there!\nHow are you?\nI\'m doing fine.")  # 原始字符串：前面加r

# multiple line string
print('''Dear Alice,

Eve's Cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob
''')

# multiple line comment
'''
This is a multiple line comments.
Thanks.
'''

spam = 'Hello world!'
print(spam[0])
print(spam[:4])
print(spam[-3:])

print(pyperclip.paste())
# pyperclip 从计算机剪贴板收集文本，或copy一个新的文本
spamU = spam.upper()
print(spamU)

spamL = spam.lower()
print(spamL)
print('abc12123'.islower())

# Omit:
# isalpha() [only alpabets], isalnum() [only alpabets and nums],
# isdecimal(), isspace(), istitle() [truely capital]
# startswith(), endswith()

print(','.join(['cats','dogs','rats']))

spam ='''Dear Alice,
Eve's Cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,
Bob'''
print(spam.split('\n'))

print('hello'.rjust(20))
print('hello'.ljust(20,'-'))
print('hello'.rjust(20,'^'))
print('hello'.center(20,'='))