# Atomic Add
import copy


class Pointer():
    def __init__(self, value:int):
        "Dummy pointer class"
        self.value = value

    def __str__(self):
        return f"Pointer({self.value})"

    # Add ops
    def __add__(self, operand):
        # Add number via: instance + value
        # i.e., an int + instance of this class with + operator
        return Pointer(operand+self.value)

    def __iadd__(self, operand):
        # Add in-place, i.e., update class' value
        self.value += operand
        return self

    def __radd__(self, operand):
        # Add number via: value + instance
        #  same as __add__ but ordering is different,
        #  for simplicity, we return a new object but we could return an int
        return Pointer(operand+self.value)

    # same thing for 


def atomic_add(result, operand) -> int:
    """
    Args:
        result: variable that is modified such that
            result = result + operand
        operand: value to add to result
    Return:
        the old value of "result"
    """
    old = copy.deepcopy(result)
    result += operand
    return old


def main():
    #s = Pointer(100)
    s = Pointer(25)
    print('starting s:', s)

    a = atomic_add(s, 10)
    print('s:', s)
    print('a:', a)

    #b = atomic_add(s, 20)
    b = atomic_add(s, 25)
    print('s:', s)
    print('b:', b)

    print('a+b:', a+b)

if __name__ == "__main__":
    main()
