import math
import time
import random
import csv

def main(start=10, step=10, count=1000):
  with open('insertion_sort.csv', mode='w') as csv_file:
    fieldnames = ['items_coutn', 'time_to_run']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    #writer.writeheader()
    n = start
    for i in range(count):
      print("run fo n: %d" % n)
      result_data = insertion_sort([random.randint(1,n) for i in range(n)])
      writer.writerow({'items_coutn': (' %5.5f' % n), 'time_to_run': (' %5.5f' % result_data[1])})
      n += step


def insertion_sort(data_set):
  n = len(data_set)
  start_time = time.time()
  for i in range(1,n):
    key = data_set[i]
    j = i-1
    while (j >= 0) and (data_set[j] > key):
      data_set[j+1] = data_set[j]
      j -= 1
    data_set[j+1] = key
  end_time = time.time()
  return data_set, (time.time() - start_time)


main()
