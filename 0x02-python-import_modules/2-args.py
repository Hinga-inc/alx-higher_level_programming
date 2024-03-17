
#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_length = len(sys.argv)
    if arg_length == 1:
        print("{} arguments.".format(arg_length - 1))
    elif arg_length == 2:
        print("{} argument:".format(arg_length - 1))
    else:
        print("{} arguments:".format(arg_length - 1))

    for i in range(1, arg_length):
        print("{}: {}".format(i, sys.argv[i]))
