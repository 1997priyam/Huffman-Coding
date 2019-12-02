class Character:
    def __init__(self, ucode, freq):
        self.ucode = ucode
        self.freq = freq

class MinHeap:
    def __init__(self):
        self.size = 0

    def extract_min(self):
        pass

    def insert(self):
        pass

    def shift_up(self):
        pass

    def shift_down(self):
        pass

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
            obj = Character(ucode, freq)
            charObjArr.append(obj)
    return charObjArr

def print_character_array(charObjArray):
    for i in charObjArray:
        print("Character Ucode: {}  Frequency: {}".format(i.ucode, i.freq))

if __name__ == "__main__":
    fileContent = read_file("./file.txt")
    print(fileContent)
    freqArr = create_frequencies(fileContent)
    charObjArr = create_character_objects(freqArr)
    print_character_array(charObjArr)