#  SSH configuration file so that you can connect
# to a server without typing a password.
exec {' SSH configuration file':
    command  => 'usr/bin/echo "    IdentityFile ~/.ssh/school" >> ~/etc/ssh/ssh_config',
    provider => 'shell',
}
exec {' SSH configuration file':
    command  => 'usr/bin/echo "    PasswordAuthentication no" >> ~/etc/ssh/ssh_config',
    provider => 'shell',
}
