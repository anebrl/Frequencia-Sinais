import numpy as np  # Importa a biblioteca NumPy, usada para operações matemáticas com arrays.
import matplotlib.pyplot as plt  # Importa a biblioteca Matplotlib para criação de gráficos e visualizações.
from scipy import signal  # Importa o módulo de sinal da biblioteca SciPy, usado para processamento de sinais.

# Mudando a duração do sinal alterando o tempo=20s
# Parâmetros do sinal
fs = 1000  # Define a frequência de amostragem (fs) em 1000 Hz, ou seja, 1000 amostras por segundo.
t = np.arange(0, 20, 1/fs)  # Cria um vetor de tempo (t) que vai de 0 a 10 segundos com passos de 1/fs segundos.

# Modificando a frequência dos sinais s1=75 e s2=150Hz respectivamente
# Sinal de exemplo: soma de duas senóides com ruído
signal1 = np.sin(2 * np.pi * 75 * t)  # Gera um sinal senoidal de 50 Hz (signal1).
signal2 = np.sin(2 * np.pi * 150 * t)  # Gera um sinal senoidal de 120 Hz (signal2).

# Ajustando o Nível de Ruído multiplicando por 2.0
noise = 0.2 * np.random.randn(len(t))  # Gera ruído branco com a mesma duração dos sinais, multiplicado por 0.5.


x = signal1 + signal2 + noise  # Combina os dois sinais senoidais e o ruído em um único sinal (x).

# Inserindo o paramentro nperseg=512 na função signal.spectrogram
# Gera o espectrograma do sinal combinado
f, t, Sxx = signal.spectrogram(x, fs, nperseg=512)  # Calcula o espectrograma de 'x' com a frequência de amostragem 'fs'.
                                       # Retorna frequências (f), tempos (t) e a densidade espectral de potência (Sxx)
                                       #dada em W/Hz em dB/Hz (em escala logarítmica).


# Plota o espectrograma
plt.pcolormesh(t, f, 10 * np.log10(Sxx))  # Plota o espectrograma usando uma escala logarítmica para a densidade espectral.
plt.ylabel('Frequência [Hz]')  # Define o rótulo do eixo y como "Frequência [Hz]".
plt.xlabel('Tempo [s]')  # Define o rótulo do eixo x como "Tempo [s]".
plt.title('Espectrograma')  # Define o título do gráfico como "Espectrograma".
plt.colorbar(label='Intensidade [dB]')  # Adiciona uma barra de cores ao lado do gráfico, indicando a intensidade em dB.
plt.show()  # Exibe o gráfico.
