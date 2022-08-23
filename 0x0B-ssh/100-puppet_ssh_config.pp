#  SSH configuration file so that you can connect
# to a server without typing a password.
exec {'Client configuration file (w/ Puppet)':
    command  => 'echo "   IdentityFile ~/.ssh/holberton\n   PasswordAuthentication no" >> /etc/ssh/ssh_config',
    provider => shell
}
