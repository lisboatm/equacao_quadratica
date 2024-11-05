# Determinação de Soluções Racionais ou Irracionais de uma Equação Quadrática

Este programa recebe os coeficientes de uma equação quadrática da forma \(Ax^2 + Bx + C = 0\) e determina se suas soluções são racionais ou irracionais.

## Funcionalidade

O código verifica se o discriminante da equação quadrática, dado por \(D = B^2 - 4AC\), é um número perfeito (ou seja, se possui uma raiz quadrada inteira). Se o discriminante for um número perfeito, as soluções são racionais; caso contrário, são irracionais.

## Entrada

O programa aceita uma única linha de entrada contendo três inteiros:
- **A**: Coeficiente do termo quadrático (A ≠ 0)
- **B**: Coeficiente do termo linear
- **C**: Termo constante

As condições para os coeficientes são:
- \(-10^9 < A, B, C < 10^9\)

## Saída

A saída do programa consiste em uma única letra:
- **'Y'**: se as soluções da equação são racionais
- **'N'**: se as soluções são irracionais

## Exemplo de Uso

### Entrada:
```
1 0 -4
```
### Saída:
```
Y
```

### Entrada:
```
1 4 1
```
### Saída:
```
N
```

### Entrada:
```
0 0 1
```
### Saída:
```
Y
```

## Como Executar

1. Certifique-se de que você tenha Python 3.x instalado em sua máquina.
2. Salve o código em um arquivo, por exemplo, `solucao_quadratica.py`.
3. Execute o programa usando o comando:

   ```bash
   python solucao_quadratica.py
   ```

4. Insira os coeficientes quando solicitado.

## Licença

Este projeto é licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.
