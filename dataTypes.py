"""this fuction determins if the kind of data passedto it is a list, none, boolean less than or greater than 100 and returns the appropriate
response"""
try:
    def dataType(arg):
        
        if isinstance(arg, bool):
            return arg
        elif isinstance(arg, basestring):
            return len(arg)
        elif isinstance(arg, int):
            if dataType < 100:
                return "less than 100"
            elif arg > 100:
                return "more than 100"
            else:
                return "equal to 100"
        elif isinstance(arg, list):
            try:
                return arg[2]
            except IndexError:
                return None
        else:
            return "no value"
except IOError:
    print("your cases can not be handled")

finally:
    print("code execution completed")