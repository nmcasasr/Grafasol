import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from graph import Graph
import track as tk
import argparse
import mingus.extra.lilypond as LilyPond
def randomMusic(n,x,y,m,t):
    g = Graph(n=n, max_x=x, max_y=y, mode=m)
    t = tk.generate_track(g,n, t)
    bar = LilyPond.from_Track(t)
    print("Lilypond music sheet: ")
    print(bar)
    nx.draw(g.G)
    plt.show()
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--nodes", nargs='?', const='nodes')
    parser.add_argument("-x", "--maxx", nargs='?', const='maxx', default='50')
    parser.add_argument("-y", "--maxy", nargs='?', const='maxy', default='50')
    parser.add_argument("-m", "--mode", nargs='?', const='mode', default='1')
    parser.add_argument("-tn", "--track", nargs='?', const='track', default='track1')
    args = parser.parse_args()
    print(args)
    randomMusic(n=int(args.nodes),x=int(args.maxx), y=int(args.maxy), m=int(args.mode), t=args.track)


if __name__ == "__main__":
    main()