
class Node:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value, next_node = None):

        self.next = next_node
        self.key = key
        self.value = value
        self.entry = (key, value)

    def __repr__(self):
        return str(self.entry)
    # returns the index of the value in the entry tuple
    def get_value(self):
        return self.value
    # returns the index of the key in the entry tuple
    def get_key(self):
        return self.key
    # returns the next node or None
    def get_next(self):
        return self.next

    #sets the next node
    def set_next(self, new_next):
      self.next = new_next

class LinkedList:
    def __init__(self):

        self.head = None

    def __repr__(self):
        currStr = ""
        curr = self.head
        while curr is not None:
            currStr += f'{str(curr.entry)}'
            curr = curr.next
        return currStr


    def add_to_head(self, node):
        #if there is no head head becomes the node
        if self.head == None:
            self.head = node
        else:
            #set head to the node and the pointer to the current head
            curr = self.head
            self.head = node
            node.set_next(curr)


    def delete(self, key):
        curr = self.head
        if curr != None:
            if curr.key == key and self.head.next ==None:
                self.head = None
            prev = curr
            curr = curr.next
            while curr != None:
                if curr.key == key:
                    prev.next = curr.next
                    curr = None
                else:
                    prev = curr
                    curr = curr.next


    def find(self, key):
        curr = self.head
        while curr is not None:
            if curr.key == key:
                return curr
            curr = curr.next
        return "No such element Exists"
    # Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity = MIN_CAPACITY):
        # Your code here
        self.capacity = capacity
        self.num_elements = 0
        self.table = [None] * self.capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.table)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.elements // get_num_slots()

    def fnv1(self, key):
        """h
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for x in key:
            hash = (( hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        #finding the index we are working with
        index = self.hash_index(key)
        if self.table[index] == None:
            ll = LinkedList()
            ll.add_to_head(Node(key, value))
            self.table[index] = ll

        else:
            if self.table[index].find(key) == None:
                self.table[index].head = Node(key, value)
            curr = self.table[index].head
            self.table[index].add_to_head(Node(key, value))


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        if self.table[index] != None:
            self.table[index].delete(key)


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        if self.table[index]:
            curr = self.table[index].head
            while curr != None:
                if curr.key != key:
                    curr = curr.get_next()
                else:

                    return curr.value
        else:
            return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        # setting varible for old table
        old_table = self.table
        #creating new table filled with a number of None values equal to the new_capacity
        self.table = [None] * new_capacity
        #iterate through the old table
        for ll in old_table:
            #if the ll still has a head
            while ll.head != None:

                #value for key to pass through the hash_index and store in the new list
                key = ll.head.key
                #value for value to store in new node
                value = ll.head.value
                #set index to check entry at index of new table
                index = self.hash_index(key)
                #value for index we are operating on in new table
                entry = self.table[index]
                #if nothing is stored there
                if entry is None:
                    #make a linked list
                    new_ll = LinkedList()
                    #add a node to head
                    new_ll.add_to_head(Node(key, value))
                    #set index to new_ll
                    self.table[index] = new_ll
                    #checking if any other elements are in the linked list
                    if ll.head.get_next()!= None:
                        #set variables forhandling other variables in list
                        curr = ll.head
                        next = ll.head.get_next()
                        #removing the current head and setting next to head
                        ll.delete(curr.key)
                        ll.head = next
                        print(f'current: {ll.head}')
                    else:
                        ll.head = ll.head.get_next()


                    print(f'self.table[index] after creating linked list and new node: {self.table[index]}')
                else:

                    entry.add_to_head(Node(key, value))
                    if ll.head.get_next()!= None:
                        curr = ll.head
                        next = ll.head.get_next()
                        ll.delete(curr.key)
                        ll.head = next
                    else:
                        ll.head = ll.head.get_next()




if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))
    # Test resizing


    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()
    print(f"\nResized from {old_capacity} to {new_capacity}.\n")
    print(ht.table)

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
