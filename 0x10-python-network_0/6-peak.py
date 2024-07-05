#!/usr/bin/python3
"""Algorithms for list of integers."""


def find_peak(list_of_integers):
    """"The function find the peak of given list."""
    if not list_of_integers:
        return None
    else:
        return max(list_of_integers)
