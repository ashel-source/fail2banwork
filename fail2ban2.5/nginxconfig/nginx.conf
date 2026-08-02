        proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=my_cache:20m max_size=1g inactive=24h use_temp_path=off;
        limit_conn_zone $remote_addr zone=addr:25m;
        limit_conn_zone $request_uri zone=requri:25m;
        limit_req_zone $binary_remote_addr zone=one:35m rate=55r/s;
		#获取真实IP
        set_real_ip_from 0.0.0.0/0;
        real_ip_header X-Forwarded-For;
        
        #白名单
        geo $whitelist_ip {
            default 0;
            193.36.237.0/24 1;
			187.77.159.45 1;
         }
        #  定义限流 zone（只对非白名单生效）
        map $whitelist_ip $limit_key {
            1 "";
            0 $binary_remote_addr;
        }
        #短信限制
        limit_req_zone $binary_remote_addr zone=code_limit:10m rate=1r/m;  
        #防CC
        limit_req_zone $limit_key zone=index_limit:10m rate=10r/s; 
        #限制登录
        limit_req_zone $binary_remote_addr zone=login_limit:10m rate=3r/s;
	    #更改日志格式
        log_format main_with_host
        '$remote_addr - $remote_user [$time_local] '
        '"$request" $status $body_bytes_sent '
        '"$http_referer" "$host" "$http_user_agent" '
        'TCP-IP:$realip_remote_addr | ' 'XTT-IP:$http_x_forwarded_for | ' 'CF-IP:$http_cf_connecting_ip';
		server {
			listen 80;
			return 301 https://$host$request_uri;
		} 