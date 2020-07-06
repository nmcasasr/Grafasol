import numpy as np
import networkx as nx
import mingus.core.notes as notes
import mingus.core.scales as scales

class Graph:
    class Node:
        def __init__(self, n, x, y, note, duration):
            self.edges = np.zeros(n,dtype=Graph.Node)
            self.x = x
            self.y = y
            self.note = note
            self.duration = duration
    def __init__(self, n, max_x, max_y, mode):
        self.G = nx.Graph()
        self.n = n
        self.max_x = max_x
        self.max_y = max_y
        self.mode = mode
        self.scale = self.get_scale2()
        self.nodes = np.zeros(n,dtype=Graph.Node)
        if(self.mode == 0):
                print("######## Mode 0 ########")
                print("Using Random Note Values")
        else:
                print("######## Mode 1 ########")
                print("Using Random Scale and assigning random values in that range.")
        for i in range(self.n):
            x = np.random.uniform(-max_x,max_x);
            y = np.random.uniform(-max_y,max_y);
            note = ''

            if(self.mode == 0):
                note_int = np.random.randint(0,13)
                if note_int == 12:
                    note = None
                else:
                    note = notes.int_to_note(note_int)
            else:
                note_int = np.random.randint(0,8)
                if note_int == 7:
                    note = None
                else:
                    note = self.scale.ascending()[note_int]
            duration = np.random.randint(1,9)
            self.G.add_node(i, x=x, y=y, note=note, duration=duration)
            self.nodes[i] = Graph.Node(n=self.n,x=x, y=y, note=note, duration=duration)

        #Getting the average
        self.distances = np.zeros((n,n))
        avg = 0
        for i in range(0,n):
            for j in range(i,n):
                if(i == j): continue
                a = (self.nodes[i].x-self.nodes[j].x)
                b = (self.nodes[i].y-self.nodes[j].y)
                d = np.sqrt(a*a + b*b)
                avg += d
                self.distances[i,j] = d
        avg /= (self.n*(self.n-1))

        friends = np.zeros(self.n)
        for i in range(0,n):
            for j in range(i,n):
                if(i == j): continue
                rn = np.random.uniform(0,1);
                if(rn <= avg/(avg + self.distances[i][j])):
                #if(rn <= 1/(self.distances[j][i] * self.distances[i][j])):
                #if(rn <= 1/(self.distances[j][i] + self.distances[i][j])):
                    self.G.add_edge(i,j)
                    self.G.add_edge(j,i)
                    self.nodes[i].edges[j] = self.nodes[j]
                    self.nodes[j].edges[i] = self.nodes[i]
                    friends[i] = friends[i] + 1
        
        meanFriends = np.mean(friends)
    def get_scale(self):
        init_note = np.random.randint(0,12)
        scale = np.random.randint(1,12)
        note = notes.int_to_note(init_note)
        if(scale == 1):
            print("## Ionian Scale Selected!")
            return scales.Ionian(note)
        if(scale == 2):
            print("## Dorian Scale Selected!")
            return scales.Dorian(note)
        if(scale == 3):
            print("## Phrygian Scale Selected!")
            return scales.Phrygian(note)
        if(scale == 4):
            print("## Lydian Scale Selected!")
            return scales.Lydian(note)
        if(scale == 5):
            print("## Mixolydian Scale Selected!")
            return scales.Mixolydian(note)
        if(scale == 6):
            print("## Aeolian Scale Selected!")
            return scales.Aeolian(note)
        if(scale == 7):
            print("## Locrian Scale Selected!")
            return scales.Locrian(note)
        if(scale == 8):
            print("## NaturalMinor Scale Selected!")
            return scales.NaturalMinor(note)
        if(scale == 9):
            print("## HarmonicMinor Scale Selected!")
            return scales.HarmonicMinor(note)
        if(scale == 10):
            print("## MelodicMinor Scale Selected!")
            return scales.MelodicMinor(note)
        if(scale == 11):
            print("## WholeTone Scale Selected!")
            return scales.WholeTone(note)

    def get_scale2(self):
        init_note = np.random.randint(0,12)
        scale = np.random.randint(1,12)
        note = notes.int_to_note(init_note)
        return scales.MelodicMinor(note)