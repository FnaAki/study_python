
#[＜開始位置＞：＜終了位置＞：＜ステップ幅＞]
test_list = ['https', 'www', 'python', 'izm', 'com']
 
print(test_list[:])
print(test_list[::])


test_list = ['https', 'www', 'python', 'izm', 'com']
 
print(test_list[:4])

test_list = ['https', 'www', 'python', 'izm', 'com']
 
print(test_list[2:])

test_list = ['https', 'www', 'python', 'izm', 'com']
 
print(test_list[3:5])

test_list = ['https', 'www', 'python', 'izm', 'com']
 
print(test_list[-1:])   # 末尾から全ての要素
print(test_list[:-1])   # 末尾まで全ての要素
print(test_list[::-1])  # 末尾から全ての逆順要素

test_list = ['https', 'www', 'python', 'izm', 'com']
 
print(test_list[:999])

test_list = ['https', 'www', 'python', 'izm', 'com']
 
test_list[1:3] = ('WWW', 'PYTHON')
 
print(test_list)