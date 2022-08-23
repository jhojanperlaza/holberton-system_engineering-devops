#  SSH configuration file so that you can connect
# to a server without typing a password.
exec {'Client configuration file (w/ Puppet)':
    command  => 'echo "Hello World" >> ~/.ssh/school',
    provider => shell
}
