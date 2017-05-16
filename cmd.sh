for i in `ls -th |head -1`
do 
echo $i
a=`date`
echo $a >> $i
git add $i;git status;git commit -m "shenme";git push origin master;
echo "############"
echo "GIT SUCCESS"
echo "###########" 
done
#scp bioinfo@10.2.48.94:/home/bioinfo/liuqi/tool/script/get_gene.py .
