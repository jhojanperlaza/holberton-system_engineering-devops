# Using Puppet, create a manifest that kills a process named killmenow.
exec {'kill_file_killmenow':
    command  => 'pkill killmenow',
    provider => shell
}
