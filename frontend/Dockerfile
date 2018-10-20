FROM nginx:1.13-alpine

COPY conf/nginx.conf /etc/nginx/nginx.conf
RUN mkdir -p /usr/share/nginx/html/static
COPY dist/*.html /usr/share/nginx/html/
COPY dist/dist /usr/share/nginx/html/dist
COPY dist/src /usr/share/nginx/html/src
COPY dist/demo /usr/share/nginx/html/demo
