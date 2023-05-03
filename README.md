# finalproject349
Sports Betting Data Pipeline

Dataprep.py is a file used to extract the data. We want to extract the information of successful shooting (made baskets) from ONE team in ONE game. These extraction constraints can be modified later in the code, but it's our entry point. In any data project, this is a very lengthy, unsexy, and necessary step.

datavis.py is a file that is used to build a graph. The size of the node (bubble) will be the number of points a player does without any assists. The width of the edge (arrow) will be the number of points that a combination (Assister & Scorer) does.

WAM.py is a file that creates a weighted adjacency matrix. This matrix has the same representation as the network graph, but in this one you can read the actual values. The diagonal of the matrix is the number of points scored solo.

game_summary.py creates a summary of the shots taken by the team and In this case you can see how many points are scored solo or assisted, and how this is split by the diverse types of shots in NBA Basketball (tree points, two points and free throws).

dash.py creates a dashboard that includes datavis.py, WAM.py and game_summary.py in one view.
