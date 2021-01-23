#package maze;
import operator
import sys
import queue
class Cell("1prize-medium.txt"):
    def __init__(self):
        self.data = []; 
    def read_file(self, path): #file is the path
        #reads the maze file and returns that maze in two-dimensional array representation, by row x colums
        maze = []
    
        with open(path) as f:
            for line in f.read().splitlines():
                maze.append(list(line))
            self.data = maze
    
    
    def write_file(self, path):
        #writes our data taken from the maze file into another file as a two-dimensional array
        with open(path, 'w') as f:
            for row, line in enumerate(self.data):
                f.write('%s\n' % ''.jpin(line)) # unsure about the '% sign here' ?????????
                
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
    
    def goal(maze, where = None, arrows=None):
        start_square = 'P'
        empty_square = ' '
        visited_square = 'b' #correct later?????? #vacant ..
        cord = (0,1), (1,0),(0,-1),(-1,0) #direction
        direct_signs = 'l','r','u','d' #direction_marks - left, right, up, down
        prize_square = '.'
        
    def DFS(coord_x = None, coord_y = None, coord_vis=None):
            


            coord_vis.append((coord_x, coord_y))
            content = maze[coord_x, coord_y]
            
        
            if coord_x < 0: 
                return
            if coord_y < 0:
                return
            if coord_x >=matrix.shape[0]:
                return
            if coord_y >=matrix.shape[1]:
                return
            
            for i in range(coord_x-1, coord_x+2):
                for j in range(coord_y-1,coord_y+2):
                    if not(i==coord_x and j==coord_y) and i >-1 and j > -1 and i<matrix.shape[0] and j<matrix.shape[1] and (i,j) not in visited:
                        
                        if content == ".": 
                #decrement number of prizes
                            num_prizes = num_prizes -1
               # if num_prizes = 0:
                    #return
                
                #in our second file mark this as 0
                #file name is f
                            maze[coord_x][coord_y] = 0  #not sure check later????
                        
                return DFS(i, j, visited)
                    
    def BFS (queue=None):
        currentPostion = queue.get()
        coord_x, coord_y = currentPosition[0], currentPosition[1]
        content == maze[coord_y, coord_x]
        if content == ".":
            return coord_x, coord_y
             
            for i in range(coord_x-1, coord_x+2):
                for j in range(coord_y-1,coord_y+2):
                    if not(i==coord_x and j==coord_y) and i >-1 and j > -1 and i<matrix.shape[0] and j<matrix.shape[1] and (i,j) not in queue.queue:
                        
                     
                        if content == ".": 
                #decrement number of prizes
                            num_prizes = num_prizes -1
                            queue.put((i,j))

            return BFS(queue)
            
            
            
    def main():
        results = Cell("1prize-medium.txt")
        results.DFS(coord_x,coord,y)
        
    if __name__ == "__main__":
        main()
        print("lets go")
       
      
        
        
                
                

