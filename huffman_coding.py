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

def create_character_objects(freq):
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

if __name__ == "__main__":
    fileContent = read_file("./file.txt")
    print(fileContent)
    freqArr = create_frequencies(fileContent)
    charObjArr = create_character_objects(freqArr)
    print_character_array(charObjArr)
    minHeap = create_heap(charObjArr)
    # print_min_heap(minHeap)
    merge_nodes(minHeap)
    print(minHeap)