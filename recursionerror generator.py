def recursive_a(a):
    print(a)
    recursive_b(a+1)
def recursive_b(b):
    print(b)
    recursive_a(b+1)
recursive_a(1)
