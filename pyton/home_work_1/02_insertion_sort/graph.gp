set title 'Insertion Sort'
set ylabel 'Time'
set xlabel 'Size'
set grid
set term png
set output 'insertion_sort.png'
plot 'insertion_sort.csv'
