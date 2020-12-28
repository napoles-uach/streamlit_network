import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
import pandas as pd
import streamlit as st


def got_func(physics):
  got_net = Network(height="600px", width="100%", font_color="black",heading='Game of Thrones Graph')

# set the physics layout of the network
  got_net.barnes_hut()
  got_data = pd.read_csv("https://www.macalester.edu/~abeverid/data/stormofswords.csv")
  #got_data = pd.read_csv("stormofswords.csv")
  #got_data.rename(index={0: "Source", 1: "Target", 2: "Weight"}) 
  sources = got_data['Source']
  targets = got_data['Target']
  weights = got_data['Weight']

  edge_data = zip(sources, targets, weights)

  for e in edge_data:
    src = e[0]
    dst = e[1]
    w = e[2]

    got_net.add_node(src, src, title=src)
    got_net.add_node(dst, dst, title=dst)
    got_net.add_edge(src, dst, value=w)

  neighbor_map = got_net.get_adj_list()

# add neighbor data to node hover data
  for node in got_net.nodes:
    node["title"] += " Neighbors:<br>" + "<br>".join(neighbor_map[node["id"]])
    node["value"] = len(neighbor_map[node["id"]])
  if physics:
    got_net.show_buttons(filter_=['physics'])
  got_net.show("gameofthrones.html")
  

def simple_func(physics): 
  nx_graph = nx.cycle_graph(10)
  nx_graph.nodes[1]['title'] = 'Number 1'
  nx_graph.nodes[1]['group'] = 1
  nx_graph.nodes[3]['title'] = 'I belong to a different group!'
  nx_graph.nodes[3]['group'] = 10
  nx_graph.add_node(20, size=20, title='couple', group=2)
  nx_graph.add_node(21, size=15, title='couple', group=2)
  nx_graph.add_edge(20, 21, weight=5)
  nx_graph.add_node(25, size=25, label='lonely', title='lonely node', group=3)


  nt = Network("500px", "500px",notebook=True,heading='')
  nt.from_nx(nx_graph)
  #physics=st.sidebar.checkbox('add physics interactivity?')
  if physics:
    nt.show_buttons(filter_=['physics'])
  nt.show('test.html')


def karate_func(physics): 
  G = nx.karate_club_graph()


  nt = Network("500px", "500px",notebook=True,heading='Zachary’s Karate Club graph')
  nt.from_nx(G)
  #physics=st.sidebar.checkbox('add physics interactivity?')
  if physics:
    nt.show_buttons(filter_=['physics'])
  nt.show('karate.html')
