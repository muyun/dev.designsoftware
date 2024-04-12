#ch8  - Functions and Closures
# 
# 1. Functions is an object just data, we can separate creation from naming
#     - how definition works
#
# 2. closures are functions with data attached;  objects are data with methods attached  
#     - closure is the it captures the context, the local vriables and so on  
#     - the new lexically scoped kind of procedure  
#

# function is an object which has parameters and body 
# function definition and storage
#   - a function has a name or anonymous, a list of parameters, and a body
def do_func(env, args):
    assert len(args) == 2
    params = args[0]
    body = args[1]
    return ["func", params, body] #storage

# call
#   - look up the function
#   - create a new env from the func's parameter names and the expressions' values
#   - call do_func to run the function's action and capture the result
#   - discard the env
#   - return the fun's result
#
def do_call(env, args):
    return


# 3. closures are functions with data attached  
def make_object(initial_value):
    private = {'value': initial_value}

    def getter():
        return private["value"]

    def setter(new_value):
        private["value"] = new_value

    return {"get": getter, "set": setter}


def main():
    object = make_object(0)
    print("initial value", object["get"]())
    object["set"](99)
    print("object now contains", object["get"]())

if __name__ == '__main__':
    main()