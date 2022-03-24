# cache function
def cache(times):
    def mind(func):
        def memory():
            memory.count += 1  # counts how many times the cache function has been requested
            if memory.count == 1 or memory.count > times + 1:  # start and end conditions
                memory.x = func() # we write a hash to memory
                memory.count = 1 # for reset the counter
            else:
                print(memory.x) # output the cache value

        # defining variables
        memory.x = '' # for the record cache
        memory.count = 0 # to count calls to the function
        return memory

    return mind


@cache(times=3)  # a parametrized decorator, you can change times
def f():
    return input('? ')


f()
f()
f()
f()
f()
f()
f()
f()
f()
f()