# increase the amount of files that an user can be open

exec { 'amount of files':
    command => "sed -i 's/5/500/g' /etc/security/limits.conf",
    path    => ['/usr/bin', '/usr/sbin', '/bin' ],
}

exec { 'soft files' :
    command => "sed -i 's/4/400/g' /etc/security/limits.conf",
    path    => ['/usr/bin', '/usr/sbin', '/bin' ],
}
