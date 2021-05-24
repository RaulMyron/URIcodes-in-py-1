N1, N2, N3, N4 = map(float, input().split())

MEDIA = (((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1)) / 10)

print("Media: %.1f" % MEDIA)

if MEDIA >= 7:
    print("Aluno aprovado.")

elif MEDIA < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")

    N5 = float(input())

    print('Nota do exame: %.1f' % N5)

    MEDIAF = (MEDIA + N5) / 2

    if MEDIAF >= 5:
        print("Aluno aprovado.")

    else:
        print("Aluno reprovado.")
    print("Media final: %.1f" % MEDIAF)

