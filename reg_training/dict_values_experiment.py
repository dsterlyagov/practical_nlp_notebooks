probe = {'intent': set()}
probe['intent'].add('1')
probe['intent'].add('2')
probe['intent'].add('3')
probe['intent'].add('1')
#res = sum(probe.keys())
print(len(probe['intent']))