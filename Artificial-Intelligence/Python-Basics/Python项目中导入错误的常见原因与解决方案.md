# 1.模块名错误
## 示例
### 项目结构
```bash
project/
├── main.py
└── utils.py
```
### utils.py
```python
def add(a,b):
    return a+b
```
### main.py
```python
from util import add
print(add(1,2))
```
### 报错
```python
ModuleNotFoundError: No module named "util"
```

module 模块

模块没有找到错误：没有名字为“util”的模块
### 原因
将utils写成util
### 正确写法
```python
from utils import add
print(add(1,2))
```
# 2.导入的对象名不存在
## 示例
### utils.py
```python
def add(a,b):
    return a+b
```
### main.py
```python
from utils import sub
print(sub(3,1))
```
### 报错
 ```python
 ImportError: cannot import name 'sub' from utils
 ```
 import 导入
 
 导入错误：不能从utils模块中导入名字为sub的函数
 
 ### 原因

utils.py文件里只有add函数，没有sub函数
### 正确写法
#### 1.只写utils.py中的函数
```python
from utils import add
print(add(3,1))
```
#### 2.在utils.py中添加sub函数
```python
def sub(a,b)
    return a-b
```

 # 3.运行位置错误
 ## 示例
 ### 项目结构
 ```bash
 project/
├── main.py
└── tools/
    ├── __init__.py
    └── math_utils.py
 ```
 ### math_utils.py
```python
def add(a,b):
    return a+b
```
### main.py
 ```python
 from tools.math_utils import add
 print(add(1,2))
 ```
  ### 报错
  ```python
  ModuleNotFoundError: No Module named 'tools'
  ```

### 原因
不在project目录中运行，而是在project的子目录中运行某个模块，并且这个模块导入了project目录中某个包的模块文件的方法，在该子目录中找不到包文件所以报错

Python 会根据程序的启动方式，把某些目录作为模块查找起点；如果你导入的包不在这些查找路径里，就会报错。

#### 程序的启动方式
##### 执行一个文件
这是直接将main.py当成Python文件直接执行
```python
python main.py
```
##### 执行一个模块
要求Python能够在当前目录看到包文件，即在当前目录当中找到app包文件夹
```python
python -m app.main
```
m→module模块
### 正确做法
应该在根目录（project目录之中）运行，运行main.py文件
不要随便在子文件夹里面运行模块文件
 # 4.文件名和Python内置模块重名
 ## 示例
 ### 项目结构
 ```bash
 project/
├── random.py
└── main.py
 ```
 ### random.py
 ```python
 def my_func():
     print("这是我自己的random.py文件")
 ```
 ### main.py
 ```python
 import random
 print(random.randint(1,10))
 ```
 ### 报错
 ```python
AttributeError: module 'random' has no attribute 'randint'
 ```
 属性错误：模块random中并没有属性randint
 ### 原因
 文件名和标准库名重名了

自己以为使用的是系统内置的random模块，实际上Python会优先寻找当前目录里的random.py文件即random模块并导入，但是自己的random模块中并没有randint，于是报错
### 正确做法
将自己的random.py文件改名为my_random_tools.py即可
# 5.包结构不清晰
## 示例
### 项目结构
```bash
project/
├── main.py
└── utils/
    └── math_utils.py
```
### math_utils.py
```python
def add(a,b):
    return a+b
```
### main.py
```Python
from utils.math_utils import add
print(add(1,2))
```
### 报错
```python
ModuleNotFoundError: No module named 'utils'
```
### 原因
utils只是普通文件夹，没有添加`__init__.py`文件来明确包结构

虽然新版本的Python对于包的处理比较宽松，但是初学者最好规范，避免某些环境报错
### 正确写法
```python
utils/
├── __init__.py
└── math_utils.py
```
# 6.相对导入错误
## 示例
### 项目结构
```bash
project/
└── app/
    ├── __init__.py
    ├── main.py
    └── utils.py
```
### utils.py
```python
def hello():
    print("hello")
```
### main.py
```python
from .utils import hello
hello()
```
### 报错
直接运行main.py文件
```python
ImportError: attempted relative     import with no known parent package
```
attempted  尝试 
relative 相对的
parent 父目录，父级

导入错误：尝试导入不知道的父目录包
### 原因
这个属于相对导入，相对导入要求当前文件必须是包中的文件才可以运行

直接运行main.py文件，在main.py所处的目录当中并没有找到包文件，所以python并不知道他属于哪个包
#### 正常情况
```python
project/
├── main.py
└── app/
    ├── __init__.py
    └── utils.py
```
### 正确做法
#### 1.修改为绝对导入
##### main.py
```python
from app.utils import hello
hello()
```
并且在根目录运行，或者当前目录当中存在app包文件
```Python
python -m app.main
```
#### 初级阶段尽量减少相对导入的使用
优先绝对导入，从根目录运行
# 7.绝对导入错误
## 示例
### 项目结构
```python
project/
└── app/
    ├── __init__.py
    ├── main.py
    └── utils.py
```
### utils.py
```python
def hello()
    print("hello")
```
### main.py
```python
from app.utils import hello
hello()
```
在app文件夹里面运行
```bash
cd app
python main.py
```
### 报错
```python
ModuleNotFoundError: No module named 'app'
```
### 原因
Python看到的当前路径是app，但是在app目录里面，所以无法找到app目录，因此报错
### 正确方式
```python
python -m app.main
```
或者确保以项目根目录为起点运行
# 8.循环导入错误
## 示例
### 项目结构
```bash
project/
├── a.py
├── b.py
└── main.py
```
### a.py
```python
from b import func_b
def func_a():
    print("A")
    func_b()
```
### b.py
```python
from a import func_a
def func_b():
    print("B")
    func_a()
```
### main.py
```python
from a import func_a
func_a()
```
### 报错
```python
ImportError: cannot import name 'func_a' from partially initiallized module 'a'
```
### 原因
a.py导入b.py，然后b.py有立即导入a.py，陷入无限循环导入
### 正确方式
#### 重新设计结构
将共同依赖的代码移动到common.py文件中
```bash
project/
├── a.py
├── b.py
├── common.py
└── main.py
```
# 9.把模块当文件夹，把文件夹当模块
## 示例
### 项目结构
```bash
project/
├── main.py
└── utils/
    ├── __init__.py
    └── math_utils.py
```
### math_utils.py
```python
def add(a,b):
    return a+b
```
### main.py
```python
from math_utils import add
print(add(1,2))
```
### 报错
```python
ModuleNotFoundError: No module named 'math_utils'
```
### 原因
math_utils在utils文件夹中，而不在当前根目录下，所以不能直接导入模块math_utils，需要先导入包文件，再导入包文件中的模块文件
### 正确写法
```python
from utils.math_utils import add
```
# 10.第三方库没有安装
## 示例
### main.py
```python
import pandas as pd
```
### 报错
```python
ModuleNotFoundError: No module named 'pandas'
```
### 原因
没有安装pandas，或者装到了别的Python环境里
### 正确做法
```bash
pip install pandas
```
如果有多个环境，建议更加稳妥的
```bash
python -m pip install pandas
```
#### 二者区别
二者都是将pandas安装到Python环境当中，

但是前者适用于只有一个Python环境，若存在多个Python环境，则安装时会随机挑选环境进行安装；

后者则是指定当前Python环境进行安装
### 注意
有时候确实装了第三方库，但是还是报错，可能是解释器不一致
# 11.虚拟环境和解释器不一致
## 示例
### 场景
在命令行里面装了torch
```bash
pip install torch
```
### 报错
```python
ModuleNotFoundError: No module named 'torch'
```
### 原因
解释器与虚拟环境不一致
#### 解释器是什么？虚拟环境是什么？如何辨别是否一致？
问题解释比较复杂，放到下一篇文章

### 解决方法
查看运行时解释器路径
```python
import sys
print(sys.executable)
```
再确认安装时是否装到这个解释器里面
```bash
python -m pip install torch
```
# 13.`__init__.py`理解错误
## 示例
### 项目结构
```python
project/
├──main.py
└── mypkg/
    ├── __init__.py
    ├── a.py
    └── b.py
```
### a.py
```python
def hello():
    print("hello")
```
### `__init__.py`
空文件
### main.py
```python
from mypkg import hello
```
### 报错
```python
ImportError: cannot import name 'hello' from 'mypkg'
```
### 原因
mypkg包目录中并没有hello方法，方法在mkpkg目录的a.py文件当中，因此直接导入mypkgPython并不知道hello在哪里
### 正确写法
#### 写法1
```python
from mypkg.a import hello
```
#### 写法2
先导入到`__init__.py`文件
```python
# 从当前目录（mypkg）的a.py文件中导入hello
from .a import hello
```
再采用简写导入
```python
from mypkg import hello
```
# 13.文件执行方式不同导致导入结果不同
## 示例
### 项目结构
```bash
project/
└── app/
    ├── __init__.py
    ├── main.py
    └── utils.py
```
### utils.py
```python
def hello():
    print("hello")
```
### main.py
```python
from app.utils import hello
```
### 运行方式
#### 方式1
```bash
python app/main.py
```
#### 方式2
包项目推荐
```bash
python -m app.main
```

