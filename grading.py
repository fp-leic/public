#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 11:45:03 2022

@author: jlopes, et all.
"""

from typing import List


def grading(special: bool, absences: int, le: int, re: int,
            pes: List[int], justified_pe_absence: bool,
            tes: List[int], justified_te_absence: bool) -> str:
    """Given the components, computes the final grade of FP using rules:
       https://sigarra.up.pt/feup/pt/UCURR_GERAL.FICHA_UC_VIEW?pv_ocorrencia_id=484382
    
    special: student of special regimes (TE, DA, EA, AR, ...)
    absences: number pratical classes absences
    le: agregate LE classification (given by the Moodle gradebook)
    re: agregate RE classification (given by the Moodle gradebook)
    pes: list with all (4 terms in 2021/22) pratical on computer evaluation (PEXX)
    justified_pe_absence: absence to PEXX global with justification accepted
    tes: list with all teorical evaluation (TEXX); 2 terms
    justified_te_absence: absence to TE01 global with justification accepted
    
    return: classification string
    """
    # validade inputs
    assert len(pes) >= 4
    assert len(tes) == 2
    assert 0 <= le <= 100
    assert 0 <= re <= 100
    assert all(map(lambda x: 0 <= x <= 100, pes + tes))

    # constants
    MISSINGS_ALLOWED = 3
    MIN_GRADE = 40
    MAX_RECUP = 50

    # pe with minimum classification required (the last)
    pe_global = max(pes[-2], pes[-1]) if justified_pe_absence \
                else max(pes[-2], min(pes[-1], MAX_RECUP))    # recuperation

    # te with minimum classification required
    te_global = max(tes[-2], tes[-1]) if justified_te_absence \
                else max(tes[-2],  min(tes[-1], MAX_RECUP))   # recuperation

    grade_prompt = "Final grade:"

    # compute RFF
    if absences > MISSINGS_ALLOWED and not special:
        return f"{grade_prompt} RFF"
    if pe_global < MIN_GRADE:
        return f"{grade_prompt} RFF"
    if te_global < MIN_GRADE:
        return f"{grade_prompt} RFF"

    # compute PE
    new_pes = [pe_global] + pes[:-2]
    pe = (sum(new_pes) - min(new_pes)) // (len(new_pes)-1)  # discard the smallest

    # compute TE
    te = te_global

    # compute FINAL grade
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
