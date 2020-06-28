# 学习笔记

## 用add first或add last这套新的API改写Deque的代码

```java
// 改写前
Deque<String> deque = new LinkedList<String>();
deque.push("a");
deque.push("b");
deque.push("e");
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
deque.addFirst("e");
System.out.println(deque);

String str = deque.peekFirst();
System.out.println(str);
System.out.println(deque);

while (deque.size() > 0) {
    System.out.println(deque.pollFirst());
}
System.out.println(deque);
```



## 分析 Queue 和 Priority Queue 的源码

Python3 中 Queue 基于 deque 实现，使用 list。

Python3 中用 heapq == Priority Queue，具体由 list 实现，元素满足`a[k] <= a[2*k+1] and a[k] <= a[2*k+2]`，heap[0]永远是最小的元素

其他的待补充...



## 一些总结

![points](F:\algorithm011-class01\Week_01\refs\points.png)

![要点](F:\algorithm011-class01\Week_01\refs\data_structure.png)

![optimize_time_complexity](F:\algorithm011-class01\Week_01\refs\optimize_time_complexity.png)