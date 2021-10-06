def is_triangle(a, b, c):
    if (a + b) > c:
        print('Yes')
    else:
        print('No')

def triangle():
    a = int(input('Enter a value for side a:'))
    b = int(input('Enter a value for side b:'))
    c = int(input('Enter a value for side c:'))
    is_triangle(a, b, c)

triangle()
