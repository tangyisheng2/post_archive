**swap的功能与相应内核参数**

Linux 将物理内存分为内存段的部分被称作“页面”。交换是指内存页面被复制到预先设定好的硬盘空间(叫做交换空间)的过程，目的是释放用于页面的内存。物理内存和交换空间的总大小是可用的虚拟内存的总量。交换空间通常是一个磁盘分区（此分区在安装操作系统时，系统通常会默认划分出一段空间用于交换分区，默认将交换空间的大小设定为内存的1倍到2倍），也可以是一个文件。

内核参数中有一个vm.swappiness参数，此参数代表了内核对于交换空间的喜好(或厌恶)程度。Swappiness 可以有 0 到 100 的值，默认的大小通常是60，但也有的是30。设置这个参数为较低的值会减少内存的交换，从而提升一些系统上的响应度。如果内存较为充裕，则可以将vm.swappiness大小设定为30，如果内存较少，可以设定为60。如果将此数值调整的过大，可能损失内存本来能提供的性能，并增加磁盘IO消耗和CPU的消耗。

**关于阿里云云主机swap功能**

阿里云提供的云服务器（Elastic Compute Service，简称 ECS），是云主机的一种，当前采用的虚拟化驱动是Xen（这一点可以通过bios vendor和virtual type可以看出）。

默认情况下，阿里云云主机的swap功能是没有启用的，原因当然是通过取消swap功能可以降低磁盘IO的占用率来让用户购买更多的内存、提高磁盘寿命和性能。

阿里当前的做法是：

1.不创建swap分区，由镜像决定

2.将vm.swappiness设定为0，即永不使用swap分区

启用swap分区，确实可以降低内存的使用压力，但并不是长久之计，如果云主机上运行的应用确实需要较高的内存，建议还是购买更多的内存。

**如何启用swap分区？**

步骤如下：

1.查看当前系统中是否已经启用swap分区

```shell
cat` `/proc/swaps`  `top
```

2.如果没有启用swap分区功能，则新建一个专门的文件用于swap分区

```shell
dd` `if``=``/dev/zero` `of=``/data/swap` `bs=512 count=8388616
```

注：此文件的大小是count的大小乘以bs大小，上面命令的大小是4294971392，即4GB

3.通过mkswap命令将上面新建出的文件做成swap分区

```shell
mkswap ``/data/swap
```

4.查看内核参数vm.swappiness中的数值是否为0，如果为0则根据实际需要调整成30或者60

```shell
cat` `/proc/sys/vm/swappiness`  `sysctl -a | ``grep` `swappiness  ``sysctl -w vm.swappiness=60
```

注：若想永久修改，则编辑/etc/sysctl.conf文件

5.启用此交换分区的交换功能

```shell
swapon ``/data/swap`  `echo` `"/data/swap swap swap defaults  0 0"` `>> ``/etc/fstab
```

**如何关闭swap分区？**

```shell
swapoff ``/data/swap`  `swapoff -a >``/dev/null
```

**关于多个交换分区在使用上的优先级**   
如果你有多于一个交换文件或交换分区，你可以给它们各自分配一个优先级值(0 到 32767)。系统会在使用较低优先级的交换区域前优先使用较高优先级的交换区域。例如，如果你有一个较快的磁盘 (/dev/sda) 和一个较慢的磁盘 (/dev/sdb)，给较快的设备分配一个更高的优先级。优先级可以在 fstab 中通过 pri 参数指定：   

```shell
/dev/sda1` `none swap defaults,pri=100 0 0  ``/dev/sdb2` `none swap defaults,pri=10 0 0
```

或者通过 swapon 的 ?p (或者 ??priority) 参数：   

```shell
swapon -p 100 ``/dev/sda1
```

如果两个或更多的区域有同样的优先级，并且它们都是可用的最高优先级，页面会按照循环的方式在它们之间分配。

**添加效果**

PS: 原先对阿里云主机添加swap分区是否起作用表示质疑，现在看来，阿里在云主机中确实没做这方面的手脚。

[![image](http://s3.51cto.com/wyfs02/M01/7E/E7/wKiom1cMbsLQCaMLAAB1XeqCGrI292.png)](https://yq.aliyun.com/go/articleRenderRedirect?spm=a2c4e.11153940.0.0.1810a64dOxbVNB&url=http%3A%2F%2Fs3.51cto.com%2Fwyfs02%2FM01%2F7E%2FE7%2FwKiom1cMbsLynelyAAByUXblfHk649.png)

注：关于top命令中的排序：top命令里面按下f或F，在通过箭头移动想要显示或者排序的列，按d表示显示或取消显示，按下s表示按此列排序，按下R表示翻转排序顺序。

**一些可用的参考资料和扩展阅读材料：**

Swap [https://wiki.archlinux.org/index.php/Swap](https://yq.aliyun.com/go/articleRenderRedirect?url=https%3A%2F%2Fwiki.archlinux.org%2Findex.php%2FSwap)   
All about Linux swap space [https://www.linux.com/news/all-about-linux-swap-space](https://yq.aliyun.com/go/articleRenderRedirect?url=https%3A%2F%2Fwww.linux.com%2Fnews%2Fall-about-linux-swap-space)

云服务器 ECS https://www.aliyun.com/product/ecs

tag:Linux swap,阿里云添加swap交换空间,swap性能优化,云主机性能优化,云服务器性能优化

--end--

