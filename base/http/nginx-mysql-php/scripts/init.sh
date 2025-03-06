#!/bin/sh

rm -rf /init.sh

if [ -z "$GZCTF_FLAG" ]; then
    GZCTF_FLAG="flag{seek_to_geek}"
fi

sed -i "s/flag{seek_to_geek}/$GZCTF_FLAG/g" /var/www/html/index.html
unset GZCTF_FLAG

# 初始化 MySQL 数据目录
mysql_install_db --user=mysql --datadir=/var/lib/mysql

# 启动 MySQL 服务
mysqld_safe --datadir=/var/lib/mysql &

# 等待 MySQL 启动
while ! mysqladmin ping --silent; do
    sleep 1
done

# 导入初始数据
mysql -u root </var/www/html/data.sql

# 更改 root 用户密码
mysqladmin -uroot password '123456'

php-fpm -D
nginx -g 'daemon off;'