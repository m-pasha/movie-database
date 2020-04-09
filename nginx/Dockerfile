FROM nginx:1.17-alpine

WORKDIR /code

EXPOSE 80

COPY ./bundle_nginx.conf /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]
