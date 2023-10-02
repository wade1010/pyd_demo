使用python setup.py build_ext --inplace即可生成如图的pyd文件了，在python中使用，import test即可使用了。



--inplace: 这是一个选项，用于指定将构建的扩展模块直接放置在当前目录中，而不是放置在默认的构建目录中。使用此选项后，生成的扩展模块文件将与源代码文件位于同一目录中。




这个 cp310 和 win_amd64 视 python 版本和操作系统而定。我们可以把它改成 test.pyd，注意，是只能改成 test.pyd；改成其他任何名字都不行，使用时会 import error。使用该 pyd 方式如下

import demo
from demo import {{类名|函数名}}


