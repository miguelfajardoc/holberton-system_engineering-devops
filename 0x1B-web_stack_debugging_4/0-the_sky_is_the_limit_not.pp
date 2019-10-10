# debug nginx

exec { 'more files':
     command => "sed -i 's/15/4096/g' /etc/default/nginx",
     path => ['/usr/bin', '/usr/sbin', '/bin' ],
}->
exec { 'restar nginx':
     command => "sudo service nginx restart ",
     path => ['/usr/bin', '/usr/sbin', '/bin' ],
} 	 