import matplotlib.pyplot as plt
import numpy as np

# --- Dados fornecidos pelo usuário ---
# Assumindo a convenção:
# Coluna 1 (X1): Tempo (s) - Eixo X
# Coluna 2 (X2): Tensão de Descarga (Descarga_V) - Eixo Y da Descarga
# Coluna 3 (X3): Tensão de Carga (Carga_V) - Eixo Y da Carga

data_string = """
70 1.85 3.15
30572 1.78 3.22
30974 1.71 3.29
31377 1.64 3.36
31779 1.57 3.43
32182 1.52 3.48
32583 1.46 3.54
32986 1.40 3.60
33388 1.34 3.66
33790 1.29 3.71
34193 1.24 3.76
34595 1.19 3.81
34998 1.14 3.86
35400 1.09 3.91
35803 1.06 3.94
36205 1.01 3.99
36608 0.97 4.03
37009 0.93 4.07
37411 0.90 4.10
37814 0.86 4.14
38216 0.83 4.17
38619 0.80 4.20
39021 0.76 4.24
39424 0.73 4.27
39826 0.70 4.30
40228 0.68 4.32
40631 0.65 4.35
41032 0.63 4.37
41435 0.60 4.40
41837 0.58 4.42
42240 0.55 4.45
42642 0.53 4.47
43044 0.51 4.49
43447 0.49 4.51
43849 0.47 4.53
44252 0.45 4.55
44654 0.43 4.57
45057 0.42 4.58
45458 0.40 4.60
45860 0.39 4.61
46263 0.37 4.63
46665 0.36 4.64
47068 0.34 4.66
47470 0.33 4.67
47873 0.32 4.68
48275 0.30 4.70
48677 0.29 4.71
49080 0.28 4.72
49481 0.27 4.73
49884 0.26 4.74
50286 0.25 4.75
50689 0.24 4.76
51091 0.23 4.77
51493 0.22 4.78
51896 0.21 4.79
52298 0.20 4.80
52701 0.20 4.80
53103 0.19 4.81
53506 0.18 4.82
"""

# Processamento dos dados
data_lines = [list(map(float, line.split())) for line in data_string.strip().split('\n') if line.strip()]
data_array = np.array(data_lines).T

# Atribuição das colunas a variáveis com nomes sugestivos
Tempo_s = data_array[0]   # Coluna 1
Descarga_V = data_array[1] # Coluna 2 (Meio)
Carga_V = data_array[2]    # Coluna 3 (Direita)

# --- Criação dos 3 Gráficos ---

# Configura a figura para ter 3 subplots (1 linha, 3 colunas)
fig, axes = plt.subplots(1, 3, figsize=(20, 6)) # Aumentei um pouco o tamanho para melhor visualização

# ----------------------------------------------------
# GRÁFICO 1: Carga (Carga_V vs. Tempo_s)
# ----------------------------------------------------
axes[0].plot(Tempo_s, Carga_V, marker='s', linestyle='-', color='red', markersize=4)
axes[0].set_title('Gráfico 1: Carga (C)')
axes[0].set_xlabel('Tempo (s)')
axes[0].set_ylabel('Tensão de Carga (V)')
axes[0].grid(True, linestyle='--', alpha=0.6)

# ----------------------------------------------------
# GRÁFICO 2: Descarga (Descarga_V vs. Tempo_s)
# ----------------------------------------------------
axes[1].plot(Tempo_s, Descarga_V, marker='o', linestyle='-', color='blue', markersize=4)
axes[1].set_title('Gráfico 2: Descarga (R)')
axes[1].set_xlabel('Tempo (s)')
axes[1].set_ylabel('Tensão de Descarga (V)')
axes[1].grid(True, linestyle='--', alpha=0.6)

# ----------------------------------------------------
# GRÁFICO 3: Comparação (Carga E Descarga vs. Tempo_s)
# ESTE É O GRÁFICO DE JUNÇÃO QUE VOCÊ PRECISA
# ----------------------------------------------------
# Plota a Carga (vermelha)
axes[2].plot(Tempo_s, Carga_V, marker='s', linestyle='-', color='red', markersize=4, label='Carga (C)')
# Plota a Descarga (azul) no mesmo subplot
axes[2].plot(Tempo_s, Descarga_V, marker='o', linestyle='-', color='blue', markersize=4, label='Descarga (R)')

axes[2].set_title('Gráfico 3: Comparação Carga vs. Descarga')
axes[2].set_xlabel('Tempo (s)')
axes[2].set_ylabel('Tensão (V)')
axes[2].grid(True, linestyle='--', alpha=0.6)
axes[2].legend() # Adiciona a legenda para identificar as duas linhas

# Ajusta o layout e exibe
plt.tight_layout()
plt.show()