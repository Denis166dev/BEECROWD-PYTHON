C,Q,R = map(int, input().split())

if C*R <= Q or C*R < Q:
    print('S')
else:
    print('N')