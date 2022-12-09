def sum(a=1,b=1):
    return(a+b)
    
a = int(input('ingresa un primer número: '))
b = int(input('ingresa un segundo número: '))

print(sum(a, b))

print('----------------------------------------------------------------')

def sum_with_range(min, max):
    print(min, max)
    suma = 0
    for x in range(min, max):
        suma += x
    return suma


result = sum_with_range(1, 10)
print(result)
result_2 = sum_with_range(result, result + 10)
print(result_2)


print('----------------------------------------------------------------')

def find_volume(length=1, width=1, depth=1):
    return length * width * depth, length ** 2, width

resultado, lenngth_exp2, width = find_volume(width=10)

print(resultado)
print(lenngth_exp2)
print(width)