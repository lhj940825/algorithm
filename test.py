'''
 * User: Hojun Lim
 * Date: 2020-04-10
'''

"""
def yieldtest():
    yield (1,2,3,4)



a =yieldtest()
for i in a:
    print(i)

#print(a)
print(list(a))
"""

def test():
    return (1,2,3,4)

def yieldtest(g):
    print(g)
    for i in g:
        yield i

b = test()
a = yieldtest(b)
#print(list(a))


for j in range(5):
    for i in yieldtest(b):
        print(i)

#print(a)
#print(list(a))