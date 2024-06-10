import functools
import inspect

def log_types_of_params(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs): 
        signature = inspect.signature(func)
        paramNames = [name for name in signature.parameters.keys()]
        argTypes = [type(arg).__name__ for arg in args]
        kwargTypes = [type(kwargs[kwarg]).__name__ for kwarg in kwargs]
        
        nameTypesDict = dict(zip(paramNames, [*argTypes, *kwargTypes]))
        print(nameTypesDict)
        
        return func(*args, **kwargs)
    return wrapper

@log_types_of_params
def test(num, text, set, go=True):
    print(num)
    print(go)
    print('test function')  
    
test(1, 'hello', set() , go=False)