# resource ; https://towardsdatascience.com/12-beginner-concepts-about-type-hints-to-improve-your-python-code-90f1ba0ac49

# basis notation

# <variable_name> : <variable:type> = <varialbe_value>

## func

def add_things(x : int , y : int , z : int = 100)-> int:
    return print(x + y + z)

add_things(100, 200)

## class

class Phone(object):
    color : str = 'black'
    manu : str = 'Samsung'
    size : int = 100
    def __init__(self):
        color = self.color
        manu = self.manu
        size = self.size

Phone_func = Phone()
print(Phone_func.color)


## list

from typing import List

def float_sum(l : list[float]):
    return print(sum(l))

a = [0.1 , 0.3, 0.5]
float_sum(a)

## dict

from typing import Dict
from collections import defaultdict

jd = defaultdict(str)
#jd = Dict[str , str]

jd['company'] = 'nexon'
jd['graph'] = 'bitnine'
print(jd)

## union
# pass

## TypedDict

from typing import TypedDict , List

class myDictType(TypedDict):
    name : str
    interests : List['str']

d1 : myDictType = {'name':'jit', 'interests' : ['coding','paper_reading']}
d2 : myDictType = {'name':'kyr', 'interests' : 'pray'}

print(d1)
print(d2)

## Callable

from typing import Callable

def sum_thing(x: int, y:int)->int:
    return x+y

def foo(x:int, y:int, func:Callable[[int, int],int])->int:
    output = func(x,y)
    return output

result = foo(100,100,sum_thing)
print(f'foo result , {result}')

## sequence

#An object of type Sequence is anything that can be indexed: a list, a tuple, a string, a list of objects, a tuple of lists of tuples, etc.

## tuple

# pass