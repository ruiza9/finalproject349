def draw_game_summary(df, ax):
        # making the structure
        # fig, ax = plt.subplots(figsize=(10,4))

        rows = 3 # number of rows that we want
        cols = 6 # number of columns that we want


        ax.set_ylim(-0.5, rows) #  y limits
        ax.set_xlim(0, cols) #  X limits
        ax.axis('off') # removing all the spines
        
        offense_extract = create_offense_summary(df)
        matrix = offense_extract

        # iterating over each row of the dataframe and plot the text
        # df_working is a DataFrame object with our fake data
        for row in matrix.iloc[:,:].iterrows(): # this will return the row as a tupple
                
                # row[0] will be the index of the row
                # row[1] will be the actual data as a Series
                x_position = 0.5
                for i in matrix.columns:
                        ax.text(x=x_position,  
                                y=row[0], 
                                s=row[1][i], 
                                va="center", 
                                ha="center", 
                                size=10)
                        ax.text(x_position, 
                                rows-0.5, str(i), 
                                weight='bold', 
                                ha='center', 
                                size=10,
                                color='green',
                                alpha=0.5,
                                wrap=True)._get_wrap_line_width = lambda : 100
                        x_position+=1


        # Adding title
        ax.set_title(
                'Points Splitted by Assisted and Solo Play',
                loc='center',
                fontsize=12,
                weight='bold',
                color='gray',
                wrap=True
        )

        # adds main line belowthe headers
        # ax.plot([.25,cols-.2], [rows-1.5, rows-1.5],ls="-",lw=1,c="black")

        # adds multiple lines below each row
        for row in matrix.iterrows():
                ax.plot(
                [.25, cols-.2],
                [row[0] -.5, row[0] - .5],
                ls=':',
                lw='.5',
                c='grey'
                )
        # return ax
