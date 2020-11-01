def print_reverse(num):
    n1 = num % 10
    n2 = (num // 10) % 10
    n3 = (num // 100) % 10
    n4 = (num // 1000) % 10
    print((n1 * 1000) + (n2 * 100) + (n3 * 10) + (n4))

def return_reverse(num):
    n1 = num % 10
    n2 = (num // 10) % 10
    n3 = (num // 100) % 10
    n4 = (num // 1000) % 10
    return((n1 * 1000) + (n2 * 100) + (n3 * 10) + (n4))
