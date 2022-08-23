#  SSH configuration file so that you can connect
# to a server without typing a password.
file {'/etc/ssh/ssh_config':
  ensure   => 'present',
}
exec {' SSH configuration file':
  command  => '/usr/bin/echo "    IdentityFile ~/.ssh/school\n    PasswordAuthentication no" >> ~/etc/ssh/ssh_config',
  provider => 'shell',
}
