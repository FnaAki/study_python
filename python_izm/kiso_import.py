
#testmodをimportしている場合
import testmod
 
test_class_1 = testmod.TestClass()
test_class_1.test_method('1')
 
#testmodの「TestClass」をimportした場合
from testmod import TestClass
 
test_class_2 = TestClass()
test_class_2.test_method('2')

#別名インポート
from testmod import TestClass as T
 
test_class_2 = T()
test_class_2.test_method('2')