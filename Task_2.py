names = ['Artem', 'Boris', 'Michael', 'John']
money = [10, 20, 30, 40]
percent = ['10.25%', '12.25%', '11.25%', '9.25%']

dict = {name: money / 100 * perc for name, money, perc in zip(names, money, (float(j[:-1]) for j in percent))}

print(dict)