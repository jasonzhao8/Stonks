# Stonks
# Inventory
# Jason Zhao
# Created: February 14 2020
# Modified: February 23 2020

# Displayed messages.
# These are the messages that will be displayed in junction with their
# corresponding lists when the user opens their inventory. Displayed at the end
# of the code.
inventory = ['profit', 'employees']
profit = "The current amount of money generated is: $"
employees = "The amount of active employees are:"

# Employees list.
# The user can add, remove and sort employees.
emp = ['E1', 'E2', 'E3', 'E4']
print("Original employee list:", f"{emp}")
emp.append('E5')
print("E5 has been hired and appended to the end of list:", f"{emp}")
emp.insert(0, 'E7')
print("E7 has been hired and inserted at the front of the list:", f"{emp}")
del emp[2]
print("Employee |E2| has been fired:", f"{emp}")
emp.reverse()
print("Current employee list has been reversed:", f"{emp}")
emp.sort()
print("Employees have been sorted in ascending order:", f"{emp}")
len(emp)

# Company profits.
# User can remove and sort the profits list.
prf = ['Gross', 'Taxes', 'Loans', 'Deductions']
print("Current profit includes:", f"{prf}")
print("Sorted list:", f"{sorted(prf)}")
prf.remove('Taxes')
print("Taxes have succesfuly been evaded:", f"{prf}")
popped_prf = prf.pop()
print("Deductions have also been evaded:", f"{prf}")

# Final print statements.
print("INVENTORY:", f"{inventory}")
print(f"{profit}13")
print("Employee list:"f"{emp}", ", # of current Employees:", f"{len(emp)}")
