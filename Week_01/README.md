# 学习笔记

## 用add first或add last这套新的API改写Deque的代码

不确定是否是要实现一下这两个函数...

```python3
class Deque(object):
    def __init__(self):
        self._deque = [] 

    def add_first(self, value):
        return self._deque.insert(0, value)

    def add_last(self, value):
		return self._deque.append(value)
```



## 分析 Queue 和 Priority Queue 的源码

Python3 中 Queue 基于 deque 实现，使用 list。

Python3 中用 heapq == Priority Queue，具体由 list 实现，元素满足`a[k] <= a[2*k+1] and a[k] <= a[2*k+2]`，heap[0]永远是最小的元素

其他的待补充...



## 一些总结

![points](F:\algorithm011-class01\Week_01\refs\points.png)

![要点](F:\algorithm011-class01\Week_01\refs\data_structure.png)

![optimize_time_complexity](F:\algorithm011-class01\Week_01\refs\optimize_time_complexity.png)