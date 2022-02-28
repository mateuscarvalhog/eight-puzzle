class PriorityQueue:
    def __init__(self):
        self.queue = list()

    def put(self, item: tuple):
        priority, _ = item

        if self.size() == 0:
            self.queue.append(item)
        else:
            for i in range(0, self.size()):
                another_item_priority, _ = self.queue[i]

                if priority >= another_item_priority:
                    if i == (self.size() - 1):
                        self.queue.insert(i+1, item)
                    else:
                        continue
                else:
                    self.queue.insert(i, item)
                    return True

    def get(self):
        _, element = self.queue.pop(0)
        return element

    def size(self):
        return len(self.queue)

    def empty(self):
        return len(self.queue) == 0