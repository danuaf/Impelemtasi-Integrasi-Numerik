import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import csv

if __name__ == '__main__':
    # Fungsi untuk dihitung
    def f(x):
        return 4 / (1 + x**2)

    # Metode integrasi Reimann
    def reimann_integration(N):
        a = 0
        b = 1
        dx = (b - a) / N
        total_area = 0
        for i in range(N):
            x = a + i * dx
            total_area += f(x) * dx
        return total_area

    # Menghitung galat RMS
    def rms_error(approx_pi, true_pi=3.14159265358979323846):
        return np.sqrt((approx_pi - true_pi)**2)

    # Testing dengan variasi N
    N_values = [10, 100, 1000, 10000]
    true_pi = 3.14159265358979323846

    results = []

    for N in N_values:
        start_time = time.time()
        approx_pi = reimann_integration(N)
        elapsed_time = time.time() - start_time
        error = rms_error(approx_pi, true_pi)
        results.append((N, approx_pi, error, elapsed_time))

    # Menyimpan hasil ke CSV
    with open('assets/hasil_integrasi_reimann.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["N", "Approximate Pi", "RMS Error", "Execution Time (s)"])
        writer.writerows(results)

    print("Results saved to reimann_integration_results.csv")


    # Membaca hasil dari CSV
    df = pd.read_csv('assets/hasil_integrasi_reimann.csv')
    print(df)

    plt.figure(figsize=(12, 6))

    # Plot hubungan antara N dengan RMS error
    plt.subplot(1, 2, 1)
    plt.plot(df['N'], df['RMS Error'], marker='o', linestyle='-', color='b')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('N')
    plt.ylabel('RMS Error')
    plt.title('N VS RMS Error')

    # Plot hubungan antara N dengan Execution Time
    plt.subplot(1, 2, 2)
    plt.plot(df['N'], df['Execution Time (s)'], marker='o', linestyle='-', color='r')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('N')
    plt.ylabel('Execution Time (s)')
    plt.title('N VS Execution Time')

    plt.tight_layout()
    plt.show()

