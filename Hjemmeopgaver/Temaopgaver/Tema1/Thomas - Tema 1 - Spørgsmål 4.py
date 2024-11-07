#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 13:47:34 2024

@author: ThomasThorsted
"""

import cmath

# Definer den første rod z1, som er givet i opgaven
z1 = complex(1.633333333, 0.9333333332)

# Beregn de to andre rødder ved at rotere z1 med 120 grader og 240 grader
z2 = z1 * cmath.exp(complex(0, 2 * cmath.pi / 3))  # rotation med 120 grader
z3 = z1 * cmath.exp(complex(0, 2 * cmath.pi * 2 / 3))  # rotation med 240 grader

# Udskriv resultaterne med 3 decimalers præcision
print(f"z1 = {z1.real:.3f} + {z1.imag:.3f}i")
print(f"z2 = {z2.real:.3f} + {z2.imag:.3f}i")
print(f"z3 = {z3.real:.3f} + {z3.imag:.3f}i")

