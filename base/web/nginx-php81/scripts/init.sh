#!/bin/sh

rm -rf /init.sh

if [ -z "$GZCTF_FLAG" ]; then
    GZCTF_FLAG="flag{seek_to_geek}"
fi

sed -i "s/flag{seek_to_geek}/$GZCTF_FLAG/g" /var/www/html/index.php
unset GZCTF_FLAG

php-fpm -D
nginx -g 'daemon off;'