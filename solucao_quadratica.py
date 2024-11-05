import math

def is_perfect_square(n):
    # Função para verificar se um número é um quadrado perfeito
    if n < 0:
        return False  # Números negativos não podem ser quadrados perfeitos
    root = int(math.isqrt(n))  # Calcula a raiz inteira de n
    return root * root == n  # Retorna True se n é um quadrado perfeito

def main():
    # Função principal que executa a lógica do programa
    A, B, C = map(int, input().split())  # Lê os coeficientes A, B e C

    if A == 0:
        # Para A = 0, a equação não é quadrática. Verifique se B é zero.
        if B == 0:
            # Se B = 0, a equação é C = 0. Solução depende do valor de C.
            print("Y" if C == 0 else "N")  # Se C = 0, solução é verdadeira (0 = 0)
        else:
            # Se B ≠ 0, a equação linear Bx + C = 0 sempre tem solução real.
            print("Y")
    else:
        # Calcula o discriminante da equação quadrática
        discriminant = B * B - 4 * A * C
        # Verifica se o discriminante é um quadrado perfeito
        if is_perfect_square(discriminant):
            print("Y")  # Se for um quadrado perfeito, soluções são racionais
        else:
            print("N")  # Caso contrário, soluções são irracionais

if __name__ == "__main__":
    main()  # Chama a função principal quando o script é executado
