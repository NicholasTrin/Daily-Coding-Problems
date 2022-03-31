# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Concept of closure in layered scopes, they retain data for future calls to it's sub-functions.
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair)->int:
    def first_digit(a, b):
        return a
    return pair(first_digit)


def cdr(pair)->int:
    def last_digit(a, b):
        return b
    return pair(last_digit)

def main():
    test = cons(3, 4)
    print(car(test))
    print(cdr(test))

if __name__ == "__main__":
    main()


