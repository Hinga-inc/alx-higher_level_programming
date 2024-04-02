#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    except Exception as e:
        result = None
        print(f"Oups, an error occured: {e}")
    finally:
        if result is not None:
            print("Inside result: {:.1f}".format(result))
        else:
            print("Inside result: None")
        return result
