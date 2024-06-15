import random
import sys
class HappyFarm:
    def __init__(self):
        self.Size=0
        self.Grid=[]
        self.Empty_Cells=[]
        self.Loc=[]
        self.HayStack_Count=0
        self.Score=0
    def GridGenerator(self,Input):
        self.Input_File=open(Input,'r')
        self.Size=int(self.Input_File.readline())
        self.Grid.append(['&']*(self.Size+2))
        for i in range(1,self.Size+1):
            self.Grid.append(['&']+list(self.Input_File.readline())+['&'])
            for j in range(len(self.Grid[i])):
                if(self.Grid[i][j]=='.'):
                    self.Empty_Cells.append([i,j])
                if(self.Grid[i][j]=='@'):
                    self.HayStack_Count+=1
        self.Grid.append(['&']*(self.Size+2))
        self.Input_File.close()
    def Random_Generator(self):
        self.Loc=list(range(0,len(self.Empty_Cells)))
        random.shuffle(self.Loc)
        return self.Loc[:self.Size]
    def GridCowGenerator(self):
        for i in range(self.HayStack_Count):
            self.Grid[self.Empty_Cells[self.Loc[i]][0]][self.Empty_Cells[self.Loc[i]][1]]='C'
    def HappyCowFarm(self):
        for i in range(self.HayStack_Count):
            x=self.Empty_Cells[self.Loc[i]][0]
            y=self.Empty_Cells[self.Loc[i]][1]
            if(self.Grid[x+1][y]=='@' or self.Grid[x-1][y]=='@' or self.Grid[x][y+1]=='@' or self.Grid[x][y-1]=='@'):
                self.Score+=1
            if((self.Grid[x+1][y]=='@' or self.Grid[x-1][y]=='@' or self.Grid[x][y+1]=='@' or self.Grid[x][y-1]=='@') and (self.Grid[x+1][y]=='#' or self.Grid[x-1][y]=='#' or self.Grid[x][y+1]=='#' or self.Grid[x][y-1]=='#')):
                self.Score+=2
            if(self.Grid[x+1][y]=='C' or self.Grid[x-1][y]=='C' or self.Grid[x][y+1]=='C' or self.Grid[x][y-1]=='C' or self.Grid[x+1][y+1]=='C' or self.Grid[x-1][y-1]=='C' or self.Grid[x-1][y+1]=='C' or self.Grid[x+1][y-1]=='C'):
                self.Score-=3
        return self.Score
    def OutputFileEntry(self,Output):
        self.File_Output=open(Output,'w')
        self.File_Output.write(str(self.Size)+"\n")
        for i in range(1,len(self.Grid)-1):
            self.File_Output.write("".join(self.Grid[i][1:-1]))
        self.File_Output.write(str(self.Score))
        self.File_Output.close()
def main(args):
    Cow1=HappyFarm()
    Cow1.GridGenerator(args[1])
    Cow1.Random_Generator()
    Cow1.GridCowGenerator()
    Cow1.HappyCowFarm()
    Cow1.OutputFileEntry(args[2])
if __name__ == '__main__':
    main(sys.argv)





    


