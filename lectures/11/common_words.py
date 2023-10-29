#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Oct 2023

@author: nmm
"""

"""
Lecture 11: Sets

Given a dictionary of topics, calculate the terms (words) that are commons to all entries.
"""


def common_words(topics_dict):
    """
    Given a dictionary whose values are lists of strings, calculate the words that are common to all entries.
    """
    commons = set()
    first_entry = True  # this is a flag: in the first step we cannot apply intersection
    for topics in topics_dict.values():  # recall that by default, dictionary iteration is on leys
        words = set()  # empty set, because {} is empty dictionary
        for topic in topics:
            # converting to set removes duplicates
            entry_words = set(topic.split())
            # set union avoids duplicates and doesn't care about order
            words = words | entry_words

        if first_entry:  # the first entry has nothing to be intersected with
            commons = words
            first_entry = False  # turn the flag false
        else:
            commons = commons & words  # set intersection leaves only common words

    return commons


ctp_topics = {"fpro": ["the global aim of this unit is to give the student the ability to create algorithms and use a programming language to implement  test  and debug algorithms for solving simple problems  the student will understand and use the fundamental programming constructs  and the functional approach to programming  specifically effect free programming where function calls have no side effects and variables are immutable  and contrast it with the imperative approach",
                       "design  implement  test and debug a program that uses the fundamental programming constructs  basic computations  standard conditional and iterative structures  simple input output  persistence  files  and exceptions ",
                       "understand data abstraction and use simple and aggregate data types ",
                       "understand procedural abstraction and use the definition of functions  parameter passing  recursion ",
                       "write useful functions that take and return other functions ",
                       "implement basic algorithms that avoid assigning to mutable state or considering reference equality ",
                       "understand variables and lexical scope in a program ",
                       "define operations on aggregates  including operations that take functions as arguments  especially map  reduce fold and filter   and list comprehensions ",
                       "use the programming tools that help writing  testing and documenting computer programs according to the programming best practices ",
                       "solve numerical problems using computer programs ",],
              "tcom": ["to prepare students about computing theory topics with a special emphasis on formal language topics ",
                       "students will learn about regular languages  regular expressions  non regular languages  deterministic and nondeterministic finite automata  context free languages and grammars  deterministic and non deterministic pushdown automata  and turing machines  and how to apply these topics to problems ",
                       "students will be able to express computing problems by using formal languages  automata  and turing machines ",
                       "in addition  students will learn how to formally specify computing problems related to formal languages and prove related statements ",
                       "identify the important contributions to computing theory and its protagonists ",
                       "identify the problems that finite automata can solve and express them rigorously ",
                       "compare deterministic finite automata  dfas   non deterministic finite automata  nfas   regular expressions  and regular languages ",
                       "apply the properties of regular languages ",
                       "identify problems that can be handled by context free grammars  cfgs  ",
                       "relate context free grammars and pushdown automata  pdas  in the processing of context free languages ",
                       "express computing problems by using turing machines ",
                       "relate the studied computing models with their applications in the computability theory and complexity theory ",],
              "md": ["the goals are the development of skills of rigorous reasoning and in the techniques of discrete mathematics required in several areas of computer science like problem solving  algorithm design and analysis  theory of computing  knowledge representation and security",
                     "represent situations using propositional and first order logic and to analyze them both in the models and the proof perspectives  "
                     "master the basic concepts of sets  relations  partial orders  and functions  "
                     "solve simple problems of number theory  "
                     "solve modular arithmetic equations  "
                     "perform inductive proofs  "
                     "formulate and solve problems through recurrence relations  "
                     "solve simple problems of graph theory "],
              "prog": ["the students who complete this curricular unit successfully must be able to solve programming problems using c c++ code that is well structured  readable  documented and validated ",
                       "imperative programming in c c++:",
                       "primitive and structured data types  operators  declaration and scope of variables ",
                       "program flow control : choice  iteration  functions ",
                       "pointers  dynamic memory allocation  pointer arithmetic ",
                       "object oriented programming in c++:",
                       "classes and objects: fundamental notions  class definition  information encapsulation ",
                       "inheritance between classes and polymorphism ",
                       "generic classes and methods  templates   the standard template library  stl  ",
                       "exceptions ",
                       "cross cutting concerns",
                       "use of the most common functionalities in the standard c c++ libraries ",
                       "good programming practices ",
                       "structuring programs with several modules ",
                       "code readability and documentation ",
                       "bug detection and program validation using runtime sanitizers and unit tests ",]
              }

print("common topics across ucs:", common_words(ctp_topics))
