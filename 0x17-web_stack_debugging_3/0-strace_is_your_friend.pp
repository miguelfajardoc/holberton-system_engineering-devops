# fix the bug, replace php to phpp

exec { 'replace':
  command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
  path    => ['/usr/bin', '/usr/sbin', '/bin' ],
}
