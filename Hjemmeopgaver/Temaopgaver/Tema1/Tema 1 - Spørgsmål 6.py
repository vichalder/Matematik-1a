#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 14:00:25 2024

@author: ThomasThorsted
"""

import cmath

# Definer de komplekse tal z1 og z2
z1 = complex(2, 5)  # z1 = 2 + i*1
z2 = complex(8, 3)  # z2 = 6 + i*3

# Skalering med faktor 7
scaled_z1 = z1 * 8
scaled_z2 = z2 * 8

# Rotation med vinkel 0.6 radianer mod uret
rotation_angle = 0.2
rotated_z1 = scaled_z1 * cmath.exp(complex(0, rotation_angle))
rotated_z2 = scaled_z2 * cmath.exp(complex(0, rotation_angle))

# Parallelforskydning med vektoren (2, 2)
translation = complex(3, 3)
w1 = rotated_z1 + translation
w2 = rotated_z2 + translation

# Udskriv resultaterne med 2 decimalers præcision
print(f"w1 = {w1.real:.2f} + {w1.imag:.2f}i")
print(f"w2 = {w2.real:.2f} + {w2.imag:.2f}i")
