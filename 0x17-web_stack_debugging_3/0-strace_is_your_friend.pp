# Ensure Apache is installed and running
package { 'apache2':
  ensure => installed,
}

# Ensure PHP and necessary PHP modules for WordPress are installed
package { ['php', 'php-mysql', 'php-curl', 'libapache2-mod-php']:
  ensure => installed,
}

# Ensure WordPress directory is correctly set up with proper permissions
file { '/var/www/html':
  ensure  => directory,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
  recurse => true,
}

# Ensure Apache is pointing to the correct DocumentRoot for the WordPress site
file { '/etc/apache2/sites-available/000-default.conf':
  ensure  => file,
  content => template('apache/default.conf.erb'),
  notify  => Service['apache2'],  # Reload Apache if config changes
}

# Restart Apache to apply changes
service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => [ Package['php'], File['/var/www/html'], File['/etc/apache2/sites-available/000-default.conf'] ],
}


