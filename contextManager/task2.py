import os
import tempfile
from shutil import rmtree

class TempDir:
    def __enter__(self):
        self.own_dir = os.getcwd()
        self.temp_dir = tempfile.mkdtemp()
        os.chdir(self.temp_dir)
        return self.temp_dir
    
    
    def __exit__(self, ext_type, ext_value, traceback):
        os.chdir(self.own_dir)
        rmtree(self.temp_dir)
        
print("Before", os.getcwd())
with TempDir() as tm:
    print("Inside", os.getcwd())
        
print("After", os.getcwd())
        


        