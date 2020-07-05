import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from graph import Graph
import track as tk
from mingus.containers import Track
from mingus.midi import midi_file_out
g = Graph(n=100, max_x=50, max_y=50, mode=0)
g2 = Graph(n=100, max_x=50, max_y=50, mode=1)
g3 = Graph(n=50, max_x=10, max_y=10, mode=0)
g4 = Graph(n=50, max_x=10, max_y=10, mode=1)
tk.generate_track(g,100, 'track1')
tk.generate_track(g2,100, 'track2')
tk.generate_track(g3,50, 'track3')
tk.generate_track(g4,50, 'track4')
nx.draw(g.G)
plt.show()