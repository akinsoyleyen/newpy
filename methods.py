#methods are pretty much the same thing as functions only thing is that it is a called on a value.
#example

spam = ['h', 'a', 'b']
#index method
spam.index('h')
print(spam.index("h"))
#append method
spam.append('a')
print(spam)
#insert method
spam.insert(1, 'x')
print(spam)
#remove method
spam.remove('x')
print(spam)
#sort method
spam.sort()
print(spam)
#sort methods revers
spam.sort(reverse=True)
print(spam)