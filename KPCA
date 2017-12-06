import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import decomposition
import re
import matplotlib.transforms as mtransforms

df0=pd.read_csv("out_matrix_delete_0.csv")
df=df0.set_index(['pos'])
#print(df)

def load_data():
    return df.values,df.index

def test_KPCA(*data):
    X,y=data
    kernels=['linear','poly','rbf','sigmoid']
    for kernel in kernels:
        kpca=decomposition.KernelPCA(n_components=None,kernel=kernel)
        kpca.fit(X)
        print('kernel=%s --> lambdas: %s'%(kernel,kpca.lambdas_))

def plot_KPCA(*data):
    X,y=data
    kernels=['linear','poly','rbf','sigmoid']
    fig=plt.figure()
    
    names1=[re.sub(r'[a-zA-Z]+','',j.split(".")[0]) for j in y]
    names2=[float(re.sub(r':','.',k)) for k in names1]
    for i,kernel in enumerate(kernels):
        kpca=decomposition.KernelPCA(n_components=2,kernel=kernel)
        kpca.fit(X)
        X_r=kpca.transform(X)# 原始数据集转换到二维
        ax=fig.add_subplot(2,2,i+1) ## 两行两列，每个单元显示一种核函数的 KernelPCA 的效果图
        trans_offset = mtransforms.offset_copy(ax.transData, fig=fig,x=0.05, y=0.10, units='inches')
        for label ,name in zip( np.unique(y),names2):
            position=y==label
            ax.scatter(X_r[position,0],X_r[position,1])
            plt.text(X_r[position,0],X_r[position,1],'%s'%(name),transform=trans_offset)
        ax.set_xlabel("PCA1")
        ax.set_ylabel("PCA2")
        ax.set_title("kernel=%s"%kernel)
    plt.suptitle("KPCA")
    plt.show()

if __name__=='__main__':
    X,y=load_data() # 产生用于降维的数据集
    #test_KPCA(X,y)   # 调用 test_KPCA
    plot_KPCA(X,y)   # 调用 plot_KPCA
