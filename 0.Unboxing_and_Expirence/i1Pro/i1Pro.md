# 给显示器校个色？i1 Display Pro简单上手体验

## 写在前面

![img](assets/IMG_0997-1567345190531.jpg)

笔者在学校的台式电脑分别是由两块屏幕组成的，由于两块屏幕年份不一，亮度不一，导致屏幕一直有肉眼可见的色差，所以就想到了校色的办法。

为啥要校色？

- 多显示器之间色彩不一，看着难受。
- 某些软件支持套用LUT，通过套用校色仪生成的Lut，可以对輸入的色彩信息进行转换后再显示在软件界面上，从而提高色彩表现。

对于校色的一点误区：

- 校色并不能让你的1000块显示器有媲美10000块显示器的屏幕素质，他只能在一定程度上改善你的显示器色彩还原。
- 有得必有失，校准可能会令显示器丢失一部分灰阶，如下图蓝色和绿色部分。

![校准曲线 LTN133HL05902 #1 2019-04-27 22-56 D6500 2.2 F-S XYZLUT+MTX](assets/校准曲线 LTN133HL05902 #1 2019-04-27 22-56 D6500 2.2 F-S XYZLUT+MTX.png)

**由于笔者不是专业的影像工作人员，旨在分享较色仪的使用体验，如有纰漏还请指出~**

**TIP：因为一些原因，本文中的截图有可能是笔记本内建屏幕+Dell U2719DS截图随机出现，还请见谅~**

## 较色仪的选择

较色仪市面上比较主流的有**Datacolor**和**X-Rite**两家。由于没有专业需求不需要日常校色并且较色仪本身也是消耗品，所以选择了在马云家进行租赁而不是购买，本次租的是**X-Rite i1Display Pro**，相关店铺很多，淘宝以“**较色仪 出租**”为关键字搜索就可。

## 包装

![img](assets/IMG_0983.jpg)

较色仪本身包装属久经沙场级别

![img](assets/IMG_0984.jpg)

背面是一些参数

![img](assets/IMG_0985.jpg)

里面有一张CD，一张说明书

![img](assets/IMG_0987.jpg)

较色仪本体，较色仪使用USB线进行连接，线材上夹有配重块，用于把较色仪稳妥的挂在屏幕上。（虽然包装这么惨，但是里面的较色仪保护的还是不错）

![img](assets/IMG_0990.jpg)

配重块上的标签

![IMG_0988](assets/IMG_0988.jpg)

虽然包装是久经沙场成色，所幸较色仪本身镜头还是保养的比较好的

![img](assets/IMG_0989.jpg)

底部可以上三脚架，用于校准投影仪





挂上电脑后的样子

## 校准体验

首先你需要下载两个软件，分别为DisplayCAL和ArgyIICMS，这两个软件都能在DisplayCAL的官网找到。DisplayCAL的官网直接上Bing搜索“DisplayCAL”即可，本文最后也会给出下载链接。

初次打开DisplayCAL会提示需要安装ArgyIICMS，直接Download即可，如果网速慢也可以手动下载然后点Browse浏览可执行文件。文章最后有给网址可供各位下载。

![1559923887253](assets/1559923887253.png)



![1559923952428](assets/1559923952428.png)

软件包含5个部分，显示器基本设置、校准、配置文件、3DLut和配置文件校验（上图篮框框住的位置）。

![1567342621176](assets/1567342621176.png)

一般来说直接调用下面Settings里面的预设就可以了。

![1559924311719](assets/1559924311719.png)





对于高级用户，可以在下面进行微调。

显示器基本设置是设置需要校准的显示器和用于校准的较色仪等基本设置。

![1559924065285](assets/1559924065285.png)

校准页有其他白点、白平衡、Gamma和校准速度的设置。这里的校准速度选择默认即可，否则DisplayCAL会在灰阶上浪费很多时间，对普通显示器得不偿失。

![1559924167020](assets/1559924167020.png)

配置文件页我唯一看懂的就是文件名...（个人认为保持默认就好）

![1559924190680](assets/1559924190680.png)

3DLut页不是很懂

![1559924214259](assets/1559924214259.png)

最后的验证页可以测量校准后显示器的颜色表现。

![1559924268215](assets/1559924268215.png)

回到显示器设置页，点Calibrate & profile，软件会弹出一个白色方框，将较色仪放置在上面，点击Start Measurement之后软件会测量白点和亮度，可以根据需要调整。调整完后点Stop Measurement和Continue on to calibration。

![1559924381056](assets/1559924381056.png)

![img](assets/IMG_0992-1559924486626.jpg)

然后等读条就好了~

![img](assets/IMG_0993.jpg)

测试结束后有弹窗显示测试结果。

![1559924602715](assets/1559924602715.png)

简单解释下上面的参数：

△E表示色彩还原准度，越小越好

Gamut Coverage表示不同色彩标准下的色域覆盖，越大越好

我们选择install profile，当安装成功后就可以关掉DisplayCAL了。接下来DisplayCAL Profile Loader就会自动帮我们加载配置文件了。

![1559924643687](assets/1559924643687.png)

并且，在显示设置中也能看到刚刚生成的配置文件已经被安装。

![1559924698460](assets/1559924698460.png)

如果需要变更某个显示器的配置文件设定，右击DisplayCAL Profile Loader，选择Profile associations，就可以为显示器安装或者设置其他的配置文件了。

![1559924885220](assets/1559924885220.png)

其实在MadVR里面也是同理，直接载入在Settings里面选择madvr预设就可以生成Lut文件了，载入Lut文件就可以获得经过校色后的视频体验了~。

![1565713864055](assets/1565713864055.png)

## 校色前后色彩表现对比

校色前

![LTN133HL05902_Before](assets/LTN133HL05902_Before.png)

校色后

![LTN133HL05902_After](assets/LTN133HL05902_After.png)

## 总结

其实现在对于颜色准确度的要求已经越来越高，不管是对于高级的显示器还是低级的显示器，校色都能怼色彩准确度起到一定的帮助，可以看到上面未校准前的DeltaE已经全红，校色后部分DeltaE有改善，但是还是有部分色彩的DeltaE红了，所以说是有作用的，但是并不能让屏幕素质有质的飞跃。尽管如此，对于对色彩要求比较高的用户来说还是有一定的作用的。但是就我个人而言校色之后的观感需要一段时间适应。只有用过一般显示器的我就很种草MacBook Pro的屏幕了。

较色仪其实也是消耗品，如果只是偶尔需要校色的话个人建议还是去淘宝租用会比直接购买划得来~

最后文章有点拖太久了，已经记不清当初想说什么了哈哈哈~

由于本文定位仅是简短体验，有一些概念也碍于篇幅不能交代清楚，如果各位姥爷对色彩管理感兴趣的话，不妨看看下面的参考资料，里面有比较详细的描述。

如果各位看官老爷喜欢的话还请收藏点赞评论一条龙哦，先在此谢谢各位看官姥爷了如果有其它问题还请在评论区留言~我会抽时间看的233.

下次就有可能是MBP或者AirPods或者iPhone Xr的体验，还请期待~

## 其他的参考资料

因为直接贴连接会被吞所以只提供关键字供各位感兴趣看官姥爷做一些延伸阅读。

1.知乎：张兴.3D LUT --色彩校正的利器 https://zhuanlan.zhihu.com/p/37147849

2.Khan Academy：Color Science https://www.khanacademy.org/partner-content/pixar/color

3.Chiphell 视频影像玩转显示器硬件3D LUT - 英国LightSpace不完整使用记 https://www.chiphell.com/thread-2021887-1-1.html

4.DisplayCal https://displaycal.net/#download

5.ArgyIICMS http://www.argyllcms.com/