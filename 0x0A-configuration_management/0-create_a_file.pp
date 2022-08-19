#  Create a file with Puppet
file { '/tmp/school': #the path of the new file
    content => 'I love Puppet', #this text will be inside the file
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744', #this are the permissions
    path    => '/tmp/school'
}
