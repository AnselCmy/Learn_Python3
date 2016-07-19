# Python Learning Notes
***

## Basis
***
### I/O
1. Using function `input()` to get input, but get the `str`, if want tpye of `int`, need to us int() to transeform the type forcely.  
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
2. Not like in C, the parameter if function in python don't need the type declare, if you want to inspect the type, using the build-in function `isinstance()`
3. The fuction in python can return not only one result, actually, the not-only-one return depend on a tuple, you can use the number-as-the-return variable to get the return, or use one to get the return tuple
4. ***Default parameter*** is tolerable, but you need to pay attention to that parameter is also a variable, if you change this parameter in the function, the function transfered next time will remember the change. like `def AddEnd( l = [] ):` and you change the list l in the  function
5. ***Number-alterable parameter*** can be realized by `*`, if you use `def calc(*number):`, that means the function get a tuple, and the length of this tuple can be alterable by your input when transfer the function
6. To change a list or tuple to be acceptable by number-alterable parameter, us can add a `*` in front of the list or tuple
7. ***Key-parameter declare***can build a new dic for you automatically, and the `**kw` is necessary to declare it is a key-parameter function, like 
    ```python
    def person(name, age, **kw):
        print('name:', name, ',', 'age:', age, ',', 'other:', kw)
    ```  
you can transfer the function like:
    ```python
    person('Ansel', 19, gender='male', city='mianyang')   
    #attention the '=' but not ':'
    ```
or:
    ```python
    extra = {'gender' : 'male', 'city' : 'mianyang'}
    sperson('Ansel', 19, **extra)
    ```
8. Key must be the `str` if you want to operate this dic by key-parameter function.
9. ***Given-name ker-parameter*** means you must give the keyword-arguement contained the arguement list of the function, not more or less
10. A special sign ` *, ` is necessary in front of the keyeord-only argument to declare that after the sign, here are Given-name ker-parameter, furthermore, after a Number-alterable parameter`*`, `*,` is not needed. 

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
6. If we need index-oriented iteration like FOR in C, use `enumerate()` to build a index-value couple, and us two variables, further more, we can also use the `len(` to get a range and use it as the index to loop
7. Two variables in python FOR is common, it can iterate the two demension list

### List Comprehensionss
1, `a = [x*x for x in range(0, 6)]` is a list comprehension to build a list with the element of power from 0 to 5
2. If we need more restrictive condition we can use `if`  like `[x*x for x in range(0, 10) if x%2 == 0]`
3. Two-level loop can also be used in such comprehension
4. Two variables is also common in this comprehension

### Generator