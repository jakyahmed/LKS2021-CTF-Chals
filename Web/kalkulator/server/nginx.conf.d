upstream kalkulator {
  server    kalkulator:5000;
}

server {
    listen 80;
    error_log  /var/log/nginx/error.log;
    access_log /var/log/nginx/access.log;
    location / {
        proxy_pass http://kalkulator;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $remote_addr;
    }
}