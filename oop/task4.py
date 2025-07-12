

class Counter():
    def __init__(self,start = 0, stop = None ):
        self.start = start
        self.stop = stop
        self.current = start
        
    def increment(self):
        if self.stop is None or self.current<self.stop :
            self.current+=1
        else:
            print("The maximal value is reached.")
    
    def get(self):
        print(self.current)
        

c = Counter(start=42, stop=43)
c.increment()
c.increment()
c.get()



