#python #programming #notes 

### List comprehension:

List comprehension is a fancy way of making lists where we run loops, conditionals etc in just one line . This is massively helpful to make the code much more efficient especially once you understand it well. example
```python

num=[1,2,3,4,5,6]

#without list comprehension
squares = []
for n in num :
	squares.append(n*n)
#with list comprehension
squares=[n*n for n in num]
```

This gets especially helpful when dealing a list of lists . for eg:
```python
#lets define a list of lists which represent tempereture readings of 3 floors of a set of houses

temps=[[25,27,23],[27,18,17],[12,13,14]]

#lets say now we wanna make a list of the lowes tempresture from each house 

#without comprehension it looks like 
low = []
for temp in temps:
	low.append(min(temp))

#with list comprehension
low_comp = [min(temp) for temp in temps]	
```

### Dictionary Comprehension:
Its essentially the same idea as the lists but here you can do it with a dictionary . for eg:
if we have to make a dictionary where the keys are numbers and their values are their squares.
```python
num=[1,2,3,4,5,6]
#normal way 
squares_dict={}
for n in num:
	squares_dict[n]=n*n
#with comprehension
squares_dict={n:n*n for n in num}
```

example 2 :
lets say we have a list of items and prices in a dictionary . and we want to format the itemnames and find the taxed rate of the items .
```python 
item_prices={"book":10,"pen":5,"ink":3}
#normal way 
taxed_prices={}
for key, value in item_prices.items():
	new_key=key.capitalize()
	new_value=round(value*1.13)
	taxed_prices[new_key]=new_value
#with comprehension 
taxed_prices={key.capitalize():round(value*0.13) for key,value in item_prices}
```

### example
useful code-block to further understand use case in real problems:

```python
#Function to converte a list of objects into a table 
from typing import Dict

def tabulate(books:Dict):

headers = ["id","title","author","finish_date"]

col_widths={h:len(str(h)) for h in headers}#this will make a dictionary where {header1:its length,header2 :its length}

for book in books:

for header in headers:

cell=str(getattr(book,header))

col_widths[header]=max(len(cell),col_widths[header])

#by the end of this loop the col_widths will have the maximum length of any cell within each different column

header_row=(" | ").join(str(h).ljust(col_widths[h])for h in headers)

#this adjusts the headers such that spaces are added so the length of the header matches its coresponding max lenght value form col_widths

lines=[]

lines.append(header_row)

seperator = "-+-".join("-"* col_widths[h] for h in headers)

lines.append(seperator)

for book in books:

line=" | ".join(str(getattr(book,h)).ljust(col_widths[h]) for h in headers)

lines.append(line)

return "\n".join(lines)
```