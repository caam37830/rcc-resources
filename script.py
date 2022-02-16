from time import sleep

# A test script
for i in range(10):
  print(i)

# wait a bit
sleep(10)
  
# throw an error
raise AssertionError("Some error occured!")
