# This Puppet manifest fixes the Apache 500 error caused by missing PHP modules and incorrect directory permissions.

# Ensure that the php-mysql package (required for WordPress) is installed
package { 'php-mysql':
  ensure => installed,
}

# Set correct permissions for the WordPress directory
file { '/var/www/html':
  ensure  => directory,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
  recurse => true,
}

# Restart Apache service to apply changes
service { 'apache2':
  ensure     => running,
  enable     => true,
  subscribe  => [ Package['php-mysql'], File['/var/www/html'] ],
}

