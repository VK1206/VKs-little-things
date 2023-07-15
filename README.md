# FZ-2021-class-10-random
附中2021级高二十班随机点名器  ★2.0版本已更新!

本人自制点名程序，能随机点到十班53个人中的任何一个  

.exe程序无需安装Python环境，在Windows电脑上点击即可运行  

其他为源码  

此项目允许二创，把源码下载下来，将里面的学生名更换为你的班级的即可  

如果要将.py程序打包成.exe程序，你需要安装pyinstaller  


安装pyinstaller:  

1.在cmd窗口运行如下命令(前提是你已安装Python运行环境)  

```pip install pyinstaller```  
  
2.执行  

```pyinstaller XXX.py```  
  
（默认在生成的dist文件夹里会生成好几个文件，如果想要只生成一个.exe文件在pyinstaller和XXX.py之间加上--onefile即可）  

# 2.0版本更新!!!(New)
★有了独立界面，不再只是一个CMD窗口

★增加了抽取和重新抽取的按钮，不需要关掉程序再抽取了

★最重要的!现在可以对抽取元素进行权重设置!但程序需要一个名为"names.ini"的文件才能运行

ini文件里要写的内容如下
```
[元素1]

weight = 5


[元素2]

weight = 7


[元素3]

weight = 3
```
上述配置文件表示抽取元素1的概率为5/15，抽取元素2的概率为7/15，抽取元素3的概率为3/15
可以根据需要增加或减少抽取元素，并相应地调整权重

下载在release里，解压压缩包就可以使用了
