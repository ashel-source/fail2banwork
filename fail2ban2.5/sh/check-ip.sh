#!/bin/bash

# 1. 获取输入 IP
if [ -z "$1" ]; then
    read -p "请输入要检查的IP: " IP
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

if [ -z "$JAILS" ]; then
    echo -e "\e[31m无法获取 Jail 列表，请检查 fail2ban 服务状态。\e[0m"
    exit 1
fi

echo -e "\e[36m正在检查 IP: $IP 在所有 Jail 中的状态...\e[0m"
echo

FOUND=0
for j in $JAILS; do
    if sudo fail2ban-client status "$j" | grep -Fw "$IP" >/dev/null; then
        echo -e "\e[31m[命中] IP: $IP 被 $j 封禁\e[0m"
        FOUND=1
    fi
done

# 5. 结果汇总
if [ "$FOUND" -eq 0 ]; then
    echo -e "\e[32m[安全] IP: $IP 目前没有被任何 Jail 封禁。\e[0m"
fi