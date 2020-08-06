[TOC]

# Trie 树

应用：前缀感应词

别名：字典树、单词查找树、键树

特点：统计、排序字符串，查找效率比哈希表高

性质：

- 结点本身不存完整单词
- 从根结点到某一结点，路径上经过的字符连接起来，为该结点对应的字符串
- 每个结点的所有子结点路径代表的字符都不相同

思想：空间换时间

代码模板：

```python
class Trie(object):
  
	def __init__(self): 
		self.root = {} 
		self.end_of_word = "#" 
 
	def insert(self, word): 
		node = self.root 
		for char in word: 
			node = node.setdefault(char, {}) 
		node[self.end_of_word] = self.end_of_word 
 
	def search(self, word): 
		node = self.root 
		for char in word: 
			if char not in node: 
				return False 
			node = node[char] 
		return self.end_of_word in node 
 
	def startsWith(self, prefix): 
		node = self.root 
		for char in prefix: 
			if char not in node: 
				return False 
			node = node[char] 
		return True
```



# 并查集

应用：组团、配对，与 group 有关

```python
def init(p): 
	p = [i for i in range(n)] 
 
def union(self, p, i, j): 
	p1 = self.parent(p, i) 
	p2 = self.parent(p, j) 
	p[p1] = p2 # 将一个集合老大的父节点设置为另一个集合老大
 
def parent(self, p, i): # 查找到集合老大
	root = i 
	while p[root] != root: 
		root = p[root] 
	while p[i] != i: # 路径压缩，不影响函数结果，但可优化查找集合老大的时间，缩短到O(1)
		x = i; i = p[i]; p[x] = root 
	return root
```

