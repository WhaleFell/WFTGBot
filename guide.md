# Run Guide

```shell
# docker 安装
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# 克隆项目
git clone https://github.com/WhaleFell/WFTGBot.git
docker build -t tgbot .

# 登录并获取 token
# 按照提示一步一步登录
docker run -it --rm --name tgbot -v /root/tgconfigs/tg.yaml:/wkdir/config.yaml tgbot python main.py token

# 新建配置文件夹
mkdir /root/tgconfigs
# 新建这个文件
touch /root/tgconfigs/tg.yaml
# 写入文件内容 在下面
# 将上一步获取的 token 字符串写入到 tg.yaml 的 session_str 字段
nano /root/tgconfigs/tg.yaml

# 运行
docker run -d -p 8099:5555 --name tgbot -v /root/tgconfigs/tg.yaml:/wkdir/config.yaml tgbot python main.py start

# 重启
docker restart tgbot
```

## tg.yaml

```yaml
name: TGBot # 机器人名字
isUser: true # 是否是用户机器人
bot_token: '' # 机器人 token 如果是用户机器人就不用填写
api_id: 21341224
api_hash: '2d910cf3998019516d6d4bbb53713f20'
# 会话字符串（如果是机器人账户的话不用填写）
session_str: ""

log: DEBUG  # 日志等级

# 机器人 /start 时候的描述
bot_desc: |
  机器人描述发送 /start 的时候

Web:
  host: 0.0.0.0
  port: 5555
  username: admin
  password: admin
  # 随机字符串,可以不用管
  SECRET_KEY: w1wdihehoihiodi1pdh

# 插件设置

# 关键词监控插件
KeyMonitor:
  enable: false  # 关闭
  keywords: # 监控的关键词
  - 做爱
  forword_id: # 转发信息到id
  - me

# 文件改名插件
RenameFile:
  enable: true # 启用
  file_path: data/file.zip  # 文件路径

  # 发送文件时的描述 文件的更新时间用 {update_time} 代替
  # yaml 中使用 | 来识别带换行的字符串
  file_desc: | 
    当前毒包更新时间为: {update_time} 
    请核对好毒包再推毒！

# 输入命令提示插件 未完善
CommandTips:

# 输入自定义命令输出描述
CustomCommands:
  # 注意命令不要带 /
  - command: jdgs
    text: | 
      渠道：
      行业：
      微信号：
      微信名字：
      电话：
      地区：
      交单人：
      单数：
      文件：
    desc: 查看交单格式
  
  - command: jjff
    text: | 
      弹窗解决方法频道：
      https://t.me/+wY8Wx6M_a5BlMGU1
    desc: 查看弹窗解决方法
  
  - command: xsjc
    text: | 
      新手教程频道：
      https://t.me/+5NRMXo6d_EM0Y2Rl
    desc: 查看新手教程
```
