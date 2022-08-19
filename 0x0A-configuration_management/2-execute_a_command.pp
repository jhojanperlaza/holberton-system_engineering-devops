exec {'create a manifest that kills a process named killmenow':
    command  => 'pkill killmenow',
    provider => shell
}
