'''Complete the insert function in your editor so that it creates a new Node (pass data as the Node constructor argument) and inserts it at the tail of the linked list referenced by the head parameter. Once the new node is added, return the reference to the head node
Sample Input

STDIN   Function
-----   --------
4       T = 4
2       first data = 2
3
4
1       fourth data = 1
Sample Output

2 3 4 1'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
        temp = Node(data)
        if head is None:
            head = temp
            return head
        current = head
        while current.next is not None:
            current = current.next
        current.next = temp
        return head  
    #Complete this method

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  