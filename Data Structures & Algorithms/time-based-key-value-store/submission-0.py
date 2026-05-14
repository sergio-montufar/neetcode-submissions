class TimeMap:
    
    def __init__(self):
        self.hashmap = {} # key : [value, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        values = self.hashmap.get(key, [])
        left, right = 0, len(values)-1
        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] <= timestamp:
                ans = values[mid][0]
                left = mid + 1
            elif values[mid][1] > timestamp:
                right = mid - 1

        return ans
        
