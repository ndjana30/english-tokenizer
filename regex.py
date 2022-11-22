import re
#pattern is 
#2 lower case letters
#between 1 to 3 digits
#2 upper case letters 
#one symbol



# class Regex():
#     def __init__(self):
        # self.pattern = re.compile("^[a-z]{2}[0-9]{1,3}[A-Z]{2}[^a-zA-Z0-9]{1}$")
#         print(self.pattern.search("rt45UI. rt45UI."))
#         print(self.pattern.search("r45DavE"))
# r=Regex()

class Regex():
    def __init__(self)->None:
        n=None
        try:
            self._sentence_pattern = re.compile("^[A-Z\s]+[a-z\s]+\.$")
            self._matching_string=self._sentence_pattern.search("My name is davy.")[0]
            print("matching sentence is \t" + self._matching_string)
            self.tokenize()
            self.classification()
        except:
            print("\t no matching sentence found")

    def tokenize(self)->list:
        self._tokens = self._matching_string.split()
        print(self._tokens)
    
    def classification(self)->str:
       
        self._noun_pattern=re.compile("^[A-Z|a-z]+[^0-9]+[^A-Za-z0-9]+$")
        for i in self._tokens:
            try:
                self._noun_pattern.search(i)[0]
                n=self._noun_pattern.search(i)[0]
                print("noun found\t"+n)
            except:
                print("no match for noun")
        # self._noun_pattern = re.compile("^[]$")


r=Regex()
# r.tokenize()
# r.classification()
