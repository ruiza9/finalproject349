def draw_dashboard(df2):
    fig = plt.figure("Degree of a random graph", figsize=(12, 8))

    axgrid = fig.add_gridspec(10, 6)

    ax0 = fig.add_subplot(axgrid[1:4, :])
    draw_game_summary(df2, ax0)

    ax1 = fig.add_subplot(axgrid[4:, :4])
    draw_networkgraph(df2, ax1)

    ax2 = fig.add_subplot(axgrid[4:, 4:])
    draw_adjancecy_matrix(df2, fig, ax2)

    # Add lines between subplots
    fig.add_artist(plt.Line2D((0.00, 1), (0.65, 0.65), color='gray', linewidth=0.5, linestyle=':'))
    fig.add_artist(plt.Line2D((0.6, 0.6), (0.65, 0), color='gray', linewidth=0.5, linestyle=':'))
    # fig.add_artist(plt.Line2D((0.05, 0.95), (0.82, 0.82), color='black', linewidth=1))
    fig.suptitle(str('Analysis of a Basketball Game - Network Perspective '), fontsize=16,  weight='bold',color='black')

    plt.show()
