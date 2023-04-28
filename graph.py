import matplotlib.pyplot as plt
import random
import math
import numpy
def intersect(list1, list2):
    list3=[]
    while(list1 and list2):
        if(list1[0]>list2[0]):del list2[0]
        elif(list1[0]<list2[0]):del list1[0]
        elif(list1[0]==list2[0]):
            list3.append(list1.pop(0))
            del list2[0]
    return list3
class graph:
    def __init__(self, gr):
        self.dict2=gr
        self.dict1={x:0 for x in iter(gr)}
    
    def add(self, x):
       self.dict1.update[{len(self.dict1):x}]
    def addedge(self, key1, key2):
        self.dict2[key1].append(key2)
        self.dict2[key2].append(key1)
    def random(n):
        gr={i:list() for i in range(n)}
        for i in range(n):
            gr[i].append(i)
            for j in range(i+1,n):
                if(random.randint(0,1)):
                    gr[i].append(j)
                    gr[j].append(i)
        return graph(gr)
    def drawgraph(self):
        fig=plt.figure()
        for i in self.dict2:
            for j in self.dict2[i]:
                x1=numpy.array([math.cos(2*i*math.pi/len(self.dict2)), math.cos(2*j*math.pi/len(self.dict2))])
                y1=numpy.array([math.sin(2*i*math.pi/len(self.dict2)), math.sin(2*j*math.pi/len(self.dict2))])
                plt.plot(x1,y1,'ro-')
        for i in self.dict2:
            x1=numpy.array([math.cos(2*i*math.pi/len(self.dict2))])
            y1=numpy.array([math.sin(2*i*math.pi/len(self.dict2))])
            x2=numpy.array([x1[0]*1.07])
            y2=numpy.array([y1[0]*1.07])
            plt.plot(x1,y1,'bo-')
            plt.text(x2,y2,str(i))
        plt.show()
    def complement(self):
        for key in self.dict2:
            list3=[]
            list1=self.dict2[key]
            list2=[i for i in range(len(self.dict2))]
            while(list1 and list2):
                if(list1[0]>list2[0] or list2[0]==key):
                    list3.append(list2[0])
                    del list2[0]
                elif(list1[0]<list2[0]):del list1[0]
                elif(list1[0]==list2[0]):
                    del list1[0]
                    del list2[0]
            self.dict2[key]=list3+list2
def shashlyk(gr):
    gr.complement()
    list1=[]
    list2=[]
    for key in gr.dict2:
        list1.append([[key],gr.dict2[key][:]])
        list2.append(gr.dict2[key][:])
        list3=[1]
    while(list3):
        list3=[]
        for subsets_inter in list1: #subsets=union of [[subset],intersection]
            for i in subsets_inter[1]:
                if(i>subsets_inter[0][-1]):
                    li=intersect(subsets_inter[1][:],list2[i][:])
                    list3.append([subsets_inter[0][:]+[i],li])
        if(list3):list1=list3[:] 
    return list1    
gr=graph.random(50)
#gr=graph({0: [0], 1: [1], 2: [2], 3: [3], 4: [4], 5: [5], 6: [6]})
#print(gr.dict2)

print(shashlyk(gr))
#gr.drawgraph()
  


    