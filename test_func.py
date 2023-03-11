from matplotlib import pyplot as plt
import numpy as np
import math


def f_test1(x):
    return x ** 3 + 3 * x ** 2


def f_test2(x):
    return -x ** 3 + 3 * x ** 2


def d2_f_test1(x):
    return 6 * x + 6


def d2_f_test2(x):
    return -6 * x + 6


def setMatrix(N, a, b):
    h = (b - a) / (N - 1)
    Matrix = [[0] * (N) for i in range(N)]

    Matrix[0][0] = 1
    Matrix[N - 1][N - 1] = 1

    for i in range(1, N - 1):
        Matrix[i][i] = 4 * h

    for i in range(1, N - 1):
        Matrix[i][i - 1] = h
        Matrix[i][i + 1] = h

    return Matrix


def setSolveVector1(N, a, b):
    Solve = []
    h = (b - a) / (N - 1)
    x = a + h
    Solve.append(6 * d2_f_test1(a))
    for i in range(N - 2):
        Solve.append(6 * ((f_test1(x + h) - f_test1(x)) / h - (f_test1(x) - f_test1(x - h)) / h))
        x += h
    Solve.append(6 * d2_f_test1(b))

    return Solve


def setSolveVector2(N, a, b):
    Solve = []
    h = (b - a) / (N - 1)
    x = a + h
    #Solve.append(6 * d2_f_test2(a))
    Solve.append(0)
    for i in range(N - 2):
        Solve.append(6 * ((f_test2(x + h) - f_test2(x)) / h - (f_test2(x) - f_test2(x - h)) / h))
        x += h
    #Solve.append(6 * d2_f_test2(b))
    Solve.append(0)

    return Solve


def setSystem1(N, a, b):
    M = setMatrix(N, a, b)
    V = setSolveVector1(N, a, b)

    Matrix = [[0] * (N + 1) for i in range(N)]

    for i in range(N):
        for j in range(N):
            Matrix[i][j] = M[i][j]

    j = 0
    while j < N:
        Matrix[j][-1] = V[j]
        j += 1

    return Matrix


def setSystem2(N, a, b):
    M = setMatrix(N, a, b)
    V = setSolveVector2(N, a, b)

    Matrix = [[0] * (N + 1) for i in range(N)]

    for i in range(N):
        for j in range(N):
            Matrix[i][j] = M[i][j]

    j = 0
    while j < N:
        Matrix[j][-1] = V[j]
        j += 1

    return Matrix


def progonka_forward(matrix, N):
    List_alpha = []
    List_beta = []
    y = matrix[0][0]
    List_alpha.append(-matrix[0][1] / y)
    List_beta.append(matrix[0][-1] / y)
    for i in range(1, N):
        y = matrix[i][i] + matrix[i][i - 1] * List_alpha[i - 1]
        List_alpha.append(-matrix[i][i + 1] / y)
        List_beta.append((matrix[i][-1] - matrix[i][i - 1] * List_beta[i - 1]) / y)

    return List_alpha, List_beta


def progonka_reverse(matrix, N):
    List_alpha = progonka_forward(matrix, N)[0]
    List_beta = progonka_forward(matrix, N)[1]
    List_v = []
    List_alpha.pop(-1)
    List_alpha.reverse()
    List_beta.reverse()
    List_v.append(List_beta[0])
    for i in range(N - 1):
        List_v.append(List_alpha[i] * List_v[i] + List_beta[i + 1])
    List_v.reverse()
    return List_v


def GetCoefficients1(n, a, b):
    List_a = []
    List_b = []
    List_c = []
    List_d = []
    matrix = setSystem1(n + 1, a, b)
    h1 = (b - a) / n

    for i in range(n + 1):
        List_c.append(progonka_reverse(matrix, n + 1)[i])

    x0 = a
    for i in range(n + 1):
        List_a.append(f_test1(x0))
        x0 += h1

    for i in range(1, n + 1):
        List_d.append((List_c[i] - List_c[i - 1]) / h1)

    for i in range(1, n + 1):
        List_b.append((List_a[i] - List_a[i - 1]) / h1 + List_c[i] * (h1 / 3) + List_c[i - 1] * (h1 / 6))

    return List_a, List_b, List_c, List_d


def GetCoefficients2(n, a, b):
    List_a = []
    List_b = []
    List_c = []
    List_d = []
    matrix = setSystem2(n + 1, a, b)
    h1 = (b - a) / n

    for i in range(n + 1):
        List_c.append(progonka_reverse(matrix, n + 1)[i])

    x0 = a
    for i in range(n + 1):
        List_a.append(f_test2(x0))
        x0 += h1

    for i in range(1, n + 1):
        List_d.append((List_c[i] - List_c[i - 1]) / h1)

    for i in range(1, n + 1):
        List_b.append((List_a[i] - List_a[i - 1]) / h1 + List_c[i] * (h1 / 3) + List_c[i - 1] * (h1 / 6))

    return List_a, List_b, List_c, List_d


def createSpline1(n, a, b):
    List_S = []
    List_F = []

    List_x = []

    List_dF = []
    List_d2F = []
    List_dS = []
    List_d2S = []

    List_r = []
    List_dr = []
    List_d2r = []

    h1 = (b - a) / n
    # x0 = a + h1

    x0 = a
    List_a = GetCoefficients1(n, a, b)[0]
    List_b = GetCoefficients1(n, a, b)[1]
    List_c = GetCoefficients1(n, a, b)[2]
    List_d = GetCoefficients1(n, a, b)[3]

    List_X = []

    List_X.append(x0)
    for i in range(n):
        List_x.append(np.linspace(x0, x0 + h1, 10))
        x0 += h1
        List_X.append(x0)
    # x0 = 2
    x0 = a + h1
    for i in range(1, n + 1):
        List_S.append(List_a[i] + List_b[i - 1] * (List_x[i - 1] - x0) + (List_c[i] / 2) * (List_x[i - 1] - x0) ** 2 + (
                List_d[i - 1] / 6) * (List_x[i - 1] - x0) ** 3)
        List_F.append(f_test1(List_x[i - 1]))

        List_dS.append(
            List_b[i - 1] + List_c[i] * (List_x[i - 1] - x0) + (List_d[i - 1] / 2) * (List_x[i - 1] - x0) ** 2)
        List_d2S.append(List_c[i] + List_d[i - 1] * (List_x[i - 1] - x0))

        List_dF.append(3 * List_x[i - 1] ** 2 + 6 * List_x[i - 1])
        List_d2F.append(d2_f_test1(List_x[i - 1]))
        x0 += h1

    # for i in range(1, n + 1):
    # List_F.append((List_x[i - 1] ** 2 - 1) ** (1 / 2) / List_x[i - 1])

    for i in range(n):
        List_r.append(abs(List_F[i] - List_S[i]))
        List_dr.append(abs(List_dS[i] - List_dF[i]))
        List_d2r.append(abs(List_d2S[i] - List_d2F[i]))

    return List_S, List_F, List_r, List_x, List_dS, List_d2S, List_dF, List_d2F, List_dr, List_d2r, List_X

def createSpline2(n, a, b):
    List_S = []
    List_F = []

    List_x = []

    List_dF = []
    List_d2F = []
    List_dS = []
    List_d2S = []

    List_r = []
    List_dr = []
    List_d2r = []

    h1 = (b - a) / n
    # x0 = a + h1

    x0 = a
    List_a = GetCoefficients2(n, a, b)[0]
    List_b = GetCoefficients2(n, a, b)[1]
    List_c = GetCoefficients2(n, a, b)[2]
    List_d = GetCoefficients2(n, a, b)[3]

    List_X = []

    List_X.append(x0)
    for i in range(n):
        List_x.append(np.linspace(x0, x0 + h1, 10))
        x0 += h1
        List_X.append(x0)
    # x0 = 2
    x0 = a + h1
    for i in range(1, n + 1):
        List_S.append(List_a[i] + List_b[i - 1] * (List_x[i - 1] - x0) + (List_c[i] / 2) * (List_x[i - 1] - x0) ** 2 + (
                List_d[i - 1] / 6) * (List_x[i - 1] - x0) ** 3)
        List_F.append(f_test2(List_x[i - 1]))

        List_dS.append(
            List_b[i - 1] + List_c[i] * (List_x[i - 1] - x0) + (List_d[i - 1] / 2) * (List_x[i - 1] - x0) ** 2)
        List_d2S.append(List_c[i] + List_d[i - 1] * (List_x[i - 1] - x0))

        List_dF.append(-3 * List_x[i - 1] ** 2 + 6 * List_x[i - 1])
        List_d2F.append(d2_f_test2(List_x[i - 1]))
        x0 += h1

    # for i in range(1, n + 1):
    # List_F.append((List_x[i - 1] ** 2 - 1) ** (1 / 2) / List_x[i - 1])

    for i in range(n):
        List_r.append(abs(List_F[i] - List_S[i]))
        List_dr.append(abs(List_dS[i] - List_dF[i]))
        List_d2r.append(abs(List_d2S[i] - List_d2F[i]))

    return List_S, List_F, List_r, List_x, List_dS, List_d2S, List_dF, List_d2F, List_dr, List_d2r, List_X


def getdata_testFunc1(N, a, b):
    List_x = createSpline1(N, a, b)[3]
    List_Xy = createSpline1(N, a, b)[10]
    List_s = createSpline1(N, a, b)[0]
    List_f = createSpline1(N, a, b)[1]
    List_r = createSpline1(N, a, b)[2]
    List_dr = createSpline1(N, a, b)[8]
    List_d2r = createSpline1(N, a, b)[9]

    List_df = createSpline1(N, a, b)[6]
    List_d2f = createSpline1(N, a, b)[7]
    List_ds = createSpline1(N, a, b)[4]
    List_d2s = createSpline1(N, a, b)[5]

    List_a = GetCoefficients1(N, a, b)[0]
    List_b = GetCoefficients1(N, a, b)[1]
    List_c = GetCoefficients1(N, a, b)[2]
    List_d = GetCoefficients1(N, a, b)[3]

    List_R = []
    List_dR = []
    List_d2R = []

    List_X = []
    List_S = []
    List_F = []

    List_dF = []
    List_d2F = []
    List_dS = []
    List_d2S = []

    for i in range(N):
        for j in range(9):
            List_X.append(List_x[i][j])
            List_S.append(List_s[i][j])
            List_F.append(List_f[i][j])
            List_R.append(List_r[i][j])
            List_dR.append(List_dr[i][j])
            List_d2R.append(List_d2r[i][j])
            List_dF.append(List_df[i][j])
            List_d2F.append(List_d2f[i][j])
            List_dS.append(List_ds[i][j])
            List_d2S.append(List_d2s[i][j])

    List_R.append(List_r[N - 1][9])
    List_dR.append(List_dr[N - 1][9])
    List_d2R.append(List_d2r[N - 1][9])

    List_X.append(List_x[N - 1][9])
    List_S.append(List_s[N - 1][9])
    List_F.append(List_f[N - 1][9])
    # List_R.append(List_r[N - 1][9])
    # List_dR.append(List_dr[N - 1][9])
    # List_d2R.append(List_d2r[N - 1][9])
    List_dF.append(List_df[N - 1][9])
    List_d2F.append(List_d2f[N - 1][9])
    List_dS.append(List_ds[N - 1][9])
    List_d2S.append(List_d2s[N - 1][9])

    return List_X, List_S, List_F, List_dS, List_dF, List_d2S, List_d2F, List_R, List_dR, List_d2R, List_a, List_b, List_c, List_d, List_Xy

def getdata_testFunc2(N, a, b):
    List_x = createSpline2(N, a, b)[3]
    List_Xy = createSpline2(N, a, b)[10]
    List_s = createSpline2(N, a, b)[0]
    List_f = createSpline2(N, a, b)[1]
    List_r = createSpline2(N, a, b)[2]
    List_dr = createSpline2(N, a, b)[8]
    List_d2r = createSpline2(N, a, b)[9]

    List_df = createSpline2(N, a, b)[6]
    List_d2f = createSpline2(N, a, b)[7]
    List_ds = createSpline2(N, a, b)[4]
    List_d2s = createSpline2(N, a, b)[5]

    List_a = GetCoefficients2(N, a, b)[0]
    List_b = GetCoefficients2(N, a, b)[1]
    List_c = GetCoefficients2(N, a, b)[2]
    List_d = GetCoefficients2(N, a, b)[3]

    List_R = []
    List_dR = []
    List_d2R = []

    List_X = []
    List_S = []
    List_F = []

    List_dF = []
    List_d2F = []
    List_dS = []
    List_d2S = []

    for i in range(N):
        for j in range(9):
            List_X.append(List_x[i][j])
            List_S.append(List_s[i][j])
            List_F.append(List_f[i][j])
            List_R.append(List_r[i][j])
            List_dR.append(List_dr[i][j])
            List_d2R.append(List_d2r[i][j])
            List_dF.append(List_df[i][j])
            List_d2F.append(List_d2f[i][j])
            List_dS.append(List_ds[i][j])
            List_d2S.append(List_d2s[i][j])

    List_R.append(List_r[N - 1][9])
    List_dR.append(List_dr[N - 1][9])
    List_d2R.append(List_d2r[N - 1][9])

    List_X.append(List_x[N - 1][9])
    List_S.append(List_s[N - 1][9])
    List_F.append(List_f[N - 1][9])
    # List_R.append(List_r[N - 1][9])
    # List_dR.append(List_dr[N - 1][9])
    # List_d2R.append(List_d2r[N - 1][9])
    List_dF.append(List_df[N - 1][9])
    List_d2F.append(List_d2f[N - 1][9])
    List_dS.append(List_ds[N - 1][9])
    List_d2S.append(List_d2s[N - 1][9])

    return List_X, List_S, List_F, List_dS, List_dF, List_d2S, List_d2F, List_R, List_dR, List_d2R, List_a, List_b, List_c, List_d, List_Xy