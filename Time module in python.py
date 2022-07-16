import time
initial_time=time.time()
print(time.process_time())

k=0
while(k<150000):
    # print("This is in while Loop")
    k=k+1
print("Time taken by while loop:",time.time()-initial_time,"seconds")
initial_time2=time.time()
for i in range(150000):
    # print("This is in for Loop")
    pass
print("Time taken by while loop:",time.time()-initial_time2,"seconds")