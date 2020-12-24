# Memory
    # Setup how large memory we want
    # What algorithm we want to use


# Process
    # Request allocation of size X
    # Remove allocation

# Test data
    # Set in operations (request, unallocate)
    # Test for each approach

from search import Search
import random
import pickle
import time
import matplotlib.pyplot as plt



class Computer (Search):
    def __init__(self,searchType, size):
        super().__init__()
        self.size = size
        self.searchType = searchType
        self.Array = [-1]*size
        # list of Process
        self.process = list()


    def allocate(self, name, chunk_size):
        position = self.can_allocate(name, chunk_size)
        if (position == -1):
            # return f"[{name}] FAILED TO ALLOCATE: chunk size: {chunk_size}" 
            return 0
        
        self.Array[position:position+chunk_size] = [name]*chunk_size
        # return f"[{name}] SUCESS"
        return 1
    
    def can_allocate(self, name, chunk_size):
        if (self.searchType == "linearSearch"):
            return self.linearSearch(self.Array, self.size, chunk_size)
        if (self.searchType == "exhuastiveSearch"):
            return self.linearSearch(self.Array, self.size, chunk_size)
        if (self.searchType == "directSearch"):
            return self.linearSearch(self.Array, self.size, chunk_size)

    def remove(self, process):
        for i in range(len(self.Array)):
            if (self.Array[i] == process):
                self.Array[i] = -1
        self.print()

    def print(self):
        print(self.Array)


    def linearSearch(self,A,N,X):
        return super().linear_Search(A,N,X)




class Test():
    def __init__(self, search, memorySize, instructions):
        self.comp = Computer(search, memorySize)
        self.instructions = instructions

    def main(self):
        # inst = [03]   # This means process 0 wants to allocate chunk of 3
        # inst = [0E]   # This means process 0 wants to end
        # From these instrutions we can create an array of what instructions we want to apply
        self.comp.print()
        timeTaken = list()
        frag = list()
        for i in self.instructions:
            processName = i[0]
            instruction = i[1]
            start = time.time()
            suc = self.doInstruction(processName,instruction)
            end = time.time()
            timeTaken.append(end-start)
            frag.append(suc) 
        self.comp.print()
     

        self.plot(timeTaken, frag)


    def doInstruction(self, name,inst):
        if (inst == 0):
            print("removing")
            self.comp.remove(name)
            return 1
        else:
            # either add process or try to allocate more to process
            res = self.comp.allocate(name, inst)
            return res


    def plot(self, time, frag):
        print(time)
        print("do the plot")
        # plt.plot(time)
        # plt.ylabel("time")
        # plt.show()
        plt.plot([1,2,3,4])
        plt.ylabel('some numbers')
        plt.show()

if __name__ == "__main__":
    # instructions = [[3, 6], [2, 7], [5, 8], [0, 7], [4, 0], [5, 2], [2, 5], [3, 3], [0, 0], [2, 0], [4, 3], [3, 3], [1, 5], [2, 0], [1, 0], [5, 1], [4, 8], [3, 3], [2, 1], [2, 5], [2, 2], [2, 8], [4, 8], [5, 1], [5, 0], [5, 2], [1, 4], [4, 2], [0, 5], [0, 6], [2, 3], [0, 6], [0, 6], [1, 4], [3, 2], [2, 7], [4, 2], [5, 0], [4, 2], [1, 7], [4, 4], [4, 1], [0, 0], [2, 0], [5, 6], [4, 6], [5, 7], [2, 8], [2, 2], [0, 0], [1, 4], [0, 1], [2, 8], [0, 2], [1, 2], [2, 8], [3, 3], [0, 3], [5, 8], [1, 1], [0, 6], [0, 6], [2, 4], [4, 2], [4, 5], [5, 1], [4, 8], [0, 0], [4, 6], [5, 3], [3, 5], [1, 1], [0, 2], [1, 3], [3, 4], [0, 7], [2, 0], [4, 6], [5, 5], [5, 2], [5, 8], [1, 7], [4, 3], [3, 5], [1, 5], [1, 7], [2, 8], [4, 6], [5, 0], [5, 0], [4, 8], [4, 5], [3, 7], [5, 2], [5, 6], [3, 4], [1, 0], [1, 0], [3, 8], [3, 7]]
    instructions = [[0,2],[0,0]]
    instructions = pickle.load(open("input.prod", "rb"))
    # instructions = [1,2],[2,3],[3,1],[2,0],[4,2],[1,3]
    test = Test("linearSearch", 16, instructions)
    test.main()


