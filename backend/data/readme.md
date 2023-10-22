* 可以通过访问

  ```python
  http://101.200.241.8:3389/authors
  http://101.200.241.8:3389/links
  ```

  分别获取json格式的学者和关联信息。

  author数据格式如下,其中$node\_size$表示学者的影响力大小，可以用作显示的像素大小：

  ```
  {
  [field: "Data mining", id: 0, name: "Sreangsu Acharyya",node_size: 22],
  [field: "Data mining", id: 1, name: "Francois Rioult",node_size: 23],
  ...
  }
  ```

  Link信息格式如下：

  ```
  {
  [field: "Data mining", id: 0, name: “0”，sid: 16, tid: 4],
  [field: "Data mining", id: 1, name: “1”，sid: 1, tid: 16],
  ...
  }
  ```

* 注:以上格式是后端目前提供的小规模数据的数据格式，最新处理好的数据一方面规模较大，另外在link中多加入了一个“count”属性，表示两个学者之间的合著的论文篇数。