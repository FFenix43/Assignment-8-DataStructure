class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''
    def __init__(self, name, number):
        self.name = name
        self.number = number
    def __str__(self):
        return f'{self.name}: {self.number}'

     # Delete this line when implementing the class

class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next
    
    
    
     # Delete this line when implementing the class

class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    def __init__(self, size: int =10):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
        ascii_sum = sum(ord(char) for char in key)
        return ascii_sum % self.size

    def insert(self, key: str, value: str) -> None:
        index = self.hash_function(key)
        current = self.data[index]

        while current:
            if current.key ==key:
                current.value.number = value
                return
            current = current.next
        
     
        new_contact = Contact(key, value)
        new_node = Node(key=key, value=new_contact, next=self.data[index])
        self.data[index] = new_node


    def search(self, key: str) -> Contact | None:
        index = self.hash_function(key)
        current = self.data[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next

    def print_table(self) -> None:
        for i in range(self.size):
            chain = []
            current = self.data[i]
            while current:
                chain.append(f"[{current.value.name}: {current.value.number}]")
                current = current.next

            chain_str = " -> ".join(chain) if chain else "Empty"
            print(f"Index {i}: {chain_str}")

     
     # Delete this line when implementing the class

# Test your hash table implementation here.  
'''
contact1 = Contact("Riley", "123-456-7890")
print(contact1) 

node1 = Node(contact1.name, contact1)
print(node1.key)
print(node1.value)
print(node1.next)
'''
table = HashTable(10)
table.print_table()


'''
Index 0: Empty
Index 1: Empty
Index 2: Empty
Index 3: Empty
Index 4: Empty
Index 5: Empty
Index 6: Empty
Index 7: Empty
Index 8: Empty
Index 9: Empty 
'''
# Add some values
table.insert("John", "909-876-1234")
table.insert("Rebecca", "111-555-0002")
# Print the new table structure 
table.print_table()
'''
Index 0: Empty
Index 1: Empty
Index 2: Empty
Index 3: Empty
Index 4: Empty
Index 5: Empty
Index 6: Empty
Index 7: - Rebecca: 111-555-0002 
Index 8: Empty
Index 9: - John: 909-876-1234 
'''
# Search for a value
contact = table.search("John") 
print("\nSearch result:", contact)  # Search result: John: 909-876-1234 


table.insert("Amy", "111-222-3333") 
table.insert("May", "222-333-1111")
table.print_table()

# Edge Case #2 - Duplicate Keys 
table.insert("Rebecca", "999-444-9999")  # Should update Rebecca's number 
table.print_table()

print(table.search("Chris")) # None


'''
The hash table is the right structure for fast look-ups, because its formula is very efficient and it is almost instantly as to look up the values needed. It translates a key directly into a specific memory address where the target data resides, ignoring the need to iterate through every item. By doing so, it eliminates the need to compare every value to reach the required value.
The collisions were handled using separate chaining with linked lists. When two different contact names hash to the exact same array index, the new contact is wrapped in a Node and appended to the linked list residing at that index. In the insert and search operations, the code calculates the target index and navigates the linked list node by node, matching the contact name key. If the name already exists during insertion. Its pgone number updates in place, and a new node attaches to the front of the chain.
An engineer would choose a hash table over a list or tree when the structure of the code needs fast lookups to avoid delays in the user experience. Furthermore, if he also needs to have quick insertions or deletions of values, the hash table is optimal for these kinds of problems. This makes them ideal for this type of data structure in high-performance applications such as database indexing or real-time duplicate detection.


'''