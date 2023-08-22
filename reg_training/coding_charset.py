
text = '+'+b"\xc2\xa0\xc2\xa0".decode(encoding='utf-8') + '1'
print(text)
import random
import sys
import re
from contextlib import suppress
#sys.stdin = open(sys.stdin.fileno(), encoding='utf-8')
with open(sys.stdin.fileno(), encoding='utf-8') as f:

    for line in f:
        line = re.sub(r'\t', ' ', line)
        mas = [word for word in re.sub(r'[^A-Za-z\s]','',line).strip().lower().split(' ') if word]
        with suppress(IndexError):
            for i in range(len(mas)):
                print(f'{mas[i]}_{mas[i+1]}'.encode('utf-8'), 1, sep='\t')
                 #print(u'mas[i]', 1, sep='\t')