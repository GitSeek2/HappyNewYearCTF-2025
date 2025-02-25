#!/bin/sh
if [ -z "$GZCTF_FLAG" ]; then
    GZCTF_FLAG="flag{seek_to_geek}"
fi

sed -i "s/flag{seek_to_geek}/$GZCTF_FLAG/g" /var/www/html/index.php
chmod 444 /flag
unset GZCTF_FLAG

nginx -g 'daemon off;'