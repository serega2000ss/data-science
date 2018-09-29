import math
import time

## variant 1 (shity one)
#n = 10000
#data_set = [i for i in range(2,n+1)]
#start_time = time.time()
#for i in data_set:
    #k = 2
    #j = k*i
    #while j <= data_set[-1]:
        #if (j in data_set):
            #data_set.remove(j)
        #k += 1
        #j = k*i
#end_time = time.time()
#print(*data_set)
#print("--- %s seconds ---" % (time.time() - start_time))

# variant 2
n = 1000000
data_set = [True for i in range(2,n+1)]
start_time = time.time()
data_len = len(data_set)
for i in range(2,data_len):
    if data_set[i]:
        k = 2
        j = k*i
        while j < data_len:
            data_set[j] = False
            k += 1
            j = k*i
end_time = time.time()
for i in range(2,data_len):
    if data_set[i]:
        print(i)
print("--- %s seconds ---" % (time.time() - start_time))
