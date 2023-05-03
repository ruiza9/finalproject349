def draw_networkgraph(df2, ax):

    offense_summary = create_offense(df2)
    individual_offense = create_individual_offense(offense_summary)    
    G = create_graph(offense_summary)
    
    ###### DRAWING NODES #######
    '''
    The size of the nodes will be proportional to 
    the amount of scoring they create by themselves
    without the help of an assist
    '''

    individual_offense = (offense_summary[['ShooterName','ShotValue']]
                        .loc[(offense_summary['ShooterName']==offense_summary['AssisterName'])]
                        .reset_index(drop=True))

    a = dict(zip(individual_offense['ShooterName'],individual_offense['ShotValue']))
    for k, v in a.items():
        a[k] = float(v)

    players_solo_score = dict.fromkeys(G.nodes(), 0)
    players_solo_score.update(a)

    for k, v in players_solo_score.items():
        players_solo_score[k] = float(v)

    nodesize = np.array(list(players_solo_score.values()))
    nodesize = nodesize/np.sum(nodesize)
    nodesize = [i*10000 for i in nodesize]

    ###### DRAWING EDGES #######
    '''
    The width of the edges will be proportional to the amount
    of points created by an assist between two players.
    '''
    #EdgeList
    non_assisted = [(u, v) for (u, v, d) in G.edges(data=True) if u != v]

    #EdgeSize
    edgesize = [(d) for (u, v, d) in G.edges(data=True) if u != v]
    edgesize = np.array([value['ShotValue'] for value in edgesize])
    edgesize = edgesize/np.sum(edgesize)*100


    ###### DRAWING GRAPH #######

    # Position of the Nodes in the Graph (Circular)
    pos = nx.circular_layout(G)


    # Drawing Nodes
    nx.draw_networkx_nodes(G, pos, 
                        node_size=nodesize, 
                        node_color='green',
                        alpha=0.5)


    # Drawing Edges
    nx.draw_networkx_edges(G, pos, 
                        edgelist=non_assisted, 
                        width=edgesize, 
                        alpha=0.2, 
                        arrows=True,
                        arrowstyle='-',
                        arrowsize=20,
                        edge_color="black")

    # Dreawing Labels
    label_options = {"ec": "k", "fc": "green", "alpha": 0.01}
    nx.draw_networkx_labels(G, pos, 
                            font_size=7, font_family="sans-serif", font_color='black',
                            verticalalignment='bottom',
                            horizontalalignment = 'center',
                            bbox=label_options
                            )

    ax.set_title(
        "Network of Points between players",
        loc='center',
        fontsize=12,
        weight='bold',
        color='gray',
        wrap=True
            )

    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    # return ax    
