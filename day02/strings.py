
str1 = 'hello, world!'
print('字符串的长度：', len(str1))
print('字符串首字母大写：', str.title(str1))
print('字符串大写：', str.upper(str1))

print('字符串是不是大写：', str.isupper(str1))
print('字符是不是hello开头', str1.startswith('hello'))
print('字符是不是hello结尾：', str1.endswith('hello'))
print('字符串是不是！开始：', str1.startswith('!'))
print('字符串是不是！结尾', str1.endswith('!'))

str2 = '- \u9a86\u660a'
str3 = str1.title() + ' ' + str2.lower()
print(str3)

