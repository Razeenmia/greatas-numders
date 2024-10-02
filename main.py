import graphviz

dot = graphviz.Digraph()

dot.node('start', 'Start')
dot.node('input', 'Get input')
dot.node('process', 'Process input')
dot.node('output', 'Display output')
dot.node('end', 'End')

dot.edge('start', 'input')
dot.edge('input', 'process')
dot.edge('process', 'output')
dot.edge('output', 'end')

dot.render('flowchart', view=True)