import numpy as np
import math
import random
import networkx as nx
import copy
import matplotlib.pyplot as plt
from itertools import combinations
from networkx.algorithms import tree
class point:
    def __init__(self):
        self.x=0
        self.y=0
        self.oldx=0
        self.oldy=0
        self.radius=random.randint(1,3)
        self.theta=math.pi/5