#!/bin/bash

# 1. 获取输入 IP
if [ -z "$1" ]; then
    read -p "请输入要解封的IP: " IP
else
    IP="$1"
fi

# 2. 校验 IP 格式
if ! python3 -c "import ipaddress; ipaddress.ip_address('$IP')" >/dev/null 2>&1; then
    echo -e "\e[31m错误：'$IP' 不是一个有效的 IP 地址。\e[0m"
    exit 1
fi

# 3. 获取所有正在运行的 jail
JAILS=$(sudo fail2ban-client status | grep "Jail list" | sed 's/.*Jail list:[ ]*//; s/,/ /g')

echo "正在从所有封禁规则中解封 IP: $IP ..."
echo

# 4. 优化：直接使用 grep -Fw 进行匹配，不再需要 sed 转义
for j in $JAILS; do
    # -F: 固定字符串模式，-w: 全字匹配
    if sudo fail2ban-client status "$j" | grep -Fw "$IP" >/dev/null; then
        echo -e "\e[33mIP: $IP 被 $j 封禁 → 正在解封...\e[0m"
        
        if sudo fail2ban-client set "$j" unbanip "$IP" >/dev/null 2>&1; then
            echo -e "\e[32m成功：已从 $j 中解封 IP：$IP\e[0m"
        else
            echo -e "\e[31m失败：无法解封 $j 中的 IP：$IP\e[0m"
        fi
    else
        echo "IP: $IP 没有被 $j 封禁"
    fi
done

echo
echo -e "\e[36m操作完成。\e[0m"