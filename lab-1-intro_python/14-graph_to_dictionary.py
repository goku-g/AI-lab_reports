import pprint

tree1 = {
    'A':['B', 'C'], 
    'B':['A','D', 'E'], 
    'C':['A', 'F'], 
    'D':['B', 'G'], 
    'E':['B', 'H'], 
    'F':['C'], 
    'G':['D'], 
    'H':['E']
}

tree2 = {
    'Biratnagar':[{'Itahari':22}, {'Biratchowk':30}, {'Rangeli':25}], 
    'Itahari':[{'Biratnagar':22}, {'Biratchowk':11}, {'Dharan':20}], 
    'Dharan':[{'Itahari':20}], 
    'Biratchowk':[{'Biratnagar':30}, {'Itahari':11}, {'Kanepokhari':10}], 
    'Rangeli':[{'Biratnagar':25}, {'Kanepokhari':25}, {'Urlabari':40}], 
    'Kanepokhari':[{'Biratchowk':10}, {'Rangeli':25}, {'Urlabari':12}], 
    'Urlabari':[{'Kanepokhari':12}, {'Rangeli':40}, {'Damak':6}], 
    'Damak':[{'Urlabari':6}]
}

print("")
pprint.pprint(tree1)
print("")
pprint.pprint(tree2)
print("")