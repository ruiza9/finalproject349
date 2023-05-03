def draw_adjancecy_matrix(df2, fig, ax):

    offense_summary = create_offense(df2)
    # individual_offense = create_individual_offense(offense_summary)    
    G = create_graph(offense_summary)
    
    A = nx.adjacency_matrix(G,weight='ShotValue',)
    matrix = A.todense()
    assiters = list(G.nodes())
    scorers = list(G.nodes())

    # fig, ax = plt.subplots()
    im = ax.imshow(matrix, cmap='Greens')

    # Show all ticks and label them with the respective list entries
    ax.set_xticks(np.arange(len(assiters)), labels=assiters)
    ax.set_yticks(np.arange(len(scorers)), labels=scorers)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
            rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    for i in range(len(scorers)):
        for j in range(len(assiters)):
            text = ax.text(j, i, matrix[i, j],
                        ha="center", va="center", color="black")

    ax.set_title(
           "Points Distributed by Scorer and Assister",
            loc='center',
            fontsize=12,
            weight='bold',
            color='gray',
            wrap=True
                )

    fig.tight_layout()
    # return plt.show()
