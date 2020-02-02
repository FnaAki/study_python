#タプルとは
import datetime
 
 
def get_today():
 
    today = datetime.datetime.today()
    value = (today.year, today.month, today.day)
 
    return value
 
 
test_tuple = get_today()
 
print(test_tuple)
print(test_tuple[0])
print(test_tuple[1])
print(test_tuple[2])

# 7行目で要素を3つ「 () 」（カッコ）を使用して囲んでいます。
# これでその3要素を保持しているタプルとして作成することができます。
import datetime
 
 
def get_today():
 
    today = datetime.datetime.today()
    value = (today.year, today.month, today.day)
 
    return value
 
 
test_tuple = get_today()
 
print(test_tuple)
print(test_tuple[0])
print(test_tuple[1])
print(test_tuple[2])
 