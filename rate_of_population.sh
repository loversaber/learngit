endpath=/home/bioinfo/liuqi/ped/info/test/loc

for d in `ls -d *_1/`
do
echo $d
cd $d
a=${d%%_*}
touch end
for i in `ls [A-Z]*`
do
awk '{getline;print($1)}' $i >> end
done
n=`ls [A-Z]*|wc -l`

awk -v m=$n '{a[$1]++}END{for(i in a)print(i,a[i]/m)}' end |sort -nk2,2|tail -10|sort -nk1,1|awk '{printf("%d\t%.2f\n",$1,$2)}' > $a".loc"
mv $a".loc" $endpath
rm end 
#$a".loc"

cd ..
done


awk 'split($0,a,"_");b=a[1]{print(b)}' dir_name|sed '/.*_1/d'|awk 'BEGIN{printf "pos\t"}{printf $0"\t"}END{printf"\n"}' > final2

perl $endpath/paste.pl $endpath/../share_total_location $endpath/*.loc >> final2;
less -S final2
2017年 5月17日 星期三 16时43分06秒 CST
