class FileSize():
    def __init__(self, bytes):
        self.bytes = bytes

    @property
    def bytes(self):
        return self._bytes

    @bytes.setter
    def bytes(self, value):
        if value < 0:
            raise ValueError("ValueError: Size must be >= 0")
        self._bytes = value

    @property
    def kilobytes(self):
        return round(self._bytes /1024, 2)
    
    @property
    def megabytes(self):
        return round(self._bytes /(1024**2), 9)


f = FileSize(2048)

print(f.bytes)      # 2048
print(f.kilobytes)  # 2.0
print(f.megabytes)  # 0.001953125

f.bytes = 1048576
print(f.megabytes)  # 1.0

#f.bytes = -100      # ❌ ValueError: Size must be >= 0
