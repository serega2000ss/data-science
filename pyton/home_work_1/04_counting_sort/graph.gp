set title 'Counting Sort'
set ylabel 'Time'
set xlabel 'Size'
set grid
set term png
set output 'counting_sort.png'
plot 'counting_sort.csv'
