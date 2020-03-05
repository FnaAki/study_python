test_set_1 = {'python', '-', 'izm', '.', 'com'}
print(test_set_1)
 
print('--------------------------------')
 
for i in test_set_1:
    print(i)

#要素がない空のセットを作成する時はsetを用います。
## これはディクショナリ
test_dict = {}
 
## これはセット
test_set = {'python'}
 
## 空のセットは「set」を使う
empty_set = set()

#重複していても、1つしか出力されない。
test_set_1 = {'python', '-', 'izm', '.', 'com', 'python', 'izm'}
print(test_set_1)
 
print('--------------------------------')
 
for i in test_set_1:
    print(i)

#単一の要素を追加する時は「add」
#セットやリスト、タプルから要素を追加する場合は「update」
test_set_1 = set()
 
test_set_1.add('python')
test_set_1.update({'-', 'izm', '.', 'com'})
 
print(test_set_1)

#セットから要素を削除する場合は「remove」「discard」を使用する。
#指定した要素がないのに「remove」を使用した場合、エラーとなる。
test_set_1 = {'python', '-', 'izm', '.', 'com'}
 
test_set_1.remove('-')
test_set_1.discard('.')
 
print(test_set_1)

#frozensetは通常のsetのように作成できるが、「remove」や「discard」さらに
# 「add」「update」を行おうとすると「AttributeError」が発生します。
test_set_1 = frozenset({'python', '-', 'izm', '.', 'com'})
 
# test_set_1.remove('-')
# test_set_1.discard('.')
 
print(test_set_1)