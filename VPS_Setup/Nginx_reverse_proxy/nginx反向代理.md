# Nginx反向代理githubusercontent

## 效果演示

PS.原图大小34MB

反代：

![yande.re 526872 anmi ass c.c. chibi danua guts horns jiji kero l liana lime nadia nami nier pantsu puck puu revy rider saber sanji simon sword togame touhou usopp](assets/yande.re 526872 anmi ass c.c. chibi danua guts horns jiji kero l liana lime nadia nami nier pantsu puck puu revy rider saber sanji simon sword togame touhou usopp.png)

直连：

![yande.re 526872 anmi ass c.c. chibi danua guts horns jiji kero l liana lime nadia nami nier pantsu puck puu revy rider saber sanji simon sword togame touhou usopp](assets/yande.re 526872 anmi ass c.c. chibi danua guts horns jiji kero l liana lime nadia nami nier pantsu puck puu revy rider saber sanji simon sword togame touhou usopp.png)



不废话，上代码，注释有空再写

```nginx
server
    {
  	# 监听端口
		listen 80;
		listen 443 ssl;
  	server_name pic.tangyisheng2.com;
  	# SSL 常规配置
		ssl_certificate /usr/local/nginx/cert/3414705_pic.tangyisheng2.com.pem;
		ssl_certificate_key /usr/local/nginx/cert/3414705_pic.tangyisheng2.com.key;
		ssl_session_cache shared:SSL:10m;
		ssl_session_timeout  10m;
		ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;
		ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
		ssl_prefer_server_ciphers on;
		add_header Strict-Transport-Security "max-age=31536000";
		
  	# http自动跳转https
		if ( $scheme = http ){
			return 301 https://$server_name$request_uri;
		}
		
  	# 反爬虫
		if ($http_user_agent ~* (baiduspider|360spider|haosouspider|googlebot|soso|bing|sogou|yahoo|sohu-search|yodao|YoudaoBot|robozilla|msnbot|MJ12bot|NHN|Twiceler)) {
		return  403;
		}
  
  	# 反向代理设置
		location ~ .*
		{
   	 # 一些header的设置
			proxy_set_header Host raw.githubusercontent.com;
			proxy_set_header Referer "https://raw.githubusercontent.com";
			proxy_cookie_domain raw.githubusercontent.com pic.tangyisheng2.com;
			proxy_pass https://raw.githubusercontent.com;
			proxy_set_header Accept-Encoding "";

    	# 反戴后域名替换，保证链接域名和反代域名一致
			sub_filter "raw.githubusercontent.com" "pic.tangyisheng2.com";
			# 防止错误上报暴露站点
			sub_filter "js_error.php" "block_js_error";
			# 防止谷歌服务暴露站点，同时也可以加快网站加载
			sub_filter "www.google" "block_google";
			sub_filter_once off;
			sub_filter_types *;
		}
		
			# lnmp自带常规配置
        include enable-php-pathinfo.conf;

        location ~ .*\.(gif|jpg|jpeg|png|bmp|swf)$
        {
            expires      30d;
        }

        location ~ .*\.(js|css)?$
        {
            expires      12h;
        }

        location ~ /.well-known {
            allow all;
        }

        location ~ /\.
        {
            deny all;
        }

        access_log  /home/wwwlogs/pic.tangyisheng2.com.log;
    }

```

Credit：https://moe.best/technology/pixiv-proxy.html