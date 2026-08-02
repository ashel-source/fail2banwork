#!/bin/bash

# 1. 自动获取以 -scan 结尾的 jail，并取第一个
TARGET_JAIL=$(sudo fail2ban-client status | grep -oE "[^[:space:]]+-scan" | head -n 1)

if [ -z "$TARGET_JAIL" ]; then
    echo -e "\e[31m错误：未找到合适的封禁规则。\e[0m"
    exit 1
fi

# 2. 获取输入 IP
if [ -z "$1" ]; then
    read -p "请输入要封锁的IP: " IP
else
    IP="$1"
fi

# 3. 校验 IP
if ! python3 -c "import ipaddress; ipaddress.ip_address('$IP')" >/dev/null 2>&1; then
    echo -e "\e[31m错误：'$IP' 不是一个有效的 IP 地址。\e[0m"
    exit 1
fi

# 4. 预检查：使用 grep 精确匹配，避免误判且不会参数溢出
# 转义 IP 中的点号，确保正则表达式匹配的是字面意义的 IP
if sudo fail2ban-client status "$TARGET_JAIL" | grep -Fw "$IP" >/dev/null; then
    echo -e "\e[33m提示：IP $IP 已经在 $TARGET_JAIL 的封禁列表中，无需重复操作。\e[0m"
    exit 0
fi

# 5. 执行封锁
echo "正在执行封锁..."
if sudo fail2ban-client set "$TARGET_JAIL" banip "$IP" >/dev/null 2>&1; then
    echo -e "\e[32m成功：已在 $TARGET_JAIL 中封锁 IP：$IP\e[0m"
else
    echo -e "\e[31m失败：封锁命令执行错误，请检查权限。\e[0m"
fi

echo
echo -e "\e[36m操作完成。\e[0m"