class Heap:
    def __init__(self,*args):
        if len(args)!=0:
            self.__a=args[0]
        else:
            self.__a=[]
    
    def __percolateup(self, i):
        parent= (i-1)//2
        if i>0 and self.__a[i][0] < self.__a[parent][0]:
            self.__a[i], self.__a[parent] = self.__a[parent], self.__a[i]
            self.__percolateup(parent)
            
    def __percolatedown(self,i):
        leftch= 2*i+1
        rightch=2*i+2
        if leftch<=len(self.__a)-1:
            if (rightch<=len(self.__a)-1) and (self.__a[rightch][0]<self.__a[leftch][0]):
                minch=rightch
            else:
                minch=leftch
            if self.__a[i][0]> self.__a[minch][0]:
                self.__a[minch] , self.__a[i]= self.__a[i], self.__a[minch]
                self.__percolatedown(minch)
                
    def insert(self, cnt,x) :
        self.__a.append([cnt,x])
        self.__percolateup(len(self.__a)-1)
        

    def deleteMin(self):
        if self.isEmpty():
            return None
        self.__a[0], self.__a[-1] = self.__a[-1], self.__a[0]
        retitem = self.__a.pop()
        self.__percolatedown(0)
        return retitem
    
    def isEmpty(self):
        if len(self.__a)==0:
            return True
        else:
            return False
        
    def size(self):
        return len(self.__a)
    
    def min(self):
        return self.__a[0]
    
    def buildHeap(self):
        for i in range((len(self.__a)-2)//2, -1, -1):
            self.__percolatedown(i)
    
    def already_in_heap(self, data):
        for i in self.__a:
            if i[1]== data:
                i[0]+=1
                self.buildHeap()
                return True
        return False
            
    def heapPrint(self):
        l= len(self.__a)
        lst2=[]
        for i in range(l):
            if (2**i) > l:
                break
            else:
                lst2.append(2**i)

        print("==================================")
        cnt=0
        for i in range(len(self.__a)):
            print(self.__a[i],end = ' ')
            cnt+=1
            if cnt in lst2:
                lst2.pop(0)
                cnt=0
                print()           
        print()
        
        
def lfu_sim(cache_slots):
    cache_hit = 0
    tot_cnt = 0
    h= Heap()
    data_file = open("C:\\Users\\gsmin2020\\Desktop\\SoongSilUniv\\2-1\\Data_structure\\lfu_sim\\linkbench.trc")
    
    cntdict={}
    for line in data_file.readlines():
        lpn = line.split()[0]
        tot_cnt += 1        
        
        if lpn in cntdict:
            cntdict[lpn]+=1
        else:
            cntdict[lpn]=1
            
        if h.already_in_heap(lpn):
            cache_hit+=1
        else:                
            if h.size()<cache_slots:
                h.insert(1,lpn)
            else:
                h.deleteMin()
                h.insert(cntdict[lpn],lpn)
    h.heapPrint()
    print("============================")
    print("cache_slot = ", cache_slots, "cache_hit = ", cache_hit, "hit ratio = ", cache_hit / tot_cnt)
    
if __name__ == "__main__":
    #for cache_slots in range(100, 1000, 100):
     #   lfu_sim(cache_slots)
    lfu_sim(100)
    