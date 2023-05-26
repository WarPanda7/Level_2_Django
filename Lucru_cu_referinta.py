class Node:
  def __init__(self,value):
    self.value = value
    self.next = None
  def __str__(self)  :
    return f"[{self.value}]-- next --> {self.next}"
head=Node(100)

# Answer 1
head.next = Node(200)
print(head)
head.next.next = Node(300)
print(head)
head.next.next.next = Node(400)
print(head)
head.next.next.next.next = Node(500)
print(head)

#Answer 2
current_node=head
for i in range(2,6):
    new_node=Node(100*i)
    current_node.next=new_node
    current_node= new_node
    print(head)
