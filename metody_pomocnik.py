

def nazwa_metody():
    print('Nazwa metody!')

def hello_world(name):
    print(f'Hello {name}')

def add(a:int,b:int):
    print(f'A = {a}; B = {b}')
    suma = a + b
    print(f'Suma = {suma}')

def add_two(a:int,b:int)->int:
    """
    Add two numbers and give in back sum of a+b
    :param a: 
    :param b: 
    :return: int 
    """
    suma = a + b
    return suma

nazwa_metody()


hello_world('Jonas')

add(1,2)

print(add_two(3,4))




