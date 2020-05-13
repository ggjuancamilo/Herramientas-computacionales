wget https://raw.githubusercontent.com/ComputoCienciasUniandes/HerramientasComputacionalesDatos/master/Homework/hw1/01_notas.tsv
cat 01_notas.tsv
awk '{if(($4+$5+$6)>=9 && $3=="INGMEC") print $1,$2}' 01_notas.tsv
awk '{print $1,$2,$3,($4+$5+$6)/3}' 01_notas.tsv > 01.notafinal.tsv
cat 01.notafinal.tsv 
sort -n -k4,4  01.notafinal.tsv
