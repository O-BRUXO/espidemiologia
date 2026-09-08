import os
import numpy as np
import matplotlib.pyplot as plt


def grafico(beta, gamma, tempo, natalidade, mortalidade):

    dt = 0.5

    # Tempo característico
    t_c = tempo * 2

    # Tempo máximo da simulação
    D_max = 50

    t = np.arange(0, D_max, dt)

    # ==========================================================
    # Inicialização
    # ==========================================================

    N = np.zeros(len(t))
    S = np.zeros(len(t))
    I = np.zeros(len(t))

    Nasc = np.zeros(len(t))
    Mort = np.zeros(len(t))

    # Solução analítica
    Nan = np.zeros(len(t))
    San = np.zeros(len(t))
    Ian = np.zeros(len(t))

    # ==========================================================
    # Condições iniciais
    # ==========================================================

    N[0] = 1

    # 1% da população infectada
    I[0] = 0.01

    # Restante da população suscetível
    S[0] = N[0] - I[0]

    Nasc[0] = natalidade
    Mort[0] = mortalidade

    # Taxa líquida
    U = Nasc[0] - Mort[0]

    # ==========================================================
    # Condições iniciais da solução analítica
    # ==========================================================

    Nan[0] = 1
    Ian[0] = 0.01
    San[0] = Nan[0] - Ian[0]

    # ==========================================================
    # Método de Euler + Solução Analítica
    # ==========================================================

    for i in range(len(t) - 1):

        # Equações diferenciais
        dS = -beta * S[i] * I[i] + U * (1 - S[i])
        dI = beta * S[i] * I[i] - U * I[i]

        # Método de Euler
        S[i + 1] = S[i] + dS * dt
        I[i + 1] = I[i] + dI * dt

        # ------------------------------------------------------
        # Solução analítica
        # ------------------------------------------------------

        e = np.exp(-(beta - U) * t[i + 1])

        denominador_s = (
            beta * (1 - San[0])
            + (beta * San[0] - U)
        )

        San[i + 1] = (
            U * (1 - San[0])
            + (beta * San[0] - U) * e
        ) / denominador_s

        denominador_i = (
            beta * Ian[0]
            + (beta - U - beta * Ian[0]) * e
        )

        Ian[i + 1] = (
            Ian[0] * (beta - U)
        ) / denominador_i

    # ==========================================================
    # Gráfico
    # ==========================================================

    plt.figure(figsize=(10, 6))

    plt.plot(
        t,
        S,
        color='blue',
        linestyle='dashed',
        label='Suscetíveis',
        lw=2
    )

    plt.plot(
        t,
        I,
        color='red',
        linestyle='dashed',
        label='Infectados',
        lw=2
    )

    plt.plot(
        t,
        San,
        color='blue',
        label='Suscetíveis - Sol. Analítica',
        lw=2
    )

    plt.plot(
        t,
        Ian,
        color='red',
        label='Infectados - Sol. Analítica',
        lw=2
    )

    # Informações na legenda
    plt.plot(
        0, 0,
        color='none',
        label=f'β = {beta}'
    )

    plt.plot(
        0, 0,
        color='none',
        label=f'U = {U}'
    )

    plt.plot(
        0, 0,
        color='none',
        label=f'γ = {gamma}'
    )

    plt.plot(
        0, 0,
        color='none',
        label=f'T_c = {t_c / 2} dias'
    )

    plt.grid(True)

    plt.legend()

    plt.xlabel("Dias")
    plt.ylabel("População")
    plt.title("Modelo SIS")

    plt.xlim([-0.01, 50.5])
    plt.ylim([-0.01, 1.1])

    # ==========================================================
    # Salvar gráfico
    # ==========================================================

    caminho = os.path.join(
        "static",
        "img",
        "grafico",
        "grafico.png"
    )

    os.makedirs(
        os.path.dirname(caminho),
        exist_ok=True
    )

    plt.savefig(
        caminho,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()