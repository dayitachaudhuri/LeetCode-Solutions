class MyCalendar:

    def __init__(self):
        self.bookings=[]
        self.n=0

    def book(self, start: int, end: int) -> bool:
        i=0    
        while i<self.n and self.bookings[i][0]<end:
            i+=1
        if self.n==0:
            self.bookings.append([start,end])
            self.n+=1
            return True
        if i==0:
            self.bookings.insert(0,[start,end])
            self.n+=1
            return True
        if self.bookings[i-1][1]<=start:
            self.bookings.insert(i,[start,end])
            self.n+=1
            return True
        return False
        

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)