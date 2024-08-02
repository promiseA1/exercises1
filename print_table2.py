def print_table():
    print(f"{'a':<5}\t\t{'a**2':<5}\t\t{'a**3':<5}")
    for a in range(5):
        print(f"{a:<5}\t\t{a**2:<5}\t\t{a**3:<5}")

print_table()