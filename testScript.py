# Brief:  Test script for sample Python module mymodule 
#
#==================================================
import mymodule as m

print("\n ==== Call function: returnTuple ====\n")
tpl = m.returnTuple(3.5, 4.2, 10)
print("tupl = ", tpl)


print("\n ==== Call function: returnDictionary ====\n")
d = m.returnDictionary(3.5, 4.2, 10)
print("d = ", d)

print("\n ==== Call function: computeStatistics ====\n")

xs = [4, 1.2, 9.5, 10.5, 3.4, 5.10, 6.0]
print("xs = ", xs)

m.computeStatistics(xs)

print("\n\n==== End of Testing =========\n")
