# ROS获取电信原生ipv6

Step1：System - Packages确认ipv6已经安装并启用

![image-20200224164440879](assets/image-20200224164440879.png)

Step2：IPv6 - DHCP Client新增Client，request选择prefix，Pool Name自定义，Prefix Length选64

![image-20200224164613755](assets/image-20200224164613755.png)

Step3：IPv6 - Addresses，给LAN网桥分配IPv6地址，Address除输入“::/64”，Interface选择bridge1（LAN网桥）

![image-20200224164817258](assets/image-20200224164817258.png)

Step4：二级路由中，IPv6设置为Passthrough

![image-20200224164948685](assets/image-20200224164948685.png)

Step5：重新获取DHCP

![image-20200224165021650](assets/image-20200224165021650.png)

![image-20200224165124860](assets/image-20200224165124860.png)

Enjoy！

## Credit：

- RouterOS 配置电信双栈原生IPv6 及IPv6公网地址分配 https://blog.ich8.com/post/6015