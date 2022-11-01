class hashtable:
    def __init__(self):
        self.size = 100
        self.arr = [[] for i in range(self.size)]

    def hash(self,key):
        return key%self.size
    def put(self,key,value):
        h=self.hash(key)
        self.arr[h].insert(key,value)
    def get(self,key):
        h=self.hash(key)
        value=self.arr[h]
        return value

object = hashtable()
object.put(1,5)
object.put(2,8)
print(object.get(1))
print(object.get(2))