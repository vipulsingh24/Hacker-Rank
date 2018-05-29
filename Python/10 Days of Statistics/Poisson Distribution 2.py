def poisson_expect(lamb):
    result = lamb + lamb ** 2
    return result
    
n = [float(x) for x in input().split()]

# Expected daily cost of machine A
C_A = 160 + 40 * poisson_expect(n[0])

# Expected daily cost of machine B
C_B = 128 + 40 * poisson_expect(n[1])

print('%.3f' % C_A)
print('%.3f' % C_B)
