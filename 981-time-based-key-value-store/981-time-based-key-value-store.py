class TimeMap:

    def __init__(self):
        self.val={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.val:
            self.val[key][timestamp]=value
        else:
            self.val[key]={timestamp:value}

    def get(self, key: str, timestamp: int) -> str:
        if key in self.val:
            for t in range(timestamp,-1,-1):
                if t in self.val[key]:
                    return self.val[key][t]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)