tree1 = {
    'A':['B', 'C'], 
    'B':['A','D', 'E'], 
    'C':['A', 'F'], 
    'D':['B', 'G'], 
    'E':['B', 'H'], 
    'F':['C'], 'G':['D'], 
    'H':['E']
}

tree2 = {
    'Biratnagar':['Itahari', 'Biratchowk', 'Rangeli'], 
    'Itahari':['Biratnagar', 'Biratchowk', 'Dharan'], 
    'Dharan':['Itahari'], 
    'Biratchowk':['Biratnagar', 'Itahari', 'Kanepokhari'], 
    'Rangeli':['Biratnagar', 'Kanepokhari', 'Urlabari'], 
    'Kanepokhari':['Biratchowk', 'Rangeli', 'Urlabari'], 
    'Urlabari':['Kanepokhari', 'Rangeli', 'Damak'], 
    'Damak':['Urlabari']
}

tree2_wt = {
    ['Biratnagar', 'Itahari']: 22,
    ['Biratnagar', 'Biratchowk']: 30,
    ['Biratnagar', 'Rangeli']: 25,
    ['Itahari', 'Biratchowk']: 11,
    ['Itahari', 'Dharan']: 20,
    ['Biratchowk', 'Kanepokhari']: 10, 
    ['Rangeli', 'Kanepokhari']: 25,
    ['Rangeli', 'Urlabari']: 40, 
    ['Kanepokhari', 'Urlabari']: 12, 
    ['Urlabari', 'Damak']: 6,
}