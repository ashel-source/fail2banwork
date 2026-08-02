#!/bin/bash

# 严谨模式：遇到错误立即停止
set -e

if [[ $EUID -ne 0 ]]; then
    echo "请以 root 用户身份运行此脚本" 
    exit 1
fi

F2B_CLIENT="/usr/bin/fail2ban-client"

echo "[1/9] 正在停止 Fail2Ban 服务..."

# 检查客户端工具是否存在
if [ -x "$F2B_CLIENT" ]; then
    if $F2B_CLIENT stop; then
        echo "Fail2Ban 服务已成功关闭。"
    else
        echo "Fail2Ban 服务关闭失败（可能是因为服务未运行或权限不足）。"
    fi
else
    echo "错误：未找到 $F2B_CLIENT，请检查安装路径。"
    exit 1
fi

echo "[2/9] 正在安装依赖..."
apt update && apt install ipset -y

# 定义源目录
SRC_DIR="/www/fail2ban2.5"
[ ! -d "$SRC_DIR" ] && { echo "错误: 源目录 $SRC_DIR 不存在"; exit 1; }

echo "[3/9] 正在拷贝文件..."
cp -rf "$SRC_DIR/fail2banpy/"* "/www/server/panel/plugin/fail2ban/"
cp -rf "$SRC_DIR/fail2ban/action.d/"* "/etc/fail2ban/action.d/"
cp -rf "$SRC_DIR/sh/"* "/usr/local/bin/"
cp -rf "$SRC_DIR/log/"* "/etc/logrotate.d/"
cp -rf "$SRC_DIR/waf" "/www/server/panel/vhost/"
cp -rf "$SRC_DIR/nginxconfig" "/www/server/panel/vhost/"


echo "[4/9] 正在设置文件权限..."
chmod 644 /etc/fail2ban/action.d/nginx-block-iptables-ipset.conf \
          /etc/fail2ban/action.d/iptables-ipset.conf \
          /etc/fail2ban/jail.local \
          /www/server/panel/plugin/fail2ban/fail2ban_main.py \
          /www/server/panel/plugin/fail2ban/index.html \
          /etc/logrotate.d/fail2ban

chmod 755 /usr/local/bin/check-ip.sh \
          /usr/local/bin/unban-ip.sh \
          /usr/local/bin/ban-ip.sh

chown -R root:root /etc/fail2ban/action.d /www/server/panel/plugin/fail2ban /usr/local/bin /etc/logrotate.d /www/server/panel/vhost/nginxconfig /www/server/panel/vhost/waf

find /www/server/panel/vhost/waf -type d -exec chmod 755 {} \;
find /www/server/panel/vhost/nginxconfig -type f -exec chmod 644 {} \;
echo "[5/9] 正在配置参数..."
sed -i '/^\[DEFAULT\]/,/^\[/{s/^[# ]*banaction *= *.*/banaction = nginx-block-iptables-ipset/}' /etc/fail2ban/jail.local

echo "[6/9] 正在清理旧配置..."
FILE_TO_REMOVE="/www/server/panel/vhost/nginx/blockip.conf"
if [ -f "$FILE_TO_REMOVE" ]; then
    rm -f "$FILE_TO_REMOVE"
    echo "检测到文件存在，已删除: $FILE_TO_REMOVE"
else
    echo "文件不存在，跳过删除步骤。"
fi

echo "[7/9] 正在修复网站目录权限..."
if [ -d "/www/wwwroot" ]; then
    # -f 指忽略错误，即使没有 -i 属性也不会中断
    chattr -R -f -i /www/wwwroot || true
    chown -R www:www /www/wwwroot
    find /www/wwwroot -type d -exec chmod 755 {} \;
    find /www/wwwroot -type f -exec chmod 644 {} \;
    echo "网站目录权限修复完成。"
else
    echo "警告: 目录 /www/wwwroot 不存在，跳过修复。"
fi
echo "权限修复步骤已结束，继续执行后续任务..."

echo "[8/9] 正在通过启动fail2ban..."
if [ -x "$F2B_CLIENT" ]; then
    if $F2B_CLIENT start; then
        echo "Fail2Ban 服务已成功启动。"
    else
        echo "Fail2Ban 服务启动失败。"
    fi
else
    echo "错误：未找到 $F2B_CLIENT，请检查安装路径。"
    exit 1
fi

echo "[9/9] 正在清理安装包..."
rm -rf "/www/fail2ban2.5"
rm -f "/www/fail2ban2.5.zip"

echo "安装流程已全部完成！"