用styleGAN生成 20张1024*1024的人脸
```bash
python gui.py 
```

如果要编辑图片，进入editor文件夹
可以在五个维度进行编辑，分别是
年龄，性别，眼睛闭合程度，脸的宽度，笑容
```
cd editor
python editorgui.py   
```



必备库easygui,tensorflow,numpy等

model:
https://disk.pku.edu.cn/#/link/530D263C361C8C40B248C41B108931C4%20%E6%9C%89%E6%95%88%E6%9C%9F%E9%99%90%EF%BC%9A2020-07-11%2023:59
分别放入 /model/ 和 /editor/model/ 内

tips： 图像编辑可能需要大量显卡资源，在1070ti下可以跑出来 但是在1050好像就跑不出来了
