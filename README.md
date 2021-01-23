# Artificial-Intelligence-and-Machine-Learning


#Search and Pathfinding


-------------------------------------------------------------------------------------------------------------------
Introduction
-------------------------------------------------------------------------------------------------------------------
The Search_Path.py file contains four search functions: Greedy BFS, BFS, DFS and A-star. All of these functions are meant to find the path toward the prizes located in the maze. Additionally, in our Search_Path.py we have a maze reading function that reads the input.txt file of the maze and converts it into a 2D array for later searching applications. This function, when running, will return the path signed as ‘#’, number of nodes expanded and the path cost ( number of steps taken).


-------------------------------------------------------------------------------------------------------------------
Requirements
-------------------------------------------------------------------------------------------------------------------
 To run the program Python 3 version is required to use. A maze text file as an input will also be required to run this code.


-------------------------------------------------------------------------------------------------------------------
Configuration
-------------------------------------------------------------------------------------------------------------------
To run a specific search function, e.g. BFS a specific maze, e.g. 1prize_medium, the input of the file should be as followed: 
% python3 Search_Path.py 1prize_medium.txt output.txt
To specify the type of the search, open the Search_path.py with a text editor, uncomment the call function ( BFS main at the bottom of the script) and run the script from the terminal like mentioned above. 

