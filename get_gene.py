from sys import argv
#path=/home/bioinfo/liuqi/xianliti/homo/human/gene_number
#python3.4 get_gene.py $path/hhhhhhhhh $path/CHINA.only |uniq -c|sort -k1
with open(argv[1],"r") as f:
 d={}
 for line in f:
  line=line.strip()
  item=line.split("\t")
  gene=item[0]
  pos=item[1:3]
  d[gene]=pos
with open(argv[2],"r") as f2:
 l=[]
 for line in f2:
  line=int(line.strip())
  l.append(line)



for k in d.keys():
 v=d[k]
 n1=int(v[0])
 n2=int(v[1])
 for j in l:
  if n1<j<n2:
   print(k)
2017年 5月16日 星期二 21时12分49秒 CST
