# 学习笔记

[toc]

## 用`add first`或`add last`这套新的`API`改写`Deque`的代码

```java
// 改写前
Deque<String> deque = new LinkedList<String>();
deque.push("a");
deque.push("b");
deque.push("c");
System.out.println(deque);

String str = deque.peek();
System.out.println(str);
System.out.println(deque);

while (deque.size() > 0) {
    System.out.println(deque.pop());
}
System.out.println(deque);

// 改写后
Deque<String> deque = new LinkedList<>();
deque.addFirst("a");
deque.addFirst("b");
deque.addFirst("c");
System.out.println(deque);

String str = deque.peekFirst();
System.out.println(str);
System.out.println(deque);

while (deque.size() > 0) {
    System.out.println(deque.pollFirst());
}
System.out.println(deque);
```



## 分析 `Queue` 和 `Priority Queue` 的源码

### `Python3` 中的 `Queue`

- [源代码地址](https://github.com/python/cpython/blob/3.8/Lib/queue.py)

- 线程安全：使用锁，但不支持可重入锁

- 实现三种队列：先入先出（`Queue`）、先入后出（`LifoQueue`）、优先队列（`PriorityQueue`，使用 `heapq` 实现）

- `APIs`：
- `qsize()`：返回队列大小
  - `empty()`：是否为空，`True`表示为空
  - `full()`：是否满，`True`表示满
  - `put()`：入队，可设置超时时间及是否阻塞，若队列满了、且超过等待时间，则会抛异常
  - `get()`：出队，同入队的参数及含义
  - `task_done()`：任务完成，每个`get()`后跟随一个`task_done()`
  - `join()`：阻塞直到队列中所有任务都完成，与`task_done()`配合使用
  
- `Queue`内部利用`deque`实现（`self.queue = deque()`，底层是数组)，出入队列分别用`deque.popleft/append()`

- `Priority Queue`内部利用`heapq`与数组实现（`self.queue = []`），出入队列分别用`heapq.heappop/heappush()`

- `LifoQueue`内部利用数组实现（`self.queue = []`），出入对列分明用`list.pop/append()`

### `Python3` 中的 `heapq`

- [源代码地址](https://github.com/python/cpython/blob/3.8/Lib/heapq.py)
- `heap`由数组表示，其元素满足`a[k] <= a[2*k+1] and a[k] <= a[2*k+2]`，且`heap[0]`是最小的元素
- `APIs`：
  - `heappush()`：入队
  - `heappop()`：将最小的元素出队
  - `heapreplace()`：将最小的元素出队，并添加新的元素
  - `heappushpop()`：出队后入队
  - `heapify()`：将`list`转化为`heap`，时间复杂度`O(len(list))`
- 添加元素后的整理`_siftdown()`：TODO
- 删除元素后的整理`_siftup()`：TODO

## 脑图总结

![points](F:\algorithm011-class01\Week_01\refs\points.png)

![要点](F:\algorithm011-class01\Week_01\refs\data_structure.png)

![optimize_time_complexity](F:\algorithm011-class01\Week_01\refs\optimize_time_complexity.png)