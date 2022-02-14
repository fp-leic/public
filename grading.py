#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 11:45:03 2022

@author: jlopes
"""

from typing import List


def grading(special: bool, absences: int, le: int, re: int,
            pes: List[int], missing_last_pe: bool,
            tes: List[int], missing_last_te: bool) -> str:
    """Given the components, computes the final grade of FP using rules:
       https://sigarra.up.pt/feup/pt/UCURR_GERAL.FICHA_UC_VIEW?pv_ocorrencia_id=484382
    """
    MISSINGS_ALLOWED = 3
    MIN_GRADE = 40
    MAX_RECUP = 50

    pe_global = max(pes[-2], pes[-1]) if missing_last_pe \
                else max(pes[-2], min(pes[-1], MAX_RECUP))    # recuperation
    te_global = max(tes[-2], tes[-1]) if missing_last_te \
                else max(tes[-2],  min(tes[-1], MAX_RECUP))   # recuperation

    grade_prompt = "Final grade:"

    # compute RFF
    if absences > MISSINGS_ALLOWED and not special:
        return f"{grade_prompt} RFF"
    if pe_global < MIN_GRADE:
        return f"{grade_prompt} RFF"
    if te_global < MIN_GRADE:
        return f"{grade_prompt} RFF"

    # compute pe
    new_pes = [pe_global] + pes[:-2]
    pe = (sum(new_pes) - min(new_pes)) // (len(new_pes)-1)  # discard the smallest

    # compute te
    te = te_global

    # compute final grade
    grade = int(((le + re + 13 * pe + 5 * te) / 100) + 0.5) if not special \
            else int(((14 * pe + 6 * te) / 100) + 0.5)

    return f"{grade_prompt} {grade}"
 
print()
print("1.", grading(False, 4, 100, 100, [100, 100, 100, 0], False, [100, 0], False))
print("2.", grading(False, 3, 60, 80, [100, 100, 20, 0], False, [0, 0], False))
print("3.", grading(False, 3, 60, 80, [100, 100, 100, 0], False, [20, 0], False))
print("4.", grading(False, 3, 60, 80, [100, 100, 20, 50], False, [60, 0], False))
print("5.", grading(False, 3, 60, 80, [100, 100, 20, 80], False, [60, 0], False))
print("6.", grading(False, 3, 60, 80, [100, 100, 20, 80], True, [20, 50], True))
print("7.", grading(False, 3, 60, 80, [100, 100, 20, 60], True, [20, 60], True))
print("8.", grading(True, 3, 60, 80, [100, 100, 20, 60], False, [20, 60], True))
print("9.", grading(True, 3, 60, 80, [100, 100, 20, 60], False, [100, 0], True))
