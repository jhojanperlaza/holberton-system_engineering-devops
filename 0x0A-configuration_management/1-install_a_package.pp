# Using Puppet, install flask from pip3.
package { 'flask': #name of the program to be installed
  ensure   => '2.1.0', #this is the version
  provider => 'pip3',
}
