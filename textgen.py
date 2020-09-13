import pickle
import random
import re
import os
import argparse
class Textgen:
    def __init__(self):
        self.slova={}
        self.text=''
    def fit(self, path):
        for fname in os.listdir(path):
            with open(path+ '\\' + fname, 'r', encoding="utf-8") as f:
                self.text+=f.read()
            self.text+=' '
        words=re.sub(r'[^\w\.,\?!-:]', ' ', self.text).lower().split()
        for i in range(len(words)-1):
            self.slova[words[i]]=[]
        for i in range(len(words)-1):
            self.slova[words[i]].append(words[i+1])
            
    def generate(self, rnd_seed, len_p):
        now=random.choice(list(self.slova.keys()))
        out=now
        random.seed(rnd_seed)
        for i in range(len_p):
            now=random.choice(self.slova[now])
            out+=' '+now
        out+='.'
        print(out)

