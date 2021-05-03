# HomeAssistant搭建笔记

## 前言

最近购买了

## 首先是一些准备工作

本文以树莓派为例进行搭建，那么你需要准备的东西如下：

- 树莓派（建议使用3b+以上幸好）
- SSH工具：用于连接树莓派
- 稳定的网络：用于下载Github内容

那么首先请确保你的树莓派与你要部署的智能家居在同一网络下并且树莓派拥有固定IP，OpenWRT下在DHCP- Statistic Lease里面进行设置，如下图：

![image-20210412201833559](HomeAssistant%E6%90%AD%E5%BB%BA%E7%AC%94%E8%AE%B0.assets/image-20210412201833559.png)

安装Docker就不再赘述了，亲自行翻阅Google

## HaaS容器安装

鉴于HomeAssistant提供了非常亦可赛艇的Docker镜像，我们就直接使用了，食用命令如下：

```sh
docker run --init -d \
  --name homeassistant \
  --restart=unless-stopped \
  -v /etc/localtime:/etc/localtime:ro \
  -v /PATH_TO_YOUR_CONFIG:/config \
  --network=host \
  homeassistant/home-assistant:stable
```

其中**/PATH_TO_YOUR_CONFIG**为自定义的homeassistant配置储存空间，在输入了命令之后，你的homeassistant应该就会准备就绪了。

**Pro Tips:** docker部分命令需要sudo才能运行，可以讲当前用户添加到docker组就不用一直sudo了

```sh
sudo usermod -aG docker pi
```

## HA初见面

在docker启动之后，输入树莓派IP地址**192.168.1.5:8123**就可以进入到homeassistant的后台了，初次进入我们需要进行一些初始化配置。

首先是账号密码：

![image-20210412211343890](HomeAssistant%E6%90%AD%E5%BB%BA%E7%AC%94%E8%AE%B0.assets/image-20210412211343890.png)

家庭的基本信息：

![image-20210412211427493](HomeAssistant%E6%90%AD%E5%BB%BA%E7%AC%94%E8%AE%B0.assets/image-20210412211427493.png)

诊断数据：

![image-20210412211446323](HomeAssistant%E6%90%AD%E5%BB%BA%E7%AC%94%E8%AE%B0.assets/image-20210412211446323.png)

最后完成

![image-20210412211455439](HomeAssistant%E6%90%AD%E5%BB%BA%E7%AC%94%E8%AE%B0.assets/image-20210412211455439.png)

## 仪表盘

下图所示就是仪表盘啦，如你所见，目前仪表盘还是非常的干净，接下来我们就要开始添加上各种各样奇奇怪怪的东西了。

![image-20210412211901085](HomeAssistant%E6%90%AD%E5%BB%BA%E7%AC%94%E8%AE%B0.assets/image-20210412211901085.png)

## HomeKit联动

首先，我整HA最主要的目的便是与HomeKit联动，HA本身提供了很方便的HomeKit集成。我们在集成中选择HomeKit就可以很方便的进行Homekit联动。

![image-20210413144418589](HomeAssistant%E6%90%AD%E5%BB%BA%E7%AC%94%E8%AE%B0.assets/image-20210413144418589.png)

在这里，我们点击提交便能完成Homekit的配置。

![image-20210413144449114](HomeAssistant%E6%90%AD%E5%BB%BA%E7%AC%94%E8%AE%B0.assets/image-20210413144449114.png)

回到手机，打开家庭App。在家庭App右上角加号中，扫描通知中的二维码，此时会弹出一个窗口说Homekit配件不受信任，我们继续添加即可。

![image-20210413144855878](HomeAssistant%E6%90%AD%E5%BB%BA%E7%AC%94%E8%AE%B0.assets/image-20210413144855878.png)

![image-20210413145433093](HomeAssistant%E6%90%AD%E5%BB%BA%E7%AC%94%E8%AE%B0.assets/image-20210413145433093.png)

![image-20210413145417175](HomeAssistant%E6%90%AD%E5%BB%BA%E7%AC%94%E8%AE%B0.assets/image-20210413145417175.png)

至此，我们的Homekit至此已经安装完毕了。

### Homekit自定义配置

![image-20210413160513268](HomeAssistant%E6%90%AD%E5%BB%BA%E7%AC%94%E8%AE%B0.assets/image-20210413160513268.png)

## HACS安装

为了整活，一个丰富的软件源是必不可少的。虽然本身HaaS已经提供了非常丰富的软件源，但是仍然不能满足本人折腾的心。隆重介绍HACS（Home Assistant Community Store）：一个由社区维护的HA软件源。安装方法也非常简单：

1.进入HA的docker容器内，在终端输入以下命令进入容器内终端：

```sh
docker exec -it homeassistant sh
```

回车后，你的终端应该是这样的

```sh
/config #
```

2.在容器终端内输入安装脚本

```sh
export https_proxy=http://192.168.1.121:7890	# 设置代理，如果网不好可以设置一下
curl https://install.hacs.xyz/ | bash -
```

返回值如下

```sh
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--       0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     100  2482  100  2482    0     0   1888      0  0:00:01  0:00:01 --:--:--  1890
INFO: Trying to find the correct directory...
INFO: Found Home Assistant configuration directory at '/config'
INFO: Changing to the custom_components directory...
INFO: Downloading HACS
Connecting to github.com (13.114.40.48:443)
Connecting to github.com (13.114.40.48:443)
Connecting to github-releases.githubusercontent.com (185.199.109.154:443)
saving to 'hacs.zip'
hacs.zip             100% |*****************************| 77300  0:00:00 ETA
'hacs.zip' saved
INFO: Creating HACS directory...
INFO: Unpacking HACS...
INFO: Removing HACS zip file...
INFO: Installation complete.	# 安装完成

INFO: Remember to restart Home Assistant before you configure it
/config #
```

随后我们重启一下HA的docker

![image-20210412214926999](HomeAssistant%E6%90%AD%E5%BB%BA%E7%AC%94%E8%AE%B0.assets/image-20210412214926999.png)

重启完成之后，在「配置-集成」处，右下角选择「添加集成」，添加HACS集成

![image-20210412215041071](HomeAssistant%E6%90%AD%E5%BB%BA%E7%AC%94%E8%AE%B0.assets/image-20210412215041071.png)

随后会出现一些TOC，此处需要全部同意

![image-20210412215406965](HomeAssistant%E6%90%AD%E5%BB%BA%E7%AC%94%E8%AE%B0.assets/image-20210412215406965.png)

根据页面提示，我们需要去Github授权设备

![image-20210412215419109](HomeAssistant%E6%90%AD%E5%BB%BA%E7%AC%94%E8%AE%B0.assets/image-20210412215419109.png)

授权成功截图如下：

![image-20210412215514817](HomeAssistant%E6%90%AD%E5%BB%BA%E7%AC%94%E8%AE%B0.assets/image-20210412215514817.png)

![image-20210412220233386](HomeAssistant%E6%90%AD%E5%BB%BA%E7%AC%94%E8%AE%B0.assets/image-20210412220233386.png)

随后，在左侧菜单就可以看见HACS的图标了。

![image-20210412220458387](HomeAssistant%E6%90%AD%E5%BB%BA%E7%AC%94%E8%AE%B0.assets/image-20210412220458387.png)

## 接入小米生态链

在左侧HACS中，我们选择Integrations，搜索「miot」并且点击进入。

![image-20210413145729202](HomeAssistant%E6%90%AD%E5%BB%BA%E7%AC%94%E8%AE%B0.assets/image-20210413145729202.png)

选择右下角的「Install This Repository in HACS」

![image-20210413145828885](HomeAssistant%E6%90%AD%E5%BB%BA%E7%AC%94%E8%AE%B0.assets/image-20210413145828885.png)

在安装好后，我们要从重新启动一下HA的服务。

![image-20210413150340686](HomeAssistant%E6%90%AD%E5%BB%BA%E7%AC%94%E8%AE%B0.assets/image-20210413150340686.png)

重启完成后，回到「配置-集成-添加集成」，在此时选择MIoT即可。登录方式我们选择直接接入账号，简单快捷。

![image-20210413150429252](HomeAssistant%E6%90%AD%E5%BB%BA%E7%AC%94%E8%AE%B0.assets/image-20210413150429252.png)

登录成功后，选择「选项」，勾选「批量添加设备」。

![image-20210413150538878](HomeAssistant%E6%90%AD%E5%BB%BA%E7%AC%94%E8%AE%B0.assets/image-20210413150538878.png)

![image-20210413150546269](HomeAssistant%E6%90%AD%E5%BB%BA%E7%AC%94%E8%AE%B0.assets/image-20210413150546269.png)

![image-20210413150558611](HomeAssistant%E6%90%AD%E5%BB%BA%E7%AC%94%E8%AE%B0.assets/image-20210413150558611.png)

添加成功后，回到开始界面，便可以看到我们新添加的传感器了。

![image-20210413151221943](HomeAssistant%E6%90%AD%E5%BB%BA%E7%AC%94%E8%AE%B0.assets/image-20210413151221943.png)

最后对HA进行亿点点的整理

![image-20210413211817172](HomeAssistant%E6%90%AD%E5%BB%BA%E7%AC%94%E8%AE%B0.assets/image-20210413211817172.png)