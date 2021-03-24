# control flow
- if, elif, else
- Conditional statements are used to control the flow of our program

### examples:
- if:  
  ```
  if age >= 15:
    print("Thank you, please proceed to your purchase")
  ```
  
- elif: 
    ```
  elif age < 15:
    print("You're too young to watch this movie")
  ```  
  
- else:
    ```
  else:
    print("something went wrong")
  ```
  
## For loops and while loops:
- ###are used to iterate through the data
- ###for loop
- ###while loop
- ###data sets

- example without using a loop:
```python
shopping_list = ["bread", "eggs", "milk", "orange"]
print(shopping_list[0]) 
print(shopping_list[1])
print(shopping_list[2])
print(shopping_list[3]) 
``` 

- for loop syntax example:
```python
  for items in shopping_list:
    print(items)
```
  
- break: 
```python
for items in shopping_list:
    print(items)
    if items == "milk": 
        break 
```
- looping through dictionary with a list:
```python
for items in food_bill.values():
    print("name:", items["name"] + ",", "bill:", items["bill"])
```

- ##while loop:








