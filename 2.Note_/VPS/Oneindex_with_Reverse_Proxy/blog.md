# Oneindex反向代理：实现高速下载

# 前言

Oneindex是一款优秀的OneDrive分享前端，相比h5ai，有以下的优点：

- 不占服务器本地硬盘
- 不跑服务器本地流量

但是在国内因为众所周知的原因，OneDrive的连通性并不好，因此造成了使用Oneindex下载慢的问题，利用nginx的反向代理功能实现下载加速，需要注意的是，这样操作后Oneindex的下载将走服务器本地流量，如果是按流量付费的服务器请慎用。

# 准备：

- Nginx
- Oneindex
- acme.sh（用于签发SSL证书）
- Onedrive下载域名：public.by.files.1drv.com（可以在Oneindex中随便下载一个文件获取）

# Nginx反代设置：

这里使用LNMP建立网站，并配备SSL证书，在原有LNMP的vhost config的基础上，新增两个location如下

```nginx
location  ~* \.(php|jsp|cgi|asp|aspx)$
    {
        proxy_pass https://yours.sharepoint.com;#把这里改成使用宝塔面板步骤3、步骤4的截选出的链接
        proxy_set_header Host yours.sharepoint.com;#把这里改成上面链接去掉https://
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header REMOTE-HOST $remote_addr;
        proxy_set_header Range $http_range;#此项感谢评论区超音速的提醒
    }
    location /
    {
        proxy_pass https://yours.sharepoint.com;#把这里改成使用宝塔面板步骤3、步骤4的截选出的链接
        proxy_set_header Host yours.sharepoint.com;#把这里改成上面链接去掉https://
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header REMOTE-HOST $remote_addr;
        proxy_set_header Range $http_range;#此项感谢评论区超音速的提醒
        
        add_header X-Cache $upstream_cache_status;
        add_header Cache-Control no-cache;
        expires 12h;
    }
```

经过测试开启rewrite之后会狂跑流量，所以此处关闭rewrite，注释掉此行

```nginx
# include rewrite/other.conf;
```

# 修改Oneindex程序：

在lib/onedrive.php下找到此段

```php
//通过分页获取页面所有item
static function dir_next_page($request, &$items, $retry=0){
	$resp = fetch::get($request);
	
	$data = json_decode($resp->content, true);
	if(empty($data) && $retry < 3){
		$retry += 1;
		return self::dir_next_page($request, $items, $retry);
	}
	
	foreach((array)$data['value'] as $item){
		//var_dump($item);
		$items[$item['name']] = array(
			'name'=>$item['name'],
			'size'=>$item['size'],
			'lastModifiedDateTime'=>strtotime($item['lastModifiedDateTime']),
			'downloadUrl'=>$item['@microsoft.graph.downloadUrl'],
			'folder'=>empty($item['folder'])?false:true
		);
	}

	if(!empty($data['@odata.nextLink'])){
		$request = self::request();
		$request['url'] = $data['@odata.nextLink'];
		return self::dir_next_page($request, $items);
	}
}
```

将第16行替换为

```PHP
'downloadUrl'=>str_ireplace("截取的链接","反代的链接",$item['@microsoft.graph.downloadUrl']),
```

# 后记

没有，懒

# Credits

1. [反代 OneDrive ：OneIndex 实现高速下载在线观看视频](https://www.nbmao.com/archives/3917)

