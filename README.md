# Beamforming and DOA Simulation

Este repositório contém um script em Python que simula técnicas de **Beamforming** e estima a **Direção de Chegada (DOA - Direction of Arrival)** de um sinal. O script demonstra, de forma simples e didática, como um sinal transmitido é recebido por um array de antenas, como o beamforming pode ser aplicado para combinar os sinais e, a partir disso, estimar o ângulo de chegada do sinal. Essa abordagem é fundamental em sistemas de comunicação modernos, como os utilizados em 5G.

## Funcionalidades

- **Geração do Sinal Transmitido (TX):**  
  Criação de um sinal complexo com frequência e amplitude definidas, incluindo a adição de ruído para simular condições reais.

- **Simulação da Recepção (RX):**  
  Modelagem de um array de antenas (neste exemplo, 3 antenas) com atrasos de fase correspondentes à direção de chegada do sinal.

- **Beamforming e Estimativa de DOA:**  
  Implementação de um beamformer que varre um campo de ângulos, combina os sinais de cada antena e estima o DOA ao identificar o ângulo que maximiza a potência do sinal combinado.

- **Visualizações:**  
  Geração de gráficos para:
  - Exibir os sinais transmitidos (parte real e imaginária);
  - Comparar os sinais recebidos por cada antena;
  - Visualizar o padrão do beamformer (energia normalizada em função do ângulo).

## Tecnologias Utilizadas

- **Python 3**
- **NumPy** para cálculos numéricos
- **Matplotlib** para visualizações

## Pré-requisitos

Certifique-se de ter o [Python 3](https://www.python.org/downloads/) instalado. Em seguida, instale as dependências necessárias utilizando o `pip`:

```bash
pip install numpy matplotlib
