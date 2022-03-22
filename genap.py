class genap: 
    def __init__(n):
        n.items=[]
    def enqueue(n,item):
        n.items.insert(0,item) 
    def dequeue(n):
        return n.items.pop() 
    def semua(n):
        return n.items

q = genap()
q.enqueue(3)
q.enqueue(4)
print(q.semua())
print(q.dequeue(), "Bukan bilangan genap")
print(q.dequeue(), "Adalah Bilangan genap")
   
