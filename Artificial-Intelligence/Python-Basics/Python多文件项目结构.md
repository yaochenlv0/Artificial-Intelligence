# 作用
1. 将原本的大文件进行切分，方便寻找代码
2. 功能分开，逻辑清晰
3. 修改一个地方，不会影响其他地方
4. 代码容易复用
5. 方便添加新功能
# 常见拆分
1. 入口文件
2. 功能模块
3. 工具模块
4. 配置文件
5. 数据文件
6. 包目录
# 最基础的多文件项目结构
```bash
my_project/
│
├── main.py
├── config.py
├── utils.py
├── model.py
└── data/
    └── train.csv
```
## 各文件作用
### main.py
项目入口，程序从这里开始运行
### config.py
存放配置，比如路径，参数，常量
### utils.py
存放通用工具函数
### model.py
 存放核心业务逻辑，比如模型训练，预测等
### data/
存放数据文件
# 文件之间互相调用的方式

方式：导入

## 导入整个模块
```Python
# 导入整个utils文件
import utils
# 调用函数
print(utils.add(2,3))
```

调用函数

```python
utils.add(2,3)
```
## 导入模块中的函数

只将add函数导入进来

```python
from utils import add
print(add(2,3))
```
## 导入多个内容
```Python
import utils as add,sub
```
## 起别名

```python
import utils as ut
print(ut.add(1,2))
```

或者

```python
from utils import add as a
print(a(1,2))
```
# 文件夹的调用方式

文件夹也可以变成模块来被调用

大一点的项目也不再仅仅是文件，而是包含文件夹
```bash
my_project/
│
├── main.py
├── config.py
├── utils/
│   ├── __init__.py
│   ├── file_utils.py
│   └── math_utils.py
└── models/
    ├── __init__.py
    └── mlp.py
```
utils，models已经不是普通文件夹，而是包（package）

只要文件夹里有这个`__init__.py`，Python就可以将它看做包

对于 `__init__.py`的解释在文章最后

# 包里文件的导入方式

from 包.文件 import 文件中的函数 as 别名

## 示例

utils/math_utils
```python
def add(a,b):
    return a+b
```

main.py
```python
from utils.math_utils import add
print(add(10,20))
```
# 真实项目的结构
```bash
project/
│
├── main.py                 # 入口
├── config.py               # 配置
├── requirements.txt        # 依赖
├── README.md               # 项目说明
│
├── data/                   # 数据
├── logs/                   # 日志
├── tests/                  # 测试
│
├── utils/                  # 工具函数
│   ├── __init__.py
│   └── helpers.py
│
├── services/               # 业务逻辑
│   ├── __init__.py
│   └── user_service.py
│
└── models/                 # 数据模型/机器学习模型
    ├── __init__.py
    └── classifier.py
```
# 完整示例
## 项目结构
```bash
student_project/
│
├── main.py
├── config.py
├── utils.py
└── student.py
```
## config.py
负责配置
```python
SCHOOL_NAME＝“xx大学”
```
## utils.py
负责工具函数
```python
def print_line():
    print("-" * 30)
```
## student.py
负责类
```python
class Student:
    def __init__(self,name,age):
        self.name ＝ name
        self.age ＝ age
    def introduce(self):
        print(f"大家好，我的名字是{self.name}，年龄为{self.age}")
```

## main.py
负责调度
```python
from config import SCHOOL_NAME
from utils import print_line
from student import Student

print_line()
print(f"学校：{SCHOOL_NAME}")

stu ＝ Student("张三",20)
stu.introduce()
print_line()
```

# 混淆概念
## 模块和文件的关系
通常一个.py文件就是一个模块
## 包和文件夹的关系
带有`__init__.py`的文件，通常就是包
## 工具模块与功能模块的区分

工具模块和功能模块里面放的都是函数，但是工具函数只是作为辅助使功能模块的函数得以实现

工具模块，提供通用功能；功能模块，聚焦具体业务的实现
# `__init__.py`的理解
## 直观理解
```bash
project/
├── main.py
└── utils/
    ├── __init__.py
    ├── math_tools.py
    └── file_tools.py
```
因为utils里面有`__init__.py`文件，所以不是一个普通文件，而是一个包

所以，可以如下方式导入
```python
from utils.math_tools import add
```
## 名字理解
init全称initialize（初始化）

初始化：当一个包被导入时，优先执行包中的`__init__.py`文件

因此`__init__.py`文件也叫初始化文件
## 最基础的功能

让文件夹成为包
## `__init__.py`文件是否必须要有

没有`__init__.py`文件，常常也可以运行，但是要将文件夹作为包来使用，最好加上它
### 作用
1. 老版本python比较依赖
2. 环境和工具更规范、更稳定
3. 代码结构更清晰
4. 便于初学者理解包的概念
## 文件内容
### 可以为空
什么不写也有意义，表示所在的文件夹是一个包
### 可以写代码
在导入包之后，会有优先执行`__init__.py`文件中的代码
#### 示例
utils/`__init__.py`
```python
print("utils包已经被导入")
```
main.py
```python
import utils
```
运行结果
```python
utils包已经被导入
```
## 其他功能：统一导出内容
在`__init__.py`文件中加入导入代码，可以简化导入代码，直接如下：

from 包文件夹 import 包文件夹中各个文件中的函数
## 示例
### 项目结构
```python
project/
└── utils/
    ├── __init__.py
    ├── math_tools.py
    └── file_tools.py
```
### main_tools.py
```python
def add(a, b):
    return a + b
```
### file_tools.py
```python
def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
```
### `__init__.py`不写内容

导入方式
```python
from utils.math_tools import add
from utils.file_tools import read_file
```
### `__init__.py`写内容

内容如下：
```python
from .math_tools import add
from .file_tools import read_file
```

“.math_tools”中的“.”代表在当前目录下的math_tools

导入方式
```python
from utils import add, read_file
```