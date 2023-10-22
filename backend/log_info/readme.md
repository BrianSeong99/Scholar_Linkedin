* 文件说明：
  * `part_info.json`是从`aminer_user_behavior_log_info.json`中截取的，大约两万行
  * `log.data`是抽取出`part_info.json`中访问类型是`lab.nd.search`的记录，处理过程见`process_loginfo.py`
  * `Tracking Log Documents`解释了`part_info.json`的一些键值含义（虽然说得不够清楚）
* 执行测试：
  * 为随机用户推荐：`python recommend.py`
  * 为指定用户推荐，例：`python recommend.py 5c03da6f3a69b1c9e1ec12c2`
  * 所有用户`id`见`log.data`