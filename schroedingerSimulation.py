import numpy as np

hbar = 1.0  
mass = 1.0  
dx = 0.1    
dt = 0.01   
x_min = 0   
x_max = 10   

def potential(x):
    # Infinite square well potential
    if 3 < x < 7:
        return 0
    else:
        return 1e6  # High potential outside the well

x_values = np.arange(x_min, x_max, dx)
num_points = len(x_values)

def init_wavefunction(x_values):
    center = 5
    width = 0.5
    k = 5
    wavefunc = np.exp(-(x_values - center)**2 / (2 * width**2)) * np.cos(k * x_values)
    return wavefunc / np.linalg.norm(wavefunc)  # Normalize the wavefunction

def kinetic_operator(wavefunc, dx):
    return -0.5 * hbar**2 / mass * np.roll(wavefunc, -1) + np.roll(wavefunc, 1) / dx**2

def potential_operator(x_values):
    return np.array([potential(x) for x in x_values])

def time_evolution(wavefunc, dt, dx):
    V = potential_operator(x_values)
    K = kinetic_operator(wavefunc, dx)
    
    wavefunc_new = wavefunc + dt * (K + V * wavefunc)
    
    return wavefunc_new

def simulate_wavefunction(num_steps):
    wavefunc = init_wavefunction(x_values)
    for step in range(num_steps):
        wavefunc = time_evolution(wavefunc, dt, dx)
    return wavefunc

wavefunc_final = simulate_wavefunction(100)
