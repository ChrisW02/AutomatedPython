import re

phoneNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# 传递原始字符串：前面加r
# \\d -> \d
mo=phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: '+mo.group())
# group()方法返回实际匹配文本的字符串

bracketRegex=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# 使用()对字符串进行分组
mo=bracketRegex.search('My number is 415-555-4242')
print('Area code: '+mo.group(1))
print('Main number: '+mo.group(2))
# group(n)返回匹配文本的第n组字符串
areaCode, mainNumber = mo.groups();
# groups() 向多个变量分配各组字符串
print(areaCode+'-'+mainNumber)

regexBrackets = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
# 处理含括号的字符串，需要反斜杠转义 '('to'\('   ')'to'\)'
mo=regexBrackets.search('My number is (415) 555-4242')
print(mo.group(1)+mo.group(2))

heroRegex=re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())