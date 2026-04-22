# 示例

```python
file_path = '' 
with open(file_path,'r',encoding='utf-8') as file:  
    text = file.read()  
```
### with 
上下文管理器，自动管理资源  
### open()
打开文件的函数  
### file_path
文件路径  
### r
只读模式  
### encoding='utf-8'
编码方式为中文  
### as file
给打开的文件对象起个别名为file  
# 文件打开模式  

| 模式  | 含义       |
| --- | -------- |
| r   | 只读（默认）   |
| w   | 写入（会覆盖）  |
| a   | 追加（末尾添加） |
| x   | 独自创建     |
| b   | 二进制模式    |
| +   | 读写模式     |
### 独自创建

### 二进制模式

### 读写模式

# with解释
## 传统方式
```python
file = open('data.txt','r')
text = file.read()
# 如果前面出错，则关闭文件就无法执行
file.close()
```
## with方式（自动管理）
```python
# 自动关闭文件，即使出错也会关闭
with open('data.txt', 'r') as file:
	text = file.read()
```
# 文件读取方法
```python
with open("file.txt', 'r',encoding='utf-8') as f:
	# 方法1 全部读取
	content = f.read()
	
	# 方法2：按行读取（推荐大文件）
	for line in f:
		print(line)
		
	# 方法3：读取所有行到列表
	lines = f.readlines()
	
	# 方法4：只读第一行
	first_line = f.readline()
```
# 文件写入方法
```python
with open('output.txt','w',encoding='utf-8') as f:
	# 方法1：写入字符串
	f.write("Hello world")
	
	# 方法2：换行
	f.write('\n')
	
	# 方法3：写入多行
	f.write(['行1','行2'])
	
# 方法4：追加内容
with opem('output.txt', 'a', encoding='utf-8') as f:
	f.write('这是追加的内容)
```
# 处理大文件（不会内存爆炸）
```python
# 处理小文件可以，但是大文件会直接内存爆炸
with open('big_file.txt','r') as f:
	# 1GB文件会直接俄读入内存
	all_content = f.read()
# 处理大文件方法1：逐行处理
with open('big_file.txt','r',encoding='utf-8') as f:
	# 一次只读一行
	for line in f:
		# 处理这一行 
		process_line(line)
# 处理大文件方法2：分块读取
with open('big_file.txt','r',encoding='utf-8') as f:
	while True:
		# 一次读1024个字节
		chunk = f.read(1024)
		if not chunk:
			break
		# 处理这一块
		process_chunk(chunk)
```
# 编码问题详解
## 常见编码

| encoding   | 语言          |
| ---------- | ----------- |
| utf-8（最常用） | 支持所有语言      |
| gbk        | Windows中文默认 |
| gb2312     | 简体中文老文件     |
| ascii      | 纯英文         |
## 处理编码错误
```python
try:
	with open('file.txt','r',encoding='utf-8') as f:
		text = f.read()
# 编码错误
except UnicodeDecodeError:
	with open('file.txt','r',encoding='gbk') as f:
		text = f.read()	
# 都无法解析，则忽略
with open('file.txt','r',encoding='utf-8',errors='igore') as f:
	text = f.read()
```
# 同时打开多个文件
```python
# 同时打开两个文件
with open('file1.txt','r') as f1,open('file2.txt','r') as f2:
	content1 = f1.read()
	content2 = f2.read()

# 复制文件
with open('source.txt','r') as src,open('dest.txt','w') as dst:
	dst.write(src.read())
```