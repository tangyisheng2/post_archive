# Apple Watch开启ECG功能

## 0.前言：

在Apple Watch Series 4上面苹果就已经加入了ECG功能，但是由于一些审查原因迟迟未能在中国使用。最近看了Reddit上[u/x43x61x69](https://www.reddit.com/user/x43x61x69/)的研究（我把原帖地址放在最后），测试出了这个可以说是最保险的ECG激活方法，不用登陆别人ID，不用给ID别人激活，你的iCloud信息也不会被污染。

答应我如果你也成功开启请在下方留言让我知道，如果文章对你有用请不要忘记一条龙，拜托啦这对我真的很重要～

你可以在这里查询你的手表是否支持ECG功能：https://www.apple.com/watchos/feature-availability/#branded-ecg

测试条件：

iPhone XR 国行 - iOS 13.3

Apple Watch Series 5 加拿大版 - Watch OS 6.1.1

**免责声明：这个方法仅仅适用于个人学习之用，个人不对使用造成的任何后果负责。**

另外转载请附上原作者（包括我和reddit原帖）的信息，尊重他人劳动成果谢谢。

## 1.准备材料

Apple Watch一支

iPhone手机一个

电脑一台

IMazing软件（收费软件，用于编辑备份）

大约4个小时的空闲时间（依照个人手机内容不同而不同）

## 2.开始整活

首先的首先，咱们没有尝试过国行手表，所以能不能用我也不太清楚，请先确认你的手表上有ECG的APP，如下图中间所示。

![IMG_7082](/Users/tangyisheng2/OneDrive/post/Apple Watch ECG/assets/IMG_7082.PNG)

首先使用IMazing软件对手机做一次加密备份，一定要是加密备份这样才会备份你的健康数据。

![image-20200115200125542](/Users/tangyisheng2/OneDrive/post/Apple Watch ECG/assets/image-20200115200125542.png)

打开软件，链接iPhone，选择右边的备份(Back up)

![image-20200115200351694](/Users/tangyisheng2/OneDrive/post/Apple Watch ECG/assets/image-20200115200351694.png)

这里千万注意备份加密一定要开启，不然健康信息无法备份

![Screen Shot 2020-01-14 at 1.50.32 PM](/Users/tangyisheng2/OneDrive/post/Apple Watch ECG/assets/Screen Shot 2020-01-14 at 1.50.32 PM.png)

![Screen Shot 2020-01-14 at 4.46.23 PM](/Users/tangyisheng2/OneDrive/post/Apple Watch ECG/assets/Screen Shot 2020-01-14 at 4.46.23 PM.png)

耐心等待备份完成

![image-20200115201555531](/Users/tangyisheng2/OneDrive/post/Apple Watch ECG/assets/image-20200115201555531.png)

我们准备的plist，长这样，下载地址我会放在最后

![image-20200115201711759](/Users/tangyisheng2/OneDrive/post/Apple Watch ECG/assets/image-20200115201711759.png)

找到我们刚刚的备份，选edit

![Screen Shot 2020-01-14 at 9.02.57 PM](/Users/tangyisheng2/OneDrive/post/Apple Watch ECG/assets/Screen Shot 2020-01-14 at 9.02.57 PM.png)

点击edit之后他会帮你把备份复制一遍，防止翻车

![image-20200115230038964](/Users/tangyisheng2/OneDrive/post/Apple Watch ECG/assets/image-20200115230038964.png)

然后打开刚刚复制的可编辑的备份，进入HomeDomain-Library-Preferences，把刚刚的plist拖进去，就算是大功告成了

![image-20200115230402727](/Users/tangyisheng2/OneDrive/post/Apple Watch ECG/assets/image-20200115230402727.png)

接下来我们将修改好的备份恢复到手机中

![Screen Shot 2020-01-14 at 10.34.08 PM](/Users/tangyisheng2/OneDrive/post/Apple Watch ECG/assets/Screen Shot 2020-01-14 at 10.34.08 PM.png)

![image-20200115230449741](/Users/tangyisheng2/OneDrive/post/Apple Watch ECG/assets/image-20200115230449741.png)

个人用时大约两个小时，并且期间手机是不能使用的状态，因此请提前预留充足时间

![D1CE5C17-C892-40FD-97E1-3C1B5729665F_1_105_c](/Users/tangyisheng2/OneDrive/post/Apple Watch ECG/assets/D1CE5C17-C892-40FD-97E1-3C1B5729665F_1_105_c.jpeg)

进入系统后打开Watch App，可以看到自动同步中，我们需要重新配对一次手表。点击返回，Apple Watch会被重置

![DFCABD2F-0FED-4F9E-B34C-00E3058DADC8_1_105_c](/Users/tangyisheng2/OneDrive/post/Apple Watch ECG/assets/DFCABD2F-0FED-4F9E-B34C-00E3058DADC8_1_105_c.jpeg)

![0134DCAA-7B2D-4E45-B828-DC1A18A26812_1_105_c](/Users/tangyisheng2/OneDrive/post/Apple Watch ECG/assets/0134DCAA-7B2D-4E45-B828-DC1A18A26812_1_105_c.jpeg)

在重新配对的时候请选择“设置为新的Apple Watch”，其余初始化步骤照常，在初始化完成后你就可以直接使用ECG的APP了，此时进入健康APP在心脏选单中也能看到ECG了

![281E7293-E48E-41FD-819E-BFDA8E63E57E_1_105_c](/Users/tangyisheng2/OneDrive/post/Apple Watch ECG/assets/281E7293-E48E-41FD-819E-BFDA8E63E57E_1_105_c.jpeg)

![1B36D059-E9BA-4927-B062-6987E13F4F98_1_105_c](/Users/tangyisheng2/OneDrive/post/Apple Watch ECG/assets/1B36D059-E9BA-4927-B062-6987E13F4F98_1_105_c.jpeg)

## 3.后记

其实并没有什么后记，相较于上某宝找ECG代激活来说可以保证个人的资料以及账户不被泄漏，也不用专门跑香港激活，唯一的缺点可能就是消耗时间以及买IMazing的激活需要花几十块，看个人权衡了。

由于手边没有国行的Apple Watch所以也无法测试，不过我估计应该是不能的吧。

最后是plist地址：https://gist.github.com/x43x61x69/0a9dd6e134c5c4a7ce39c9aab5639727

reddit地址：https://www.reddit.com/r/AppleWatch/comments/dhsbft/tutorial_apple_watch_ecg_activation_anywhere/

原本想写Apple Watch的体验先的，但是因为这个比较有趣而且好像没什么人写的样子，最后感谢各位观众老爷能看到这里啦，如果我的文章对你有那么一点点的帮助的话请不要忘记关注、打赏、收藏评论一条龙哦，也欢迎姥爷将它分享给你们所有要开ECG的朋友，那么就这样我们稍后再见～