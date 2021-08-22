while True:
    try:
        N = int(input())
        mat = []
        for i in range(0, N):
            mat.append([])
            for j in range(0, N):
                mat[i].append('3')
            col_1 = N - 1
        for i in range(0, N):
            mat[i][i] = '1'
            mat[i][col_1] = '2'
            col_1 -= 1
            resultado = ''.join(mat[i])
            print(resultado)
    except EOFError:
        break