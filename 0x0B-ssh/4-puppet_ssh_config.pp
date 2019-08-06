# change the client ssh configuration with puppet master
file { '/etc/ssh/ssh_config':
  ensure => present,
}
file_line { 'change authentication':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => '^PasswordAuthentication.*$',
}
file_line { 'set identity file':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/holberton',
  match  => '^IdentityFile.$',
}