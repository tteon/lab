# heap

print( 5 // 2 ) # 2 몫
print( 5 % 2 ) # 1 나머지

class BinaryHeap(object):
    def __init__(self):
        self.items = None

    def __len__(self):
        return len(items) - 1 

    # 삽입 시 실행, 반복 구조 구현
    def _percolate_up(self):
        i = self(len)
        # i (대상 값의 인덱스) 의 부모 노드는 2로 나눈 값의 몫임.
        parent = i // 2
        # recursion , parent > 0 이라는 것은 결국 
        while parent > 0 :
            if self.items[i] > self.items[parent]:
                self.items[parent], self.items[i] = \
                    self.items[i], self.items[parent]
            i = parent
            parent = i // 2

    def insert(self, k):
        self.items.append(k)
        self._percolate_up()
    
    def _percolate_down(self, idx):
        left = idx * 2
        right = idx * 2 + 1
        smallest = idx

        if left <= idx and self.items[left] < self.items[smallest]:
            smallest = left
        
        if right <= idx and self.items[right] < self.items[smallest]:
            smallest = right

        if smallest != idx:
            self.items[idx], self.items[smallest] = \
                self.items[smallest], self.items[idx]
            self._percolate_down(smallest)
        
    def extract(self):
        extracted = self.items[1]
        self.items[1] = self.items(len(self))
        self.items.pop()
        self._peroclate_down(1)
        return extracted

