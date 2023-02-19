# spam={'color':'red','age':42}
# for v in spam.values():
#     print(v)
# for k in spam.keys():
#     print(k)
# for i in spam.items():
#     print(i)
# print('age' in spam.keys())
#
# # if color does not exist, it will be set to black
# spam.setdefault('color','black')

from pprint import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count={}
for character in message:
    count.setdefault(character,0)
    count[character] = count[character]+1
pprint(count)

