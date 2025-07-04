a=10
c=2211
g=c//1000+a
def check_guess(secret:int):
    guess=int(input("Sonni toping "))
    return secret==guess
def print_result(is_correct):
    if is_correct:
        return True
    else:
        return f"Xato tog`ri javob {g}"
    pass
natija=check_guess(g)
print(print_result(natija))