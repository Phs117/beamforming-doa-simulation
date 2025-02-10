# -*- coding: utf-8 -*-
"""
Exemplo de Beamforming e Estimativa de DOA (Direction of Arrival)
"""

import numpy as np
import matplotlib.pyplot as plt

# ==============================
# SINAL TRANSMITIDO (TX)
# ==============================

A = 1                   # Amplitude do sinal
f = 1e6                 # Frequência do sinal (1 MHz)
fs = 10 * f             # Frequência de amostragem (10 MHz)
td = 10e-3              # Duração do sinal (10 ms)
samples = int(fs * td)  # Número de amostras

t = np.linspace(0, td, samples, endpoint=False)
tx = A * np.exp(1j * 2 * np.pi * f * t)  # Sinal complexo transmitido

# Adiciona ruído ao sinal transmitido
noise_tx = (np.random.normal(0, 0.1, tx.shape) +
            1j * np.random.normal(0, 0.1, tx.shape))
tx_noisy = tx + noise_tx

# Plot dos primeiros 100 samples do sinal transmitido com ruído
plt.figure(figsize=(8, 4))
plt.plot(t[0:100], np.real(tx_noisy[0:100]), label="Parte Real")
plt.plot(t[0:100], np.imag(tx_noisy[0:100]), label="Parte Imaginária")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.title("Sinal Transmitido com Ruído (primeiros 100 samples)")
plt.legend()
plt.grid(True)
plt.show()

# ==============================
# SIMULAÇÃO DO RECEPÇÃO (RX) EM UM ARRAY DE ANTENAS
# ==============================

M = 3                   # Número de antenas no array
d = 0.5                 # Espaçamento entre antenas (em lambda)
DOA_true = 10           # Ângulo de chegada verdadeiro em graus
DOA_true_rad = np.deg2rad(DOA_true)
antenna_indices = np.arange(M)

# Vetor de steering para o sinal recebido (cada antena tem um atraso de fase)
steering_vector = A * np.exp(-1j * 2 * np.pi * d * antenna_indices * np.sin(DOA_true_rad))

# Cada antena recebe o sinal transmitido com a defasagem apropriada
# rx terá dimensão (M, samples)
rx = steering_vector[:, None] * tx_noisy

# Adiciona ruído à recepção de cada antena
noise_rx = (np.random.normal(0, 0.1, rx.shape) +
            1j * np.random.normal(0, 0.1, rx.shape))
rx_noisy = rx + noise_rx

# Plot dos sinais recebidos (primeiros 100 samples) para cada antena
plt.figure(figsize=(8, 4))
for m in range(M):
    plt.plot(t[0:100], np.real(rx_noisy[m, 0:100]), label=f"Antenna {m+1}")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.title("Sinais Recebidos com Ruído (primeiros 100 samples)")
plt.legend()
plt.grid(True)
plt.show()

# ==============================
# BEAMFORMING E ESTIMATIVA DE DOA
# ==============================

# Definindo o campo de varredura (Field of View): de -45° a 45°
angles_scan_deg = np.linspace(-45, 45, 180)  # em graus
angles_scan_rad = np.deg2rad(angles_scan_deg)
beamformer_output = []

# Para cada ângulo de varredura, calcula-se a saída do beamformer
for theta in angles_scan_rad:
    # Vetor de steering para o ângulo 'theta'
    steering_theta = np.exp(-1j * 2 * np.pi * d * antenna_indices * np.sin(theta))
    
    # Peso ideal: o conjugado do vetor de steering (fazer a soma coerente)
    weights = np.conjugate(steering_theta)
    
    # Combinação dos sinais das antenas com os respectivos pesos:
    # para cada instante, soma-se os sinais ponderados
    y = np.sum(weights[:, None] * rx_noisy, axis=0)
    
    # Calcula-se a potência média do sinal beamformado para esse ângulo
    power = np.mean(np.abs(y)**2)
    beamformer_output.append(power)

beamformer_output = np.array(beamformer_output)

# Estima o DOA como o ângulo que maximiza a potência
DOA_est_rad = angles_scan_rad[np.argmax(beamformer_output)]
DOA_est_deg = np.rad2deg(DOA_est_rad)
print("DOA estimado:", DOA_est_deg, "graus")

# Plot do padrão do beamformer (potência normalizada em função do ângulo)
plt.figure(figsize=(8, 4))
plt.plot(angles_scan_deg, beamformer_output / np.max(beamformer_output), lw=2)
plt.xlabel("Ângulo (graus)")
plt.ylabel("Energia Normalizada")
plt.title("Padrão do Beamformer")
plt.grid(True)
plt.show()
