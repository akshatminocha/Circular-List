class  CircularList:
    def __init__(self):
        self.position,self.step=list(map(int,input().split()))
        self.List=[0,1,2,3,4,5,6,7,8,9,10,11]
        self.index=-1
    def __iter__(self):
        return self
    def __next__(self):
        self.index+=1
        if self.index==len(self.List):
            self.index=0
            return self.List[self.index]
        else:       
            return self.List[self.index]
            #for handling condition of EOF(end of list) and start from the beginning after last element of the list        
            
test_cases=int(input())
for i in range(test_cases):
    obj=CircularList()
    itr=iter(obj)
    for j in range((obj.step+obj.position)):
        (next(itr))
    print(next(itr))
