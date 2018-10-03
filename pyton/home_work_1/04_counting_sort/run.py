import math
import time
import random
import csv

def main(start=10, step=10, count=2000):
  with open('counting_sort.csv', mode='w') as csv_file:
    fieldnames = ['items_coutn', 'time_to_run']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    n = start
    for i in range(count):
      print("run fo n: %d" % n)
      max_limit = n-1
      data_set = [random.randint(1,max_limit) for i in range(n)]
      result_data = countingSort(data_set, max_limit)
      writer.writerow({'items_coutn': (' %5.5f' % n), 'time_to_run': (' %5.5f' % result_data[1])})
      n += step


def countingSort(data_set, max_limit):
  start_time = time.time()
  data_len = len(data_set)-1
  result = [1 for i in range(max_limit+1)]
  tmp = [0 for i in range(max_limit+1)]
  for j in range(data_len):
    tmp[data_set[j]] += 1
  for i in range(1,max_limit+1):
    tmp[i] = tmp[i] + tmp[i-1]
  for j in reversed(range(data_len)):
    result[tmp[data_set[j]]] = data_set[j]
    tmp[data_set[j]] = tmp[data_set[j]] - 1
  end_time = time.time()
  return result, (time.time() - start_time)

main()
