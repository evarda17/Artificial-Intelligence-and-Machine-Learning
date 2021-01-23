
import operator
import sys
import queue
# import numpy

class Cell(object):
    def __init__(self):
        self.data = [] 
    def read_file(self, path): #file is the path
        #reads the maze file and returns that maze in two-dimensional array representation, by row x colums
        maze = [[],[]]  
        with open(path) as f:
            for line in f.read().splitlines():
                maze.append(list(line))
            self.data = maze
        
    def write_file(self, path):
        #writes our data taken from the maze file into another file as a two-dimensional array
        with open(path, 'w') as f:
            for row, line in enumerate(self.data):
                f.write('%s\n' % ''.join(line)) 
                # unsure about the '% sign here' ?????????
                
    def start(self,symbol):
        for row, line in enumerate(self.data):
            try:
                return row, line.index('P')
            except ValueError:
                pass
            #this function returns the coordinates of the start position if it exist. otherwise gives a valueerror;
            
    def get(self,where ):
        row, clm = where
        return self.data[row][clm]
        #access symbols that are stored in some specific cells
    
    def place(self, where, symbol):
        row, clm = where
        self.data[row][clm] = symbol
        #specific symbols are stored in the specific cells
                
    def __str__(self):
        return '\n'.join(''.join(row) for row in self.data)
        
    def DFS(self, row, clm, coord_vis=None):
        coord_vis.append((row, clm))
        content = maze[row, clm]
        if row < 0:            
            return
        if clm < 0:
            return
        if row >=maze.shape[0]:                           
            return
        if clm >=maze.shape[1]:
            return
            
        for i in range(row-1, row+2):
            for j in range(clm-1,clm+2):
                if not(i==row and j==clm) and i >-1 and j > -1 and i<maze.shape[0] and j<maze.shape[1] and (i,j) not in coord_vis:
                        
                    if content == ".":  
                        print("found1")                                              
                #decrement number of prizes
                        # num_prizes = num_prizes - 1
               # if num_prizes = 0:
                    #return
                
                #in our second file mark this as 0
                #file name is fp
                    maze[row][clm] = 0  #not sure check later????
                        
        return DFS(i, j, visited)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Arguments: <input file> <output file>')
        sys.exit(1)
    coord_vis = []
    input_file, output_file = sys.argv[1:3]  
    maze = Cell()
    maze.read_file(input_file)
    coordinatesds = maze.start(input_file)
    # print(coordinatesds)
    # print(coordinatesds[0],coordinatesds[1], coord_vis)
    # print("done") 
    maze.DFS(coordinatesds[0], coordinatesds[1], coord_vis)
      