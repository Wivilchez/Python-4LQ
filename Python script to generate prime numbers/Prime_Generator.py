#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 14:50:24 2017

@author: pakinja
"""

n = 60000
primes = []

for p in range(2, n+1):
    for i in range(2, p):
        if p % i == 0:
            break
    else:
        primes.append(p)
        print(p)