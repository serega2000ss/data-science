import math
import time
import random
import csv

def main(start=10, step=10, count=2000):
  #n = 10
  #data_set = [random.randint(1,n) for i in range(n)]
  #print(*data_set)
  #quickSort(data_set)
  #print(*data_set)
  with open('quicksort.csv', mode='w') as csv_file:
    fieldnames = ['items_coutn', 'time_to_run']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    n = start
    for i in range(count):
      print("run fo n: %d" % n)
      start_time = time.time()
      quickSort([random.randint(1,n) for i in range(n)])
      end_time = time.time()
      writer.writerow({'items_coutn': (' %5.5f' % n), 'time_to_run': (' %5.5f' % (end_time - start_time))})
      n += step

def quickSort(data_set):
  quickSortHelper(data_set, 0, len(data_set)-1)

def quickSortHelper(data_set, p, q):
  if p < q:
    i = quickSortPartition(data_set, p, q)
    quickSortHelper(data_set, p, i-1)
    quickSortHelper(data_set, i+1, q)

def quickSortPartition(data_set, p, q):
  x = data_set[q]
  i = p-1
  for j in range(p, q-1):
    if data_set[j] <= x:
      i += 1
      data_set[i], data_set[j] = data_set[j], data_set[i]
  data_set[i+1], data_set[q] = data_set[q], data_set[i+1]
  return i+1



main()
