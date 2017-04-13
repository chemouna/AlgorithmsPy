class TwoStacks:
    def __init__(self, n):
        self.size = n
        self.arr = [None] * n
        self.top1 = -1
        self.top2 = self.size

    def push1(self, x):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = x
        else:
            print("Stack Overflow")
            exit(1)

    def push2(self, x):
        if self.top1 < self.top2 - 1:
            self.arr[self.top2] = x
            self.top2 -= 1
        else:
            print("Stack Overflow")
            exit(1)

    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 -= 1
            return x
        else:
            print("Stack Underflow ")
            exit()

    def pop2(self):
        if self.top2 >= 0:
            x = self.arr[self.top2]
            self.top2 -= 1
            return x
        else:
            print("Stack Underflow ")
            exit()


ts = TwoStacks(5)
ts.push1(5)
ts.push2(10)
ts.push2(15)
ts.push1(11)
ts.push2(7)

gst
