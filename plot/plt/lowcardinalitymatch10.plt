reset
set terminal jpeg
set output "lowcardinalitymatch10.jpg"
set style fill solid 1.00 border 0
set style histogram
set style data histogram
set xtics rotate by -45
set grid ytics linestyle 1
#set yrange [0:25]
set xlabel "Quantile" font "bold"
set ylabel "time (ns)" font "bold"
plot "plt/lowcardinalitymatch10.dat" using 2:xtic(1) ti "To: 10 addresses, 100% matche, 2815 transactions" linecolor rgb "#FF00FF"
