#Puppet script that automate task of creating a custom HTTP header response
class nginx {
  package { 'nginx':
    ensure => 'installed',
  }

  service { 'nginx':
    ensure => 'running',
    enable => true,
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => 'file',
    content => template('nginx/default.conf.erb'),
    notify  => Service['nginx'],
  }
}

class nginx::headers {
  file { '/etc/nginx/conf.d/custom-headers.conf':
    ensure  => 'file',
    content => template('nginx/custom-headers.conf.erb'),
    notify  => Service['nginx'],
  }
}

class nginx::headers::params {
  $hostname = $::hostname

  file { '/etc/nginx/conf.d/custom-headers.conf':
    content => template('nginx/custom-headers.conf.erb'),
    notify  => Service['nginx'],
  }
}

include nginx
include nginx::headers
include nginx::headers::params
