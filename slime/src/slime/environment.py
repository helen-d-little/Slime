from scipy import ndimage, datasets
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import default_rng


def initial_lattice() -> np.array:
    base = build_base_lattice()
    plt.imshow(base)
    plt.show()

def build_base_lattice(dim:int = 50) -> np.array:
    base_lattice = default_rng(42).random((dim,dim), dtype='float')
    food_lattice = add_food(base_lattice)
    filtered_lattice = filter_lattice(food_lattice)
    return filtered_lattice

def add_food(lattice:np.array) -> np.array:
    xpos = int(lattice.shape[0]/2)
    ypos = int(lattice.shape[1]/2)
    for x in [xpos-1, xpos, xpos+1]:
        for y in [ypos-1, ypos, ypos+1]:
            lattice[x,y] = 5
    return lattice

def filter_lattice(lattice:np.array) -> np.array:
    filtered_lattice = ndimage.uniform_filter(lattice, size=3)
    return filtered_lattice
