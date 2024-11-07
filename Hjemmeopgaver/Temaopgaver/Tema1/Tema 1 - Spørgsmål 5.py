#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 13:54:30 2024

@author: ThomasThorsted
"""

import cmath
import scipy.optimize

# Definer det komplekse tal z = 5 + i*5
z = complex(5, 5)

# Definer det ønskede resultat af funktionen
desired_result = complex(0.6031225005, 7.045299372)

# Opsæt en funktion til at beregne f_alpha(z)
def f_alpha(alpha, z):
    return z * cmath.exp(complex(0, alpha))

# Opret en fejlmålsfunktion som skal minimeres
def error_function(alpha):
    result = f_alpha(alpha, z)
    diff = abs(result - desired_result)
    return diff

# Brug scipy's optimize.fmin til at finde alpha
alpha_solution = scipy.optimize.fmin(error_function, 0)

# Udskriv det bedste fundne alpha med 2 decimaler
print(f"Alpha = {alpha_solution[0]:.2f}")
