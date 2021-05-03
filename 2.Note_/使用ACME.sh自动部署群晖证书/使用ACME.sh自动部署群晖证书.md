# 使用ACME.sh自动部署群晖证书

## 前言

最近群晖DSM的证书过期了，而且阿里云的免费DV证书又不再提供了，因此在考虑用acme.sh的证书服务自动部署证书。群晖其实本身有提供Let's Encrypt的证书，但是只支持使用80端口验证。由于众所周知的原因，群晖的80端口在国内并不能随便开放，因此也会导致验证失败。

## ACME脚本

ACME.sh本身就支持非常多的域名提供商，同时对DSM有专门的deployhook可以跑在局域网的其他机器上面。下为脚本：

```shell
# AliDNS 访问密钥
export Ali_Key=""
export Ali_Secret=""
# 证书生成信息
export CERT_DOMAIN=""   #域名
export CERT_DNS="dns_ali"   # 使用的DNS服务，所有支持的服务：https://github.com/acmesh-official/acme.sh/wiki/dnsapi

export SYNO_Certificate="ACME.sh"   # 证书描述
export SYNO_Create=1 # Says to create the certificate if it doesn't exist
# DSM链接信息
export SYNO_Hostname="localhost" # Specify if not using on localhost
# Single quotes prevents some escaping issues if your password or username contains certain special characters
export SYNO_Username='' # 账户
export SYNO_Password='' # 密码

# export SYNO_Hostname="localhost" # Specify if not using on localhost
export SYNO_Scheme="https"
export SYNO_Port="5001"

./acme.sh --issue --home . -d "$CERT_DOMAIN" --dns "$CERT_DNS"
./acme.sh --insecure --deploy --home . -d "$CERT_DOMAIN" --deploy-hook synology_dsm
```

运行上述脚本后，DSM内就可以看见新家的证书。

但请注意，由于ACME.sh使用DNS验证方式签发的证书只有90天有效期，因此我们还是需要加入定期任务定时续期。

```shell
0 0 1 * * ./acme.sh --issue --home . -d "$CERT_DOMAIN" --dns "$CERT_DNS" && 
./acme.sh --insecure --deploy --home . -d "$CERT_DOMAIN" --deploy-hook synology_dsm
```

## 完