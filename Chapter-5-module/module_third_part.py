# coding=utf-8
"""
在Python中，安装第三方模块，是通过包管理工具pip完成的。
pip install Pillow
"""

"""
一般来说，第三方库都会在Python官方的pypi.python.org网站注册，要安装一个第三方库，必须先知道该库的名称，可以在官网或者pypi上搜索，比如Pillow的名称叫Pillow，因此，安装Pillow的命令就是
"""

"""
安装常用模块
在使用Python时，我们经常需要用到很多第三方库，例如，上面提到的Pillow，以及MySQL驱动程序，Web框架Flask，科学计算Numpy等。用pip一个一个安装费时费力，还需要考虑兼容性。我们推荐直接使用Anaconda，这是一个基于Python的数据处理和科学计算平台，它已经内置了许多非常有用的第三方库，我们装上Anaconda，就相当于把数十个第三方模块自动安装好了，非常简单易用。

可以从Anaconda官网下载GUI安装包，安装包有500~600M，所以需要耐心等待下载。网速慢的同学请移步国内镜像。下载后直接安装，Anaconda会把系统Path中的python指向自己自带的Python，并且，Anaconda安装的第三方模块会安装在Anaconda自己的路径下，不影响系统已安装的Python目录。

安装好Anaconda后，重新打开命令行窗口，输入python，可以看到Anaconda的信息：
"""

"""
如果你用 brew 安装的 python，卸载了吧。

推荐用 Anaconda3 管理 python，安装 brew cask install anaconda 安装之后设置 anaconda 环境变量 「在你的 .zshrc 或者 bash」

export PATH=/usr/local/anaconda3/bin:"$PATH"
然后你就可以使用 conda 命令了。Anaconda3 也会给你默认安装一个 python 3.6 的稳定版本，并且之后命令行运行的 python 也会是 3.6

如果你要设置 python3.7 用 connda 命令创建一个 3.7 版本的环境

conda create -n py37 python=3.7
source activate py37
python -V
"""
