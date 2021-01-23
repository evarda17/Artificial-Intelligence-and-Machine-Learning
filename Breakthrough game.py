import sys
# from scipy.spatial.distance import euclidean
import random
import operator
import copy
class Node(object):
    def __init__(self, state, depth, parent=None):
        self.parent = None
        self.children = []
        self.action = None 
        self.state = None
        self.utility = None
        self.depth = depth

    # bd=board()

    def add_child(self, node):
        self.children.append(node)
        node.parent = self

    def getExpandNodes(self, node):
            return node.child

    def getDepth(self):
        return self.depth



class board(object):

    def __init__(self):
        """creating board"""
        self.firstPlayer = "X"
        self.secondPlayer = "Y"
        self.space = "."
        self.sumOfFirstPlayerPieces = 0
        self.sumOfSecondPlayerPieces = 0
        self.pieceTurn = "X"
        self.matrix = []

    def boardT(self, row, col, size):  
        self.matrix = [[]* row for n in range(col)]
        for x in range(0,size):
            for y in range(0,col):
                self.matrix[x].append(self.firstPlayer)
        for x in range(size,row-size):
            for y in range(0,col):
                self.matrix[x].append(self.space)
        for x in range(row-size,row):
            for y in range(0,col):
                self.matrix[x].append(self.secondPlayer)
        return self.matrix


    def displayState(self, matrix):
        for row in matrix:
                print(' '.join(row))
        # return

    def getPiece(self,state,coordinates):
        (x, y) = coordinates
        piece = state[x][y]
        if piece == self.firstPlayer:
            return "X"
        if piece == self.secondPlayer:
            return "Y"
        if piece == self.space:
            return "."


    def pieceLeft(self, matrix, piece):
        self.sumOfFirstPlayerPieces = 0
        self.sumOfSecondPlayerPieces = 0
        for row in matrix:
            for col in row:
                if col == self.firstPlayer:
                    self.sumOfFirstPlayerPieces +=1
                
                if col == self.secondPlayer:
                    self.sumOfSecondPlayerPieces +=1

        # pieces_left =  (self.sumOfFirstPlayerPieces, self.sumOfSecondPlayerPieces)
        if piece == self.firstPlayer:
            # print('pieces left:', self.sumOfFirstPlayerPieces)
            return self.sumOfFirstPlayerPieces
        else:
            # print('pieces left:', self.sumOfSecondPlayerPieces)
            return self.sumOfSecondPlayerPieces
        

    def getPlayerDirection(self, state, coordinates):
        piece = self.getPiece(state, coordinates)
        if piece == self.firstPlayer:
            piece = "Down"
            return piece
        elif piece == self.secondPlayer:
            piece == "Up"
            return piece 

    def getAllPlayerCoordinates(self, state, player):
        playerCoordinates = []
        for x, row in enumerate(state):
            for y, col in enumerate(row):
                if col == player:
                    playerCoordinates.append((x,y))

        return playerCoordinates


    def possibleMoves(self, state,coordinates):
        """Possible moves include up or down and diagonals(both left and right)"""
        (x,y) = coordinates
        piece = self.getPiece(state,(x,y))
        possible_moves = []
        if piece == self.secondPlayer:   ###up
            if x-1 > -1 and y-1 > -1:
                possible_moves.append((x-1, y-1)) #####LD
            if x-1 > -1 :
                possible_moves.append((x-1, y)) #forward  #
            if x-1 > -1 and y+1 < len(state):
                possible_moves.append((x-1, y+1))  #RD
        elif piece == self.firstPlayer: ###ddown
            if x+1 < len(state):
                possible_moves.append((x+1,y)) #forward
            if x+1 < len(state) and y-1 > -1: 
                possible_moves.append((x+1,y-1)) #leftdiagonal
            if x+1 < len(state)  and y+1 <len(state):
                possible_moves.append((x+1,y+1)) #rightdiagonal
        playerNotIN = []
        positions = self.getAllPlayerCoordinates(state,piece)
        for coords in possible_moves:
            if coords not in positions:
                playerNotIN.append(coords)
        return playerNotIN


    def moveDirection(self,state,coordinates):
        pm = self.possibleMoves(state,coordinates)
        player = self.getPiece(state,coordinates)
        direction =[]
        for i in pm:                
            (x,y) = i
            (a,b) = coordinates
            # print(a)
            if player == self.firstPlayer:
                if x == a+1 and y == b:
                    direction.append("FW")
                if x == a+1 and y == b-1:
                    direction.append("RD")
                if x == a+1 and y == b+1:
                    direction.append("LD")
            if player == self.secondPlayer:
                if x == a-1 and y == b:
                    direction.append("FW")
                if x == a-1 and y == b-1:
                    direction.append("RD")
                if x == a-1 and y == b+1:
                    direction.append("LD")
        return direction


    def switchTurn(self, player):
        if player == self.firstPlayer:
            player = self.secondPlayer
        elif player == self.secondPlayer:
            player = self.firstPlayer
        return player
        
    def _terminal_test(self, state):
        #check if either player has 0 pieces on the board
        count1 = 0
        count2 = 0
        for row in state:
            for col in row:
                if col == self.firstPlayer:
                    count1 += 1
                elif col == self.secondPlayer:
                    count2 += 1
        if count1 == 0 or count2 == 0:
            return True
        
        for i in range(len(state[0])):
            if state[0][i] == self.secondPlayer:
                print("Game over, Y won")
                return True
        for i in range(len(state[0])):
            if state[-1][i] == self.firstPlayer:
                print("Game over X won")
                return True
        return False
    
    def terminal_test(self, state):
        for x in range(0,1):
            for y in range(0,len(state)):
                if state[x] == self.secondPlayer:
                    return True
           
        for x in range(7,8):
            for y in range(0,len(state[0])):
                if state[x] == self.firstPlayer:
                    return True
        #a loop checking if the board has any X or O at all
        countX=0
        countY =0
        for x in range(0,8):
            for y in range(0,8):
                if state[x] == self.firstPlayer:
                    countX +=1
                elif state[x] == self.secondPlayer:
                    countY +=1
        if countX == 0:
            return True
        elif countY == 0:
            return True
        else:
            return False
    
    def changeDirToCoordinate(self, state,coordinates,direction):
        (x,y) = coordinates
        a = 0
        b = 0
        moveD = direction
        direction = self.getPlayerDirection(state,coordinates)
        if direction == "Up":
            a = x-1
            for action in moveD:
                if action == "FW":
                    b = y-1
                    dtg2 = (a,b)
                    return dtg2
                if action == "RD":
                    b = y+1
                    dtg1 = (a,b)
                    return dtg1
                if action == "LD":
                    b = y-1
                    dtg3 =(a,b)
                    return dtg3 
        elif direction == "Down":
            a = x+1
            for action in moveD:
                if action == "FW":
                    b = y
                    dtg2 = (a,b) 
                    return dtg2
                if action == "RD":
                    b = y-1
                    dtg1 = (a,b)
                    return dtg1
                if action == "LD":
                    b = y+1
                    dtg3 = (a,b)
                    return dtg3


    def transition(self,state,coordinates,directiontogoto):  #an alternative would be to take the coords and coords to 
        # directiontogoto = self.evaluation(state, utility,coordinates)
        if self.pieceTurn != self.getPiece(state,coordinates):
            return False
        (x,y) = coordinates
        a = 0
        b = 0
        moveD = self.moveDirection(state,coordinates)
        direction = self.getPlayerDirection(state,coordinates)
        if direction == "Up":
            a = x-1
            for action in moveD:
                if action == "FW":
                    b = y-1
                if action == "RD":
                    b = y+1
                if action == "LD":
                    b = y-1
        elif direction == "Down":
            a = x+1
            for action in moveD:
                if action == "FW":
                    b = y
                    dtg2 = (a,b) 
                if action == "RD":
                    b = y-1
                    dtg1 = (a,b) 
                if action == "LD":
                    b = y+1
                    dtg3 = (a,b) 
        # picking a directino to go
        if directiontogoto == "FW":
            state[dtg2[0]][dtg2[1]] = state[x][y]
        if directiontogoto == "RD":
            state[dtg1[0]][dtg1[1]] = state[x][y]
        if directiontogoto == "LD":
            state[dtg3[0]][dtg3[1]] = state[x][y]
        # # # replacing empty spot with "."     
        state[x][y] = self.space
        self.displayState(state)
        # return state
        # self.switchTurn()

    def simpletransition(self, state, piece, newloc):
        copy_state = copy.deepcopy(state)
        (a,b) = piece
        (x,y) = newloc
        copy_state[x][y] = copy_state[a][b]
        # replacing empty spot with "."
        copy_state[a][b] = self.space
        return copy_state
             
        # state[x][y] = self.space
        # self.displayState(copy_state)

    def permTrasition(self, state, piece, newloc):
        # copy_state = copy.deepcopy(state)
        (a,b) = piece
        (x,y) = newloc
        state[x][y] = state[a][b]
        # replacing empty spot with "."
        state[a][b] = self.space
        self.displayState(state)
        return state
             
        # state[x][y] = self.space
        
    
    def Superman(self, state, player):

        first_pieces = self.pieceLeft(state, self.firstPlayer)
        second_pieces = self.pieceLeft(state, self.secondPlayer)
        if player == self.firstPlayer:

            utility = ((first_pieces -second_pieces) *30) + first_pieces * 3
            # print("Superman result for first player", utility)
                        
            # return utility
        else:
            utility = ((second_pieces - first_pieces) *30) + second_pieces * 3
            # print("Superman result for second player", utility)
        # print(type(utility))
        return(utility)

    # def Batman(self, state, player):
    #     moves = []

    #     cords = []
    #     each_cord =()
    #     first_pieces = self.pieceLeft(state, player)
    #     second_pieces = self.pieceLeft(state, self.secondPlayer)

    #     if player == self.firstPlayer:
    #         x =7

    #         for i in range(len(state[0])):
    #             each_cord = (x, i)
    #             # print(each_cord)
    #             i+=1

    #         cords.append(each_cord)
    #         min_dist = float('inf')
    #         moves.append(self.everypiecemoves(state, self.firstPlayer))
    #         for key, value in moves[0].items():
    #             # print(key)
    #             new_dist = min(euclidean(c, key) for c in cords)
    #             # print(new_dist)
    #             if new_dist < min_dist:
    #                 min_dist = new_dist
    #                 # print(min_dist)
    #             # return(min_dist)

    #         utility = ((first_pieces -second_pieces) * 5) + min_dist * 2
    #         # print("Batman result first player:",utility)
    #         return utility
                        
    #         # print(utility)
        
    #     if player == self.secondPlayer:
    #         x = 0

    #         for i in range(len(state[0])):
    #             each_cord = (x,i)
    #             i+=1
    #         cords.append(each_cord)
    #         min_dist = float('inf')
    #         moves.append(self.everypiecemoves(state, self.secondPlayer))
    #         for key, value in moves[0].items():
    #             new_dist = min(euclidean(c, key) for c in cords)

    #             if new_dist < min_dist:
    #                 min_dist = new_dist
    #                 # print(min_dist) 
    #             # return(min_dist)  # return min_dist #min_dist_first
    #         utility = ((second_pieces - first_pieces) * 5) + min_dist *2
    #         # print("Batman result second player:", utility)
    #         return utility
                        
    #         # print(utility)

    def evasive(self,state,player):
            pieces = self.pieceLeft(state, player)
            value = round(random.uniform(0,1),0)
            utility = value + pieces
            return utility
            # print(utility)
    
    def conqueror(self, state,player):
            pieces = self.pieceLeft(state, player)
            value = round(random.uniform(0,1),2)
            utility = (0-pieces) + value
            return utility
            # print(utility)

    def everypiecemoves(self, state, player):
        diction = {}
        moves = []
        piecePositions = self.getAllPlayerCoordinates(state, player)
        for piece in piecePositions:
            moves.append(self.possibleMoves(state,piece))
        diction =dict(zip(piecePositions, moves))
        return diction


    def _minimax(self, state, player, depth, utility1, utility2):
        """state:   board
           player:  first (max) or second (min) player
           depth:   how many turns to look ahead
           utility: evasive or conqueror
        """
        #if depth == 0 or self._terminal_test(state):
            #return self.evasive(state, player)
        
        if player == self.firstPlayer:
            if depth == 0 or self._terminal_test(state):
                return utility1(state, player)
                
            maxEval = float("-inf")
            moves = self.everypiecemoves(state, player)
            for m in moves:
                new_moves = moves[m]
                for i in new_moves:
                    new_state = self.simpletransition(state, m, i)
                    eval  = self._minimax(new_state, self.secondPlayer, depth-1, utility1, utility2)
                    print(eval)
                    # gene = (m,i)
                    maxEval = max(maxEval, eval)
                    # # print(gene)
                    if maxEval < eval:
                        maxEval = eval
                        best_gene = (m,i) 
                    # print(type(eval))
                    # print(maxEval)
                    
            # self.displayState(new_state)
            # print(maxEval)
            # print('\n')
            # print(maxEval,gene)
            return  maxEval, best_gene
        
        elif player == self.secondPlayer:
            if depth == 0 or self._terminal_test(state):
                return utility2(state, player)
            minEval = float("inf")
            moves = self.everypiecemoves(state, player)
            for m in moves:
                new_moves = moves[m]
                for i in new_moves:
                    new_state = self.simpletransition(state, m, i)  
                    eval = self._minimax(new_state, self.firstPlayer, depth-1, utility1, utility2)
                    print(eval)
                    # gene = (m,i)
                    minEval = min(minEval, eval)   
                    if minEval > eval:
                        mingEval = eval
                        best_gene = (m,i)                  
                    # print(gene)
            # self.displayState(new_state)
            # print(minEval)
            # print('\n')
            # print(minEval,gene)
            return minEval, best_gene
        # else:
        #     print("okay not")



    # def evaluation(self, state, utility, coordinates):
    #     diction = {}
    #     liss = []
    #     direction = self.moveDirection(state,coordinates)
    #     # print(direction)
    #     value = utility(state, coordinates)
    #     # print(value)
    #     moves = self.possibleMoves(state,coordinates)
    #     # print(moves)
    #     for move in moves:
    #         liss.append(utility(state,move))
    #     diction =dict(zip(direction, liss))
    #     # print(diction)
    #     valueOfDiction = list(diction.values())
    #     keyOfDiction = list(diction.keys())
    #     # print(keyOfDiction, valueOfDiction)
    #     nextMax = keyOfDiction[valueOfDiction.index(max(valueOfDiction))]
    #     nextMin = keyOfDiction[valueOfDiction.index(min(valueOfDiction))]
    #     nextMove = nextMax

    #     return nextMove


def main():
    cw = board()
    # dq = Node()
    a = input("Enter number of rows: ")
    b = input("Enter number of columns: ")
    c = input("Enter number of rows to be filled by player: ")
    # x_utility = input("Enter utility for X: ")
    # print(type(x_utility))
    # y_utility = input("Enter utility for Y: ")
    state = cw.boardT(int(a),int(b),int(c))
    cw.displayState(state)
    print('\n')
    utility2 = cw.conqueror
    utility1 = cw.conqueror
    # cw.pieceLeft(state, cw.firstPlayer)
    # cw.getPiece((1,5))
    # cw.getPlayerDirection((1,5))
    # cw.getAllPlayerCoordinates(cw.firstPlayer)
    # print(cw.possibleMoves(state,(0,0)))
    # cw.terminal_test(state)
    # cw.moveDirection(state,(1,2))
    # cw.transition(cw.conqueror,state,(1,6))
    # cw.evasive(state, cw.firstPlayer)
    # cw.evaluation(state, cw.conqueror, (1,4))
    # cw._minimax(state,cw.firstPlayer,2,utility1,utility2)
    # cw.changeDirToCoordinate(state,(1,3),"LD")
    # cw.everypiecemoves(state,cw.firstPlayer)
    cw._minimax(state,cw.firstPlayer,2,utility1,utility2)
    # player = cw.firstPlayer
    # while not cw._terminal_test(state):
        
    #     movestoget = cw._minimax(state,player,3,utility1,utility2)
    #     # print(player)
    #     oldloc, newloc = movestoget[0], movestoget[1]
    #     print(cw.possibleMoves(state,oldloc))
    #     if newloc not in cw.possibleMoves(state,oldloc):
    #         pass
    #     new_state = cw.permTrasition(state,oldloc, newloc)
    #     player = cw.switchTurn(player)
        
    #     state = new_state
        
         
    #     print("\n")
    
    


    

if __name__ == '__main__':
    main()

