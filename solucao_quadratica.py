import math

def is_perfect_square(n):
    if n < 0:
        return False
    root = int(math.isqrt(n))
    return root * root == n

def main():
    A, B, C = map(int, input().split())

    if A == 0:
        # Para A = 0, a equação não é quadrática. Verifique se B é zero.
        if B == 0:
            print("Y" if C == 0 else "N")
        else:
            print("Y")  # A equação linear Bx + C = 0 sempre tem solução real.
    else:
        discriminant = B * B - 4 * A * C
        if is_perfect_square(discriminant):
            print("Y")
        else:
            print("N")

if __name__ == "__main__":
    main()
