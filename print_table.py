def print_table():
    print(f"{'a':<5}\t\t{'a**2':<7}\t\t{'a**3':<7}")

    for a in range(1 , 5):
        print(f"{a:<5}\t\t{a**2:<7}\t\t{a**3:<7}")

print_table() 