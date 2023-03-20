import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# 传递原始字符串：前面加r
# \\d -> \d   \d表示数字
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())
# group()方法返回实际匹配文本的字符串

bracketRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# 使用()对字符串进行分组
mo = bracketRegex.search('My number is 415-555-4242')
print('Area code: ' + mo.group(1))
print('Main number: ' + mo.group(2))
# group(n)返回匹配文本的第n组字符串
areaCode, mainNumber = mo.groups();
# groups() 向多个变量分配各组字符串
print(areaCode + '-' + mainNumber)

regexBrackets = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
# 处理含括号的字符串，需要反斜杠转义    ( ---> \(      ) ---> \)
mo = regexBrackets.search('My number is (415) 555-4242')
print(mo.group(1) + mo.group(2))

# 用管道匹配多个分组，优先匹配第一个
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())

# findall(): 返回所有匹配的字符串，返回值为列表
mo2 = heroRegex.findall('Batman and Tina Fey')
print(mo2)

# 管道匹配多个模式，并作为正则表达式的一部分
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))
# group()返回整个匹配字符串，group(1)返回第一个括号内的匹配字符串

# 用问号实现可选匹配
batRegex = re.compile(r'Bat(wo)?man')
# (wo)?表示wo可有可无
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())