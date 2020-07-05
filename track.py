import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from graph import Graph
from mingus.containers import Track
from mingus.midi import midi_file_out
from mingus.containers.instrument import MidiInstrument
from mingus.containers import NoteContainer
def generate_track(g, n, name):
    root = np.random.randint(0,n)
    edges = nx.bfs_edges(g.G, root)
    nodes = [root] + [v for u, v in edges]
    m = MidiInstrument(4)
    t = Track() 
    t.instrument = m
    print("##### Creating Tracks")
    for x in nodes:
        value = t.add_notes(NoteContainer(g.G.nodes[x]["note"]), g.G.nodes[x]["duration"])
        t.bars[-1].set_meter((n, 1))
    midi_file_out.write_Track( name +".mid", t)