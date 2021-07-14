
class HashTable(object):
    def __init__(self):
        self.size = 8
        self.slots = [None] * self.size

    def put(self, key):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
        else:
            if self.slots[hashvalue] == key:
                pass
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    
                else:
                    pass


    def hashfunction(self, key, size):
        consonants = 0
        digits = 0
        for x in key:
            if x.isdigit():
                digits += int(x)
            else:
                consonants += ord(x)

        return (consonants - digits) % 8

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))
        stop = False
        found = False
        position = startslot

        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = position

            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True

        return data

if __name__ == "__main__":
    h = HashTable()
    h.put("3C2SE11")
    h.put("8B41")
    h.put("DE4Z23DA")
    h.put("J4")
    h.put("6GOJE45")
    print("Position of 3C2SE11:",h.get("3C2SE11"))
    print("Position of 8B41:",h.get("8B41"))
    print("Position of DE4Z23DA:",h.get("DE4Z23DA"))
    print("Position of J4:",h.get("J4"))
    print("Position of 6GOJE45:",h.get("6GOJE45"))
    
    