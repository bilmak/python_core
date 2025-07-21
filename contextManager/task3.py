import os


class Cd:

    def __init__(self, path):
        self.path = path
        if not os.path.isdir(self.path):
            raise ValueError(
                "passed directory is not a directory or does not exist")

    def __enter__(self):
        self.own_dir = os.getcwd()
        os.chdir(self.path)
        return self.path
    
    def __exit__(self, exc_type, exc_value, traceback):
        os.chdir(self.own_dir)
        
print("befor", os.getcwd())
with Cd("/home") as cd:
    print("inside", os.getcwd())
    
print("After", os.getcwd())
        
