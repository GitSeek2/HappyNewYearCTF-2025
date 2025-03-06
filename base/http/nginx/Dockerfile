FROM nginx:alpine

COPY --chown=nginx:nginx config/nginx.conf /etc/nginx/nginx.conf
COPY --chown=nginx:nginx src /var/www/html
COPY --chmod=500 scripts/init.sh /init.sh

CMD ["/init.sh"]