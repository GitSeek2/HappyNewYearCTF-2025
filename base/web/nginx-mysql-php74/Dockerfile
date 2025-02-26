FROM php:7.4.33-fpm-alpine

RUN sed -i 's#https\?://dl-cdn.alpinelinux.org/alpine#https://mirrors.tuna.tsinghua.edu.cn/alpine#g' /etc/apk/repositories && \
    apk add --update --no-cache \
    nginx \
    mysql mysql-client && \
    docker-php-ext-install -j$(nproc) mysqli pdo_mysql && \
    mkdir -p /run/nginx && \
    chown www-data:www-data /run/nginx && \
    mkdir -p /var/log/nginx && \
    chown -R www-data:www-data /var/log/nginx

COPY config/docker-php-ext-mysqli.ini /usr/local/etc/php/conf.d
COPY config/docker-php-ext-pdo_mysql.ini /usr/local/etc/php/conf.d
COPY config/nginx.conf /etc/nginx/nginx.conf
COPY --chown=www-data:www-data src /var/www/html
COPY --chmod=500 scripts/init.sh /init.sh

CMD ["/init.sh"]