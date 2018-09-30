# this is the first comment
# this is the second one

'''
third
four
'''

"""
5
six
"""
string = r"this is a line with \n"
word = 'string'
sentence = "This is a sentence"
paragraph = """This is a paragraph,
                which comprises of several lines"""

print("Hello, Python!" + string)

#####################################
py = 'Python'

print(py)  # output the string
print(py[0:-1])  #
print(py[0])  #
print(py[2:5])  #
print(py[2:])  #
print(py * 2)  #
print(py + 'hello')#
print('------------------------------')
print('hello\npython')  #
print(r'hello\npython')  #

#######################################
if __name__ == "__main__":
    from sys import stdin,stdout
    name = stdin.readline()

    stdout.write('hello,'+name)

#######################################
    a, b, c, d = 20, 5.5, True, 4 + 3j
    print(type(a), type(b), type(c), type(d))

#######################################
# The elements in a list can be modified, but not in a tuple
# the type of element in a list, tuple, set and dictionary can be different from others
list_a = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tup1 = ()    # empty tuple
tup2 = (20,) # a tuple includes one element, there must be a comma at the end of this element
set_a = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
dict_a = {'name': 'python','code':1, 'site': 'www.python.com'}