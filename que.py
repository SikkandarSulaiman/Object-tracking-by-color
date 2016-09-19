class Queue:

    def __init__(self):
        self.qlist = []
	
    def isEmpty(self):
        return self.qlist == []
	
    def enq(self, item):
        self.qlist.insert(0,item)
	
    def deq(self):
        return self.qlist.pop()

    def size(self):
        return len(self.qlist)

    def ret(self, index):
        return self.qlist[index]

    def clear(self):
        self.qlist = []




