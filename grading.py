#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 11:45:03 2022

@author: jlopes
"""

from typing import List


def grading(special: bool, missings: int, le: int, re: int,
            pes: List[int], pe_global_missing: bool,
            tes: List[int], te_global_missing: bool) -> str:
    """Given the components, computes the final grade of FP using rules:
       https://sigarra.up.pt/feup/pt/UCURR_GERAL.FICHA_UC_VIEW?pv_ocorrencia_id=484382
    """
    MISSING_ALLOWED = 3
    MIM_GRADE = 40
    MAX_RECUP = 50

    pe_global = max(pes[-2], pes[-1]) if pe_global_missing \
                else max(pes[-2], min(pes[-1], MAX_RECUP))    # recuperation
    te_global = max(tes[-2], tes[-1]) if te_global_missing \
                else max(tes[-2],  min(tes[-1], MAX_RECUP))   # recuperation

    grade_prompt = "Final grade:"

    # compute RFF
    if missings > MISSING_ALLOWED and not special:
        return f"{grade_prompt} RFF"
    if pe_global < MIM_GRADE:
        return f"{grade_prompt} RFF"
    if te_global < MIM_GRADE:
        return f"{grade_prompt} RFF"

    # compute pe
    pe = pe_global
    for p in pes[:-2]:
        pe += p                           # sum all other pe
    pe = (pe - min(pes)) // (len(pes)-1)  # discard the smallest

    # compute te
    te = te_global

    # compute final grade
    grade = int(((le + re + 13 * pe + 5 * te) / 100) + 0.5) if not special \
            else int(((14 * pe + 6 * te) / 100) + 0.5)

    return f"{grade_prompt} {grade}"
 
print()
print(grading(False, 4, 100, 100, [100, 100, 100, 0], False, [100, 0], False))
print(grading(False, 3, 60, 80, [100, 100, 20, 0], False, [0, 0], False))
print(grading(False, 3, 60, 80, [100, 100, 100, 0], False, [20, 0], False))
print(grading(False, 3, 60, 80, [100, 100, 20, 50], False, [60, 0], False))
print(grading(False, 3, 60, 80, [100, 100, 20, 80], False, [60, 0], False))
print(grading(False, 3, 60, 80, [100, 100, 20, 80], True, [20, 50], True))
print(grading(False, 3, 60, 80, [100, 100, 20, 60], True, [20, 60], True))
print(grading(True, 3, 60, 80, [100, 100, 20, 60], False, [20, 60], True))
