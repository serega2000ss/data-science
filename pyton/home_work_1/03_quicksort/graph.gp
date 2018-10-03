set title 'QuickSort'
set ylabel 'Time'
set xlabel 'Size'
set grid
set term png
set output 'quicksort.png'
plot 'quicksort.csv'
