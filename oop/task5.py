from collections import deque

class HistoryDict():
    def __init__(self, in_data):
        self.data = {}
        self.history = deque(maxlen=5)
        if in_data:
            self.data.update(in_data)
            
    def set_value(self, k:str, v:int):
        self.data[k]=v
        self.history.append(k)
        
    def get_history(self):
        print(list(self.history))
        return list(self.history)
    
    
d = HistoryDict({"ok":7})
d.set_value("boo", 88)
d.set_value("boo", 88)
d.set_value("boo", 88)
d.set_value("boo", 88)
d.set_value("boo", 88)
d.set_value("boo", 88)
d.set_value("boo", 88)
d.get_history()
        
            