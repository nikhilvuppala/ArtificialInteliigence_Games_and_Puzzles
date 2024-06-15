#Nikhil Vuppala
import random
import sys
class HappyFarm:
    def __init__(self):                                # This function is for the Object constructor
        self.Size=0
        self.Grid=[]
        self.Empty_Cells=[]
        self.Loc=[]
        self.HayStack_Count=0
        self.Score=0
    def GridGenerator(self,Input):                     # This function is used for the creating a farm(grid) with the placements of haystack and water ponds
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
    def HappyCowFarm(self,F_in):                       # used to calculate the score(i.e. Goal).
        Score=0
        for i in range(len(F_in)):
            x=F_in[i][0]
            y=F_in[i][1]
            if(self.Grid[x+1][y]=='@' or self.Grid[x-1][y]=='@' or self.Grid[x][y+1]=='@' or self.Grid[x][y-1]=='@'):
                Score+=1
            if((self.Grid[x+1][y]=='@' or self.Grid[x-1][y]=='@' or self.Grid[x][y+1]=='@' or self.Grid[x][y-1]=='@') and (self.Grid[x+1][y]=='#' or self.Grid[x-1][y]=='#' or self.Grid[x][y+1]=='#' or self.Grid[x][y-1]=='#')):
                Score+=2
            if([x+1,y] in F_in or [x-1,y] in F_in or [x,y+1] in F_in or [x,y-1] in F_in or [x+1,y+1] in F_in or [x-1,y-1] in F_in or [x-1,y+1] in F_in or [x+1,y-1] in F_in):
                Score-=3
        return Score
    def Transition_BFS(self):                          # Performing the BFS to get the least nu. of cows to satisfy the given goals.
        Frontier=[]
        for i in range(len(self.Empty_Cells)):
            Frontier.append([self.Empty_Cells[i]])
        while(len(Frontier)!=0):
            F_in=Frontier.pop(0)
            self.Score=self.HappyCowFarm(F_in)
            if(self.Score>=7):
                self.Loc=F_in
                break
            else:
                Ind=self.Empty_Cells.index(F_in[-1])
                for i in range(Ind+1,len(self.Empty_Cells)):
                    Frontier.append(F_in+[self.Empty_Cells[i]])
    def GridCowGenerator(self):                        # After matching the goal placing the cows in the farm(i.e Grid)
        for i in range(len(self.Loc)):
            self.Grid[self.Loc[i][0]][self.Loc[i][1]]='C'
    def OutputFileEntry(self,Output):                  # This function write the output in the output txt file
        self.File_Output=open(Output,'w')
        self.File_Output.write(str(self.Size)+"\n")
        for i in range(1,len(self.Grid)-1):
            self.File_Output.write("".join(self.Grid[i][1:-1]))
        self.File_Output.write(str(self.Score))
        self.File_Output.close()
def main(args):                                        # Main function performing all the above operations.
    Cow1=HappyFarm()
    Cow1.GridGenerator(args[1])
    Cow1.Transition_BFS()
    Cow1.GridCowGenerator()
    Cow1.OutputFileEntry(args[2])
if __name__ == '__main__':
    main(sys.argv)





    


