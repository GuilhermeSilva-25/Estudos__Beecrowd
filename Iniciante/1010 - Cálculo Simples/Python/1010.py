c1, q1, v1 = input().split()
c2, q2, v2 = input().split()
c1 = int(c1)
q1 = int(q1)
v1 = float(v1)
c2 = int(c2)
q2 = int(q2)
v2 = float(v2)


def valor(a, b, c, d):
    print(f"VALOR A PAGAR: R$ {(a * b) + (c * d):.2f}")


valor(q1, v1, q2, v2)
