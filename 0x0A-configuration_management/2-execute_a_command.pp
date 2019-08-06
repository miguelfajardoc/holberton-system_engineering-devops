# kill a program
exec { 'killmenow':
  command  => 'pkill killmenow',
  provider => shell
}