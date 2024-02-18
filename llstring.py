class LLString:
    class Node:
        def __init__(self, val, next):
            self.val = val
            self.next = next

    def __init__(self, s):
        self.head = None
        self.tail = None

        for char in s:
            self.append(char)

    def append(self, new_val):
        new_node = LLString.Node(new_val, None)

        if self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node

        if self.head is None:
            self.head = new_node

    def print(self):
        trav = self.head
        while trav is not None:
            print(trav.val, end='')
            trav = trav.next
        print()

    def to_string(self):
        s = ''
        trav = self.head
        while trav is not None:
            s += trav.val
            trav = trav.next
        return s

    def print_every_other(self):
        return self.__print_every_other(0, self.head)
        pass

    def __print_every_other(self,counter, node):
        if node is None:
            return print()
        else:
            if counter % 2 == 0:
                print(node.val, end='')
                return self.__print_every_other(counter + 1, node.next)
            else:
                return self.__print_every_other(counter + 1, node.next)
            

    def char_at(self, i):
        trav = self.head
        prev = None
        num = 0
        if trav == None:
            return None
        
        while num < i:
            prev = trav
            trav = trav.next
            num += 1
            if trav == None:
                return None
        return trav.val
        pass

    def concat(self, other_llstring):
        current_str = ''
        trav = self.head
        while trav is not None:
            current_str += trav.val
            trav = trav.next
        
        incoming_str = ''
        new_trav = other_llstring.head
        while new_trav is not None:
            incoming_str += new_trav.val
            new_trav = new_trav.next
        
        return current_str + incoming_str


    def reverse(self):
        head = self.head.next
        prev = self.head
        temp = prev
        while prev is not None:
            prev = head
            head = temp
            prev = prev.next
            head = head.next
            if head == None:
                head = prev
        
        pass

    def index_of(self, c):
        return self.__index_of(c, self.head)
    
    def __index_of(self, c, node):   
        
        if node == None:
            return -1
        
        if node.val == c:
            return 0
        else:
            return 1 + self.__index_of(c, node.next)
    


mylist = LLString('hello')
mylist2 = LLString('orange')
print(mylist.concat(mylist2))