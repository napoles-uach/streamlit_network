import streamlit as st
import streamlit.components.v1 as components
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
#Network(notebook=True)
st.title('Hello Networkx')

def net_repr_html(self):
  nodes, edges, height, width, options = self.get_network_data()
  html = self.template.render(height=height, width=width, nodes=nodes, edges=edges, options=options)
  return html

Network._repr_html_ = net_repr_html

import networkx as nx
nx_graph = nx.cycle_graph(10)
nx_graph.nodes[1]['title'] = 'Number 1'
nx_graph.nodes[1]['group'] = 1
nx_graph.nodes[3]['title'] = 'I belong to a different group!'
nx_graph.nodes[3]['group'] = 10
nx_graph.add_node(20, size=20, title='couple', group=2)
nx_graph.add_node(21, size=15, title='couple', group=2)
nx_graph.add_edge(20, 21, weight=5)
nx_graph.add_node(25, size=25, label='lonely', title='lonely node', group=3)

from pyvis.network import Network
nt = Network("800px", "800px",heading='Hello Pyvis')
nt.from_nx(nx_graph)
nt.show('test.html')
#components.html(test.html)

HtmlFile = open("test.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
#print(source_code)
components.html(source_code, height = 900,width=900)
