import matplotlib.pyplot as plt
import numpy as np
from schroedingerSimulation import simulate_wavefunction, x_values

num_steps = 100
wavefunc_final = simulate_wavefunction(num_steps)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(x_values, np.abs(wavefunc_final)**2, label='Probability Density')
plt.title('Probability Density of the Wavefunction')
plt.xlabel('x')
plt.ylabel('|ψ(x)|²')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x_values, np.real(wavefunc_final), label='Real Part of ψ(x)')
plt.plot(x_values, np.imag(wavefunc_final), label='Imaginary Part of ψ(x)')
plt.title('Wavefunction (Real and Imaginary Parts)')
plt.xlabel('x')
plt.ylabel('ψ(x)')
plt.legend()

plt.tight_layout()
plt.show()
