# FZ-2021-class-10-random
附中2021级高二十班随机点名器

本人自制点名程序，能随机点到十班53个人中的任何一个
.exe程序无需安装Python环境，在Windows电脑上点击即可运行
其他为源码
此项目允许二创，把源码下载下来，将里面的学生名更换为你的班级的即可
如果要将.py程序打包成.exe程序，你需要安装pyinstaller

安装pyinstaller:
1.在cmd窗口运行如下命令(前提是你已安装Python运行环境)
  pip install pyinstaller
2.执行
  pyinstaller XXX.py
（默认在生成的dist文件夹里会生成好几个文件，如果想要只生成一个.exe文件在pyinstaller和XXX.py之间加上--onefile即可）
