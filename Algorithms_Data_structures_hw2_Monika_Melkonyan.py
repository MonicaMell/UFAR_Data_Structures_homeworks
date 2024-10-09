def recursive_selection_sort(arr, n=None, index=0):
    if n is None:
        n = len(arr)


    if index >= n - 1:
        return

    min_index = index
    for i in range(index + 1, n):
        if arr[i] < arr[min_index]:
            min_index = i

    arr[index], arr[min_index] = arr[min_index], arr[index]
    recursive_selection_sort(arr, n, index + 1)

arr = [64, 25, 12, 22, 11]
recursive_selection_sort(arr)
print("Sorted array:", arr)


class CustomQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("dequeue from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("peek from empty queue")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

q = CustomQueue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print("Queue size:", q.size())
print("Front element:", q.peek())
print("Dequeued:", q.dequeue())
print("Queue size after dequeue:", q.size())

