from matplotlib import pyplot as plt
import numpy as np
import math


def f_var10(x):
    return np.cos(np.exp(x))+np.cos(10*x)


def d_f_var10(x):
    return -np.sin(np.exp(x)) * np.exp(x) - 10*np.sin(10*x)


def d2_f_var10(x):
    return -np.cos(np.exp(x)) * np.exp(2 * x) - np.sin(np.exp(x)) * np.exp(x) - 100*np.cos(10*x)


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


def setSolveVector(N, a, b):
    Solve = []
    h = (b - a) / (N - 1)
    x = a + h
    # Solve.append(6 * d2_f_var1(a))
    Solve.append(0)
    for i in range(N - 2):
        Solve.append(6 * ((f_var10(x + h) - f_var10(x)) / h - (f_var10(x) - f_var10(x - h)) / h))
        x += h
    # Solve.append(6 * d2_f_var1(b))
    Solve.append(0)

    return Solve


def setSystem(N, a, b):
    M = setMatrix(N, a, b)
    V = setSolveVector(N, a, b)

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


def GetCoefficients(n, a, b):
    List_a = []
    List_b = []
    List_c = []
    List_d = []
    matrix = setSystem(n + 1, a, b)
    h1 = (b - a) / n

    for i in range(n + 1):
        List_c.append(progonka_reverse(matrix, n + 1)[i])

    x0 = a
    for i in range(n + 1):
        List_a.append(f_var10(x0))
        x0 += h1

    for i in range(1, n + 1):
        List_d.append((List_c[i] - List_c[i - 1]) / h1)

    for i in range(1, n + 1):
        List_b.append((List_a[i] - List_a[i - 1]) / h1 + List_c[i] * (h1 / 3) + List_c[i - 1] * (h1 / 6))

    return List_a, List_b, List_c, List_d


def createSpline(n, a, b):
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
    List_a = GetCoefficients(n, a, b)[0]
    List_b = GetCoefficients(n, a, b)[1]
    List_c = GetCoefficients(n, a, b)[2]
    List_d = GetCoefficients(n, a, b)[3]

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
        List_F.append(f_var10(List_x[i - 1]))

        List_dS.append(
            List_b[i - 1] + List_c[i] * (List_x[i - 1] - x0) + (List_d[i - 1] / 2) * (List_x[i - 1] - x0) ** 2)
        List_d2S.append(List_c[i] + List_d[i - 1] * (List_x[i - 1] - x0))

        List_dF.append(d_f_var10(List_x[i - 1]))
        List_d2F.append(d2_f_var10(List_x[i - 1]))
        x0 += h1

    # for i in range(1, n + 1):
    # List_F.append((List_x[i - 1] ** 2 - 1) ** (1 / 2) / List_x[i - 1])

    for i in range(n):
        List_r.append(abs(List_F[i] - List_S[i]))
        List_dr.append(abs(List_dS[i] - List_dF[i]))
        List_d2r.append(abs(List_d2S[i] - List_d2F[i]))

    return List_S, List_F, List_r, List_x, List_dS, List_d2S, List_dF, List_d2F, List_dr, List_d2r, List_X


def getdata_var10_period(N, a, b):
    List_x = createSpline(N, a, b)[3]
    List_Xy = createSpline(N, a, b)[10]
    List_s = createSpline(N, a, b)[0]
    List_f = createSpline(N, a, b)[1]
    List_r = createSpline(N, a, b)[2]
    List_dr = createSpline(N, a, b)[8]
    List_d2r = createSpline(N, a, b)[9]

    List_df = createSpline(N, a, b)[6]
    List_d2f = createSpline(N, a, b)[7]
    List_ds = createSpline(N, a, b)[4]
    List_d2s = createSpline(N, a, b)[5]

    List_a = GetCoefficients(N, a, b)[0]
    List_b = GetCoefficients(N, a, b)[1]
    List_c = GetCoefficients(N, a, b)[2]
    List_d = GetCoefficients(N, a, b)[3]

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

    List_dF.append(List_df[N - 1][9])
    List_d2F.append(List_d2f[N - 1][9])
    List_dS.append(List_ds[N - 1][9])
    List_d2S.append(List_d2s[N - 1][9])


    return List_X, List_S, List_F, List_dS, List_dF, List_d2S, List_d2F, List_R, List_dR, List_d2R, List_a, List_b, List_c, List_d, List_Xy
