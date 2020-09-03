#!/usr/bin/env python2
""" A tool to help prioritize a long list of things, one `cmp` at a time. """

from __future__ import print_function


def prompt_comparison(A, B):
    prompt = "Which is more important?"
    print()
    print(prompt)
    print("-" * len(prompt))
    print("A) ", A)
    print("B) ", B)

    answer = None
    while answer not in ('A', 'B'):
        answer = raw_input("Enter A or B: ")

    if answer == 'A':
        return 1
    else:
        return -1


if __name__ == '__main__':
    print("Reading items from input.txt")
    with open('input.txt', 'r') as f:
        items = f.read().strip().split('\n')

    items.sort(cmp=prompt_comparison)

    print()
    print("All done!")
    print("Writing sorted items to output.txt")
    with open('output.txt', 'w') as f:
        f.write("\n".join(items))