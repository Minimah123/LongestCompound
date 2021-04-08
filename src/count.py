mport urllib.request as request
import time, sys

class data:
    def __init__(self, url):
        self.array = self.gettext(url)
        self.combination = []
            
    def gettext(self,url):
        webpage = request.urlopen(url)
        html = webpage.read()
        text = html.decode("utf-8")
        return sorted(text.split('\n'), key=len, reverse=True)

    def check_combination(self,i):
        word = self.array[i]
        unique_array = [x for x in self.array if x != word]
        for item in unique_array:
            word = word.replace(item, '')
            if len(word) == 0: return True
        return False

    def get_combinations(self):
        out = []
        item = list(map(lambda i:self.check_combination(i),range(0,len(self.array))))
        out = [self.array[x] for x in range(0,len(self.array)) if item[x] ]
        return out

    def get_longest(self):
        combs = self.get_combinations()
        print(f'All the combinations are: {combs}')
        if combs == []: print( 'No match Found')
        else: print(f'The longest combination is:  {max(combs, key=len)}')

# url = "https://gist.githubusercontent.com/bobbae/4ca309a1857158d5766d4ede4235cae0/raw/77d5e62835c80d30b87ab7f4a84a63a4a64f7cb2/words.txt"
url = None
try: url = sys.argv[1]
except: print('The url Location of the file is needed \n How to run: \"python3 src/count.py <the url>\" \n See ReadMe for more information')
if url:
    t1 = time.perf_counter()
    data(url).get_longest()
    t2 = time.perf_counter()
    print(f'Time elapsed is {t2-t1}')
