from testmodule1 import testclass
from testmodule2 import testclass2
from rng import rng

print("Initial RNG state")
print(rng.bit_generator.state)

testobject1 = testclass()

print("First object")
print( testobject1.printResult() )

testobject2 = testclass2()
print("Second object")
print( testobject2.printResult() )

print("Final RNG state")
print(rng.bit_generator.state)
