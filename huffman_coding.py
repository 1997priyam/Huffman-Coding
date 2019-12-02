import heapq

class Node:
    def __init__(self, ucode, freq, left=None, right=None):
        self.ucode = ucode
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

    def __gt__(self, other):
        return self.freq > other.freq

def read_file(filePath):
    with open(filePath) as f:
        text = f.read()
    return text

def create_frequencies(text):
    frequncies = [0]*256
    for i in text:
        frequncies[ord(i)] += 1
    return frequncies

def create_character_objects_array(freq):
    charObjArr = []
    for ucode, freq in enumerate(freq):
        if(freq != 0):
            obj = Node(ucode, freq)
            charObjArr.append(obj)
    return charObjArr

def print_character_array(charObjArray):
    for i in charObjArray:
        print("Character Ucode: {}  Frequency: {}".format(i.ucode, i.freq))

def create_heap(charObjArr):
    # minHeap = []
    # for node in charObjArr:
    #     heapq.heappush(minHeap, (node.freq, node))
    # return minHeap
    heapq.heapify(charObjArr)
    return charObjArr

def print_min_heap(minHeap):
    while minHeap:
        node = heapq.heappop(minHeap)
        print("Character frequency: {}, Character: {}".format(node.freq, chr(node.ucode)))

def merge_nodes(minHeap):
    while len(minHeap) > 1:
        left = heapq.heappop(minHeap)
        right = heapq.heappop(minHeap)

        newFreq = left.freq + right.freq
        newNode = Node(ucode=None, freq=newFreq, left=left, right=right)
        heapq.heappush(minHeap, newNode)

def generate_code(key, tree, result):
    if tree == None:
        return
    if tree.ucode == key:
        return
    result.append("0")
    generate_code(key, tree.left, result)
    result.append("1")
    generate_code(key, tree.right, result)
    result.pop()

def create_dict_of_codes(newCharObjArr, tree):
    code_dict = {}
    for node in charObjArr:
        code_dict[chr(node.ucode)] = generate_code(node.ucode, tree, result=[])
    return code_dict

if __name__ == "__main__":
    fileContent = read_file("./file.txt")
    print(fileContent)
    freqArr = create_frequencies(fileContent)       #creating the frequency array of type [1, 2, 5, 0, 10, 18.......] 256 indexes 0-255
    charObjArr = create_character_objects_array(freqArr)   # creates the array of nodes [node1, node2, node3....] All nodes with freq>0
    # print_character_array(charObjArr)
    minHeap = create_heap(charObjArr)           # Heapifys the node array to create a min Heap
    # print_min_heap(minHeap)
    merge_nodes(minHeap)        # Merges all the nodes in the min heap so that only one node is remaining which is a tree consisting of all other nodes
    print(minHeap)
    newCharObjArr = create_character_objects_array(freqArr)     # creates a new character array to lookup in the tree generated
    print_character_array(newCharObjArr)
    code_dict = create_dict_of_codes(newCharObjArr, minHeap[0])        # generates code corresponding to each unique chracter