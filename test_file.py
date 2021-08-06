# file = open('test_file.txt','w')
# file.write('诸葛亮')
# file.close()

# filer = open('test_file.txt','r')
# for line in filer.readlines():
#     print(line,'<br/>')
#
# filer.close()

# files = open('test_file.txt')
# print(files.tell())
#
# a = 'linyi'
# print('我来了%s'%a)

file6 = open('test_file.txt','r')
print(file6.tell())
print(file6.read(2))
print(file6.tell())
file6.seek(0)
print(file6.read(2))
print(file6.tell())
