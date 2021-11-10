reset
set terminal jpeg
set output "singledist.jpg"
set style fill solid 1.00 border 0
set style histogram
set style data histogram
set xtics rotate by -45
set grid ytics linestyle 1
#set yrange [0:25]
set xlabel "Quantile" font "bold"
set ylabel "time (ns)" font "bold"
plot "plt/singledist.dat" using 2:xtic(1) ti "Status: 'confirmed', 1000 matches, 2815 transactions" linecolor rgb "#FFFF00"
