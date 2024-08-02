"""def approximate_pi(pi_1 , pi_2):
    return f"pi_1 is {pi_1:.2f} and pi_2 is {pi_2:.2f}"

pi_1 = 4 * (1 - 1 / 3 + 1 / 5 - 1 / 7 + 1 / 9 - 1 / 11 )
pi_2 = 4 * (1 - 1 / 3 + 1 / 5 - 1 / 7 + 1 / 9 - 1 / 11 + 1 / 13 - 1 / 15)
print(approximate_pi(pi_1 , pi_2))"""

def approximate_pi_formula1():
    pi = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11)
    return pi

def approximate_pi_formula2():
    pi = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + 1/13 - 1/15)
    return pi

pi_approximation1 = approximate_pi_formula1()
print(f"Approximation of pi using formula 1:  {pi_approximation1:.6f}")


pi_approximation2 = approximate_pi_formula2()
print(f"Approximation of pi using formula 2:  {pi_approximation2:.6f}")