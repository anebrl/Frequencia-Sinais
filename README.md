## Frequência de Sinais

## Análise Espectral de um Sinal

### Descrição
Este código Python realiza a análise espectral de um sinal composto por duas senóides e ruído branco. 
O objetivo é demonstrar o uso da função `signal.spectrogram` da biblioteca SciPy para calcular e visualizar o espectrograma do sinal.

### Importação de bibliotecas: 
Importa as bibliotecas NumPy, Matplotlib e SciPy, essenciais para operações numéricas, visualização e processamento de sinais, respectivamente.

### Definição de parâmetros: 
Define a frequência de amostragem, cria um vetor de tempo e ajusta os parâmetros dos sinais senoidais e do ruído.

### Geração do sinal: 
Cria dois sinais senoidais com frequências diferentes e adiciona ruído branco para simular um sinal real.

### Cálculo do espectrograma: 
Utiliza a função signal.spectrogram da SciPy para calcular o espectrograma do sinal, que representa a distribuição da energia do sinal ao longo da frequência e do tempo.

### Visualização: 
Plota o espectrograma usando a função pcolormesh do Matplotlib, com uma escala logarítmica para melhor visualização.

### Pré-requisitos
* Python 3.x
* Bibliotecas: NumPy, Matplotlib, SciPy

### Utilização
1. **Clone este repositório** ou salve o código como um arquivo Python (por exemplo, `analise_espectral.py`).
2. **Execute o código** utilizando um ambiente Python:
   ```bash
   python analise_espectral.py
