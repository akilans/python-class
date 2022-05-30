'''
from my_module import say_hello_with_name as say

print(say("Akilan"))
#greeting = say_hello_with_name("Akilan")
# print(greeting)
'''


import my_module

print(my_module.say_hello())
greeting = my_module.say_hello_with_name("Python")
print(greeting)
full_name, name_length = my_module.get_full_name("Akilan", "Subramanian")
print(full_name, name_length)
'''
import sys
print(sys.path)
'''
