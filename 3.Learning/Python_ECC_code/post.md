# 前言
这题原本是作业题，感觉有点意思就将思路和Python的实现放上来分享，顺便当本博客的最后一篇博文，以示纪念。
（主要是阿里云不给我继续用优惠价续费了，嗨）

# 题目要求

采用奇校验方法，码流格式为 A6 A5 A4 A3 A2 A1 A0 (A6 A5 A4为监督码,A3 A2 A1 A0为信息码), 其中A6为 A3 A2 A1 的奇校验，A5为 A3 A1 A0 的奇校验，A4为 A2 A1 A0 的奇校验，试找出如下接收到的码流的错码并作纠正。


<!--more-->



```
(1) 1100001 ---- 1000001
(2) 1110110 ---- 1010110
(3) 1110101 ---- 1111101
(4) 0101000 ---- 0101001
(5) 0000000 ---- 0000010
(6) 0000110 ---- 0000010
(7) 0011111 ---- 0001111
(8) 1000011 ---- 1000001
```
由奇校验可得

$$
\begin{aligned}
A6  \oplus A3  \oplus A2  \oplus A1 = 1\\
A5  \oplus A3  \oplus A1  \oplus A0 = 1\\
A4  \oplus A2  \oplus A1  \oplus A0 = 1\\
 \end{aligned}
$$

因此由编程可得以下结果：

```
Input data:1100001
Origin:[1, 1, 0, 0, 0, 0, 1],Corrected:[1, 0, 0, 0, 0, 0, 1],found error at bit:[5]
Input data:1110110
Origin:[1, 1, 1, 0, 1, 1, 0],Corrected:[1, 0, 1, 0, 1, 1, 0],found error at bit:[5]
Input data:1110101
Origin:[1, 1, 1, 0, 1, 0, 1],Corrected:[1, 1, 1, 1, 1, 0, 1],found error at bit:[5, 6]
Input data:0101000
Origin:[0, 1, 0, 1, 0, 0, 0],Corrected:[0, 1, 0, 1, 0, 0, 1],found error at bit:[4, 5]
Input data:0000000
Origin:[0, 0, 0, 0, 0, 0, 0],Corrected:[0, 0, 0, 0, 0, 1, 0],found error at bit:[4, 5, 6]
Input data:0000110
Origin:[0, 0, 0, 0, 1, 1, 0],Corrected:[0, 0, 0, 0, 0, 1, 0],found error at bit:[4, 6]
Input data:0011111
Origin:[0, 0, 1, 1, 1, 1, 1],Corrected:[0, 0, 0, 1, 1, 1, 1],found error at bit:[4]
Input data:1000011
Origin:[1, 0, 0, 0, 0, 1, 1],Corrected:[1, 0, 0, 0, 0, 0, 1],found error at bit:[4, 5, 6]
```

在错误位数为1bit的时候，我们对监督码做修正，在错误位数>1bit的时候，我们则考虑对信息码进行修正。

# 编程实现

```python
"""
@File    :   ECC
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2020, Tang Yisheng

@Modify Time        @Author     @Version        @Description
------------        -------     --------        -----------
2020/6/25     tangyisheng2        1.0             Release
"""


def conver_to_int(data_to_convert):
    data_converted = list()
    for str_data in data_to_convert:
        data_converted.append(int(str_data))
    return data_converted[::-1]  # 反序


def parity_check(data: list):
    check_result = list()  # A4,A5,A6
    if (data[4] ^ data[0] ^ data[1] ^ data[2]) == 0:
        check_result.append(4)
    if (data[5] ^ data[0] ^ data[1] ^ data[3]) == 0:
        check_result.append(5)
    if (data[6] ^ data[1] ^ data[2] ^ data[3]) == 0:
        check_result.append(6)
    return check_result


def change_bit(bit):
    if bit:
        return 0
    elif ~bit:
        return 1


def correct_error(bit, data_list):
    if bit.__len__() == 1:
        bit = bit.pop()  # 将list转为int
        data_list[bit] = change_bit(data_list[bit])
    elif bit.__len__() > 1:
        if bit == [4, 5, 6]:
            data_list[1] = change_bit(data_list[1])
        elif bit == ([4, 5] or [5, 4]):
            data_list[0] = change_bit(data_list[0])
        elif bit == ([5, 6] or [6, 5]):
            data_list[3] = change_bit(data_list[3])
        elif bit == ([4, 6] or [6, 4]):
            data_list[2] = change_bit(data_list[2])
    return data_list


if __name__ == '__main__':
    while True:
        data = input("Input data:")
        if data == "":
            exit(0)
        data_list = conver_to_int(data)
        result_bit = parity_check(data_list)
        result_bit_tmp = parity_check(data_list)
        print(f'{"Origin:"}{data_list[::-1]},{"Corrected:"}{correct_error(result_bit, data_list)[::-1]}'
              f'{",found error at bit:"}{result_bit_tmp}')

```