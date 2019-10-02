# fix the bug, replace php to phpp

file { '/var/www/html/wp-settings.php':
  ensure => present,
}

file_line { 'fix':
  path => '/var/www/html/wp-settings.php',
  line => 'require_once( ABSPATH . WPINC . \'/class-wp-locale.php\' );',
  match => '^*class-wp-locale.phpp*',
}
