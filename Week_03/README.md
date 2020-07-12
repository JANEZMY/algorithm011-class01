[toc]

# 概述

- 找重复性
- 分解问题
- 组合结果

# 递归

**代码模板**

```python
class Solution:
    def recursion(level, param1, param2, ...):
        # 递归终结条件
        if level > MAX_LEVEL:
            process_result
            return

        # 处理当前层逻辑
        process(level, data, ...)

        # 下探到下一层
        self.recursion(level + 1, p1, p2, ...)

        # 清理当前层
```

```java
class Solution {
    public void recur(int level, int param) {
        // 递归终结条件
        if (level > MAX_LEVEL) {
            // process_result
            return;
        }

        // 处理当前层逻辑
        process(level, param);

        // 下探到下一层
        recur(level: level + 1, newParam);

        // 清理当前层
    }
}
```



**生成括号**

在`2n`个位置上放置左括号/右括号

```java
// V1：排列组合 2n 个左右括号
class Solution {
    public List<String> generateParenthesis(int n) {
        _generate(0, 2 * n, "");
        return null;
    }

    private void _generate(int level, int max, String s) {
        // terminator
        if (level >= max) {
            System.out.println(s);
            return;
        }

        // process current logic: add left or right
        String s1 = s + "(";
        String s2 = s + ")";

        // drill down
        _generate(level + 1, max, s1);
        _generate(level + 1, max, s2);

        // reverse states
    }
}
```

```java
// V2：验证括号的合法性
// 1、左边括号：不超过 n 个，则任意加
// 2、右括号：已有左括号个数 > 已有右括号个数
class Solution {
    private List<String> result;

    public List<String> generateParenthesis(int n) {
        result = new ArrayList<String>();
        _generate(0, 0, n, "");
        return result;
    }

    // left：当前左括号的个数
    // right：当前右括号的个数
    private void _generate(int left, int right, int n, String s) {
        // terminator
        if (left == n && right == n) {
            result.add(s);
            return;
        }

        // process current logic: add left or right

        // drill down
        if (left < n)
            _generate(left + 1, right, n, s + "(");
        if (left > right)
            _generate(left, right + 1, n, s + ")");

        // reverse states
    }
}
```

# 分治

**代码模板**

```python
def divide_conquer(problem, param1, param2, ...):
    # terminator
    if problem is None:
        print_result
        return
    
    # prepare data
    data = prepare_data(problem)
    subproblems = split_problem(problem, data)
    
    # conquer subproblems
    subresult1 = self.divide_conquer(subproblems[0], p1, ...)
    subresult2 = self.divide_conquer(subproblems[1], p1, ...)
    subresult3 = self.divide_conquer(subproblems[2], p1, ...)
    ...
    
    # process and generate the final result
    result = process_result(subresult1, subresult2, subresult3, ...)
    
    # revert the current level states
```

