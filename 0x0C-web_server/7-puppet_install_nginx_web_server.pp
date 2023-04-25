#Install Nginx web server

package { 'nginx':
  ensure => installed
}

file { '/var/www/html/index.html':
  content => "Hello World!\n",
}

file { '/etc/nginx/sites-available/default':
  content => "
server {
  listen 80;
  root /var/www/html;
  index index.html;
  location /redirect_me {
    return 301 /redirected;
  }
}",
}

file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
}

service { 'nginx':
  ensure => running,
  enable => true,
}
