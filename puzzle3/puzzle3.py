#Nikhil Vuppala 12597901
import random
import sys
class HappyFarm:
    def __init__(self):                      # Constructor for the HappyFarm Class
        self.Size=0
        self.Grid=[]
        self.Empty_Cells=[]
        self.Loc=[]
        self.HayStack_Count=0
        self.Score=0
    def GridGenerator(self,Input):           # Creating a Grid with Haystack and Water Pond
        self.Input_File=open(Input,"r")
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
    def HappyCowFarm(self,F_in):             # Calculating the Score
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
    def Bounded_DFS(self,Depth_limit):       # Performing the DFS Algorithm with certain depth limit
        Frontier=[]
        for i in range(len(self.Empty_Cells)):
            Frontier.append([self.Empty_Cells[i]])
        while(len(Frontier)!=0):
            F_in=Frontier.pop()
            if(len(F_in)==Depth_limit):
                self.Score=self.HappyCowFarm(F_in)
                if(self.Score>=7):
                    self.Loc=F_in
                    return True
            else:
                Ind=self.Empty_Cells.index(F_in[-1])
                for i in range(Ind+1,len(self.Empty_Cells)):
                    Frontier.append(F_in+[self.Empty_Cells[i]])
        return False           
    def Transition_ID_DFS(self):             # Transition of ID_DFS and checking the DFS for individual Depth
        Depth_limit=1
        while Depth_limit>0 :
            Res=self.Bounded_DFS(Depth_limit)
            if(Res):
                break
            else:
                Depth_limit+=1
    def GridCowGenerator(self):              # Placing the Cows in the Grid
        for i in range(len(self.Loc)):
            self.Grid[self.Loc[i][0]][self.Loc[i][1]]='C'
    def OutputFileEntry(self,Output):        # Placing the Grid in the output file followed by Score
        self.File_Output=open(Output,"w")
        self.File_Output.write(str(self.Size)+"\n")
        for i in range(1,len(self.Grid)-1):
            self.File_Output.write("".join(self.Grid[i][1:-1]))
        self.File_Output.write(str(self.Score))
        self.File_Output.close()
def main(args):                              # Performing sequence of Function calls
    Cow1=HappyFarm()
    Cow1.GridGenerator(args[1])
    Cow1.Transition_ID_DFS()
    Cow1.GridCowGenerator()
    Cow1.OutputFileEntry(args[2])
if __name__ == '__main__':                   # Main Function
    main(sys.argv)
