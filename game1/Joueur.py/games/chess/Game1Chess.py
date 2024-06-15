import random
class ChessNikhil:
    def __init__(self,FenStr):
        self.FenStr=FenStr
        self.TempArray=[]
        self.PreDic={'K':[(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)], 
                     'Q':[(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)], 
                     'R':[(0,1),(0,-1),(1,0),(-1,0)],
                     'B':[(1,1),(-1,-1),(-1,1),(1,-1)],
                     'N':[(2,1),(2,-1),(-2,1),(-2,-1),(1,-2),(-1,-2),(1,2),(-1,2)],
                     'p':[(1,0),(1,-1),(1,1)],
                     'P':[(-1,0),(-1,-1),(-1,1)]}
        self.enPassanto={'w':[(1,-1),(1,1)],
                         'b':[(-1,-1),(-1,1)]}
        self.Promotion=['b','n','q','r']
        self.ChessBoard=[]
        self.BlackPieces={}
        self.WhitePieces={}
        self.ValidMoves=[]
        self.FirstMove=''
        self.castling_Index=0

    def CreateBoard(self):                    #Fuction To create ChessBoard
        self.TempArray=self.FenStr.split()
        self.FirstMove=self.TempArray[1]
        TempRow=self.TempArray[0].split("/")
        for Row in TempRow:
            ChessBoardTemp=[]
            for Piece in Row:
                if(Piece.isnumeric()):
                    ChessBoardTemp.extend(['.']*int(Piece))
                else:
                    ChessBoardTemp.append(Piece)
            self.ChessBoard.append(ChessBoardTemp)
    def inBound(self,R,C):                  # Checking for the inbound Chessboard Conditions
        if(R<0 or C>7 or R>7 or C<0):
            return False
        return True
    def isMyPiece(self,Piece):              # Checking the Mypiece with the given FenString
        if(Piece.islower() and self.FirstMove=='b'):
            return True
        if(Piece.isupper() and self.FirstMove=='w'):
            return True
        return False
    def MakeAMove(self):                   # MakeAMove Function
        SlidingPieces=['Q','B','R']
        for X in range(0,8):                 # Iterating the ChessBoard
            for Y in range(0,8):
                if(self.ChessBoard[X][Y]!='.' and self.isMyPiece(self.ChessBoard[X][Y])):
                    if(self.ChessBoard[X][Y] not in ['p','P']):                # Checking for Not Pawn Pieces
                        for X1,Y1 in self.PreDic[self.ChessBoard[X][Y].upper()]:
                            slideFlag=False
                            NextCell_X=X
                            NextCell_Y=Y
                            while(not(slideFlag)):
                                NextCell_X+=X1
                                NextCell_Y+=Y1
                                if(self.inBound(NextCell_X,NextCell_Y)):
                                    if(self.ChessBoard[NextCell_X][NextCell_Y]=='.'):          #DefenceMode
                                        self.ValidMoves.append(chr(97+Y)+str(8-X)+chr(97+NextCell_Y)+str(8-NextCell_X))
                                    else:                                                      # CaptureMode
                                        if(not(self.isMyPiece(self.ChessBoard[NextCell_X][NextCell_Y]))):
                                            self.ValidMoves.append(chr(97+Y)+str(8-X)+chr(97+NextCell_Y)+str(8-NextCell_X))
                                        slideFlag=True
                                else:
                                    slideFlag=True
                                if(self.ChessBoard[X][Y].upper() not in SlidingPieces):
                                    slideFlag=True
                    elif(self.ChessBoard[X][Y] in ['p','P']):                # Checking for only Pawn Possibilities
                        for X1,Y1 in self.PreDic[self.ChessBoard[X][Y]]:
                            NextCell_X=X+X1
                            NextCell_Y=Y+Y1
                            if(self.inBound(NextCell_X,NextCell_Y)):
                                if(self.ChessBoard[NextCell_X][NextCell_Y]=='.'and (Y1==0)):
                                    if(NextCell_X==0 or NextCell_X==7):
                                        for i in self.Promotion:
                                            self.ValidMoves.append(chr(97+Y)+str(8-X)+chr(97+NextCell_Y)+str(8-NextCell_X)+i)
                                    else:
                                        self.ValidMoves.append(chr(97+Y)+str(8-X)+chr(97+NextCell_Y)+str(8-NextCell_X))
                                if(self.ChessBoard[NextCell_X][NextCell_Y]!='.' and not(self.isMyPiece(self.ChessBoard[NextCell_X][NextCell_Y])) and (Y1==1 or Y1==-1)):
                                    if(NextCell_X==0 or NextCell_X==7):
                                        for i in self.Promotion:
                                            self.ValidMoves.append(chr(97+Y)+str(8-X)+chr(97+NextCell_Y)+str(8-NextCell_X)+i)
                                    else:
                                        self.ValidMoves.append(chr(97+Y)+str(8-X)+chr(97+NextCell_Y)+str(8-NextCell_X))
                        if(X==1 and X==6):                            # Checking for the Pawn Double Steps
                            NextCell_X=X+2*self.PreDic[self.ChessBoard[X][Y]][0][0]
                            if(self.ChessBoard[NextCell_X][Y]=='.'):
                                self.ValidMoves.append(chr(97+Y)+str(8-X)+chr(97+Y)+str(8-NextCell_X))

        if(self.TempArray[2]!='-'):                        #castlingCondition
            if(self.FirstMove=='w'):
                self.castling_Index=7
            for castling in self.TempArray[2]:
                if(self.isMyPiece(castling)):
                    if(castling.upper()=='K' and self.ChessBoard[self.castling_Index][:4].count('.')==3):
                        self.ValidMoves.append(chr(97+4)+str(8-self.castling_Index)+chr(97+6)+str(8-self.castling_Index))
                    if(castling.upper()=='Q' and self.ChessBoard[self.castling_Index][4:].count('.')==2):
                        self.ValidMoves.append(chr(97+4)+str(8-self.castling_Index)+chr(97+2)+str(8-self.castling_Index))


        if(self.TempArray[3]!='-'):                    #Enpassanto Condition
            NextCell_X1=8-int(self.TempArray[3][1])
            NextCell_Y1=ord(self.TempArray[3][0])-97
            for X,Y in self.enPassanto[self.FirstMove]:
                NextCell_X=NextCell_X1+X
                NextCell_Y=NextCell_Y1+Y
                if(self.inBound(NextCell_X,NextCell_Y)):
                    if(self.isMyPiece(self.ChessBoard[NextCell_X][NextCell_Y]) and self.ChessBoard[NextCell_X][NextCell_Y] in ['p','P']):
                        self.ValidMoves.append(chr(97+NextCell_Y)+str(8-NextCell_X)+self.TempArray[3])
        print(len(self.ValidMoves))
        self.ValidMoves.sort()
        print(*self.ValidMoves,sep=" ")
        RandomMove=random.choice(self.ValidMoves)
        print("My move =",RandomMove)
        return RandomMove
