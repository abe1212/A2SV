class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        self.points[(point[0],point[1])]+=1
        

    def count(self, point: List[int]) -> int:

        count = 0
        for x,y in self.points.keys():
            if(abs(point[0]-x)==abs(point[1]-y) and abs(point[1]-y)>0 ):
                
                possible_pt1 = (point[0],y)
                possible_pt2 = (x,point[1])

                if(possible_pt1 in self.points and possible_pt2 in self.points):
                    count +=self.points[(x,y)]*self.points[possible_pt1]*self.points[possible_pt2]

        return count


 
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)