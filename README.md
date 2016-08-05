# Python Learning Notes
***

## Basis
***
### I/O
1. Using function `input()` to get input, but it can only get the `str`, if want the tpye of `int`, need to use int() to transeform the type forcely.  
2. Function `input()` can get parameter of type `str` as the prompt of the input.   
3. Using `print()` to output, furthermore formtted output is tolerable, using `%` to connect the output str and variable.  
4. Using ` '''... ...''' ` can output the str with many rows.
5. The ESC(escape sequence) like `\n`, `\t`  are tolerble.  

### List & Tuple
1. Using bracket like [... ...] to express list, (... ...) to express tuple.  
2. Function `len()`  can get the number of element.
3. Index `[-1]` means the last element.  
4. List is variable, can be appened element by function operation `.append()`.  
5. Operation `.pop()` to delete element, if no parameter, delete the last one; else, get the parameter as the index of delete element.  
6. Tuple is immutable type.
7. List and tuple can be the element of list or tuple, using [...][...] to get such two dimension type.   
8. Not like array in C, not only one type can appear in one list or tuple.  

### Loop
1. Using `for x in range: ` to loop, and the range can be the list, tuple or the function `range(start, stop[, step]) (to make a int list from start to ***stop-1***).
2. `for x in range: ` FOR state in python meas subsituting the x by element in the list in order.

### Dic & Set
1. Type dic(dictionary) store the data by the way of ***key-value*** likes `{'Michael': 95, 'Bob': 75, 'Tracy': 85}`.  
2. Using bracket like {... ...} to express the dic.
3. A list is required to build a set, like `s = set([1, 1, 2, 2, 3, 3])`.
4. Set is just like the assemblage in math, can be operated by `| & ^`

## Funtion
***
1. Using `def` to express a function, never forget the indentation and `:`
2. Not like in C, the parameter of function in python don't need the type declaring, if you want to inspect the type, using the build-in function `isinstance()`
3. The fuction in python can return not only one result, actually, the not-only-one return depend on a tuple, you can use the number-as-the-return variable to get the return, or use one to get the return tuple
4. ***Default parameter*** is tolerable, but you need to pay attention to that parameter is also a variable, if you change this parameter in the function, the function transfered next time will remember the change.
5. ***Number-alterable parameter*** can be realized by `*`, if you use `def calc(*number):`, that means the function get a tuple, and the length of this tuple can be alterable by your input when transfer the function
6. To change a list or tuple to be acceptable by number-alterable parameter, us can add a `*` in front of the list or tuple
7. ***Key-parameter declare***can build a new dic for you automatically, and the `**kw` is necessary to declare it is a key-parameter function
8. Key must be the `str` if you want to operate this dic by key-parameter function.
9. ***Given-name key-parameter*** means you must give the keyword-arguement contained the arguement list of the function, not more or less
10. A special sign ` *, ` is necessary in front of the keyeord-only argument to declare that after the sign, here are Given-name ker-parameter, furthermore, after a Number-alterable parameter`*`, `*,` is not needed. 
11. The order in parameter list must be, integrant, default, number-alterable, Given-name key, key parameter

## Advanced Features
***
### Slice
1. Slice is a kind of operation of list and tuple to get a special range in them
2. Commonly, we use index like [0:3] to get the elements from 0 to 2(attention: the last indexed element is not inclueded), shortly we use [ :3] to ellipsis the index 0
3. Inverted slice is also supported, for instance, [-3:] means the element [-3] and [-2]
4.  If there are three arguements in the slice, the third one means step.
5. If only one `:` in the bracket, means a copy of this list
6. Type `str` can also be sliced.

### Iteration
1. FOR loop in python is more advanced than that in C or Java, not only list and tuple, but also the dic can be iterated
2. Pay attention that dic is not ordered, so the results everytime are different
3. Defaultly, the iteration element is key in dic, if we need values, using `.values()` to get the valuses
4. If we need to iterate both key and values, us `.items()` to get them.
5. Type `str` can also be iterated
6. If we need index-oriented iteration like FOR in C, use `enumerate()` to build a index-value couple, and us two variables, further more, we can also use the `len()` to get a range and use it as the index to loop
7. Two variables in python FOR is common, it can iterate the two demension list

### List Comprehensions
1. `a = [x*x for x in range(0, 6)]` is a list comprehension to build a list with the element of power from 0 to 5
2. If we need more restrictive condition we can use `if`  like `[x*x for x in range(0, 10) if x%2 == 0]`
3. Two-level loop can also be used in such comprehension
4. Two variables is also common in this comprehension

### Generator
1. Generator is created with (... ...), but not [... ...]

### Iterator
1. We can use isinstance() to check that if this type is Iterator,
2. List, dic and so on are not Iterator, but generator is, we can use iter() to change the type
3. Iterator is the data stream, it will caculate the data by transforming, it can be infinite.

## Function Programing
***
### High-Order Function
1. A variable can point a function, remember not to use the bracket.
2. Function name is actually a name of variable 
3. High-order function means a function can accept a function as the argues 
4. ***Map*** is a fuction can get a function and a Iterable as the argus, and return a Iterator, the Iterator is the result of the Iterable transformed by the function, if we want to use `print()` to print is, use `list()` change the iterator to the iterable
5. ***Reduce*** is also a function to get a function and a Iterable, but the function in argus list must be a funtion get two arguments, it will return a result by  transforming the function one by one in the Iterable
6. ***Filter*** will also act on every elements in a list, and by judge the result is true or false to abandon or hold this element
7. ***Sorted*** can easily sort a list of number, but if you wangt to have more restrictive condition, using the `key=func` , `sorted()` can also get the third arguments as the `reverse=True` to sort reversed

### Return Function
1. If we don't need to get the result of this function immediately, we can return another function, and use a variable to get it, transform it when we need it
2. When we return a function, don't forget that the function is never be transformed, it only remember the algorithm, so if we use a varible, it will be dangerous

### Lambda Function
1. It is just a function expression which can only express some easy fucntion which only has one sentence

### Decorator
1. We don't want to change the function, but need to add some features, we can use decorator 
2. If we need to give argument to the decorator, we need to have a more def function in the `log()`
3. But when we get the `.__name__` of the new `now()` function, the name is wrapper, so we need to copy the attribute of `now()` to the `wrapper()`

### Partial Function
1. Partial function can fix some argument

## Module
***


## OOP
***

### Class & Object
1. After the name of calss is the inherit class, usually we use `object`
2. A function `__init__(self, ... ...)` is necessary to build a new object of a calss
3. Every function must have the `self` to be the first argument

### Visit Restriction
1. If we want such data in class is private, we need to add`__` in front of the data, so, the function out of the class can't change and get the data diretely, only in-class function can do those

### Poly & Inher
1. Inheritance means you can use the function in the ***base calss***
2. Polymorphism means you can redeclare the function in the subclass, but not like c++, we don't need to declare it is a virtual, and even a class which has a function has the same name, we can use the polymorphism.

### Get Info
1. We can use `type()` to get the type of a variable
2. A module 'Types' can judge the function
3. `isinstance()` is function can judge the type
4. We can use the 'dir()' to get the ***method*** and the ***attribute***, 
5. Method and attribute like `__xxx__` are special, like `__len__` in str type, can transformed by `len(str)` or `str.__len__()`
6. `getattr()`, `setattr()`, `hasattr()` can operate the method and attribute, the first argu is a object, and the seconde is the attribute, remember use the type str to express the attribute.

### Attribute in Class and Object
1. As a dynamic language, we can bind a new attribute out of the class for a object, that means we bind a attribute for a object but not a class
2. If we bind a attibute in a class, that means every object of the class has the attribute


## Advanced OOP
***
### __slots__
1. Dynamic language agree that a object can bind a attribute, but if we want to restrict that, using `__slots__ = ('xxx', 'xxx')`, only name in this tuple can be binded

### @property
1. For some safety problems, we usually don't want the attribute can be exposed outside the class, like sometimed we need to check the aruguments, so, we use the build-in decorater @property
2. If we want this attribute is read-only, we can only have `@property` but not `xxx.setter`

### Mixin

### Custom-made Class
1. When we print a class name, we can use `__str__(self):` to rewrite the words we want, when we print it
2. If we want use a class in a FOR loop, we need `__iter__()` and `__next__()`, `__iter__()` will return a Iterable object, the FOR loop in python will transform the `__next__()` in the Iterable object while it occur the StopIteration
3. `__getitem__()` can make class like a list, using the index to get the item.
4. `__call__()` is a function will be transformed which when you transform the objet itself

### Enum

## Error
***
### Error
1. Using `try...except...finally` to find the problems in codes, and we can also use `logging.exception()` to make this run after print the error
2. `raise xxxError()` to raise a error 

### Debug

