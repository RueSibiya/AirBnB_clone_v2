#Ensure web_static directory exists
file { '/data/web_static':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Ensure releases and shared directories exist inside web_static
file { '/data/web_static/releases':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
}

file { '/data/web_static/shared':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
}

# Ensure symbolic link to current exists and points to releases/test
file { '/data/web_static/current':
  ensure  => 'link',
  owner   => 'root',
  group   => 'root',
  target  => '/data/web_static/releases/test',
  require => File['/data/web_static/releases'],
}

# Create index.html inside releases/test
file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => File['/data/web_static/releases/test'],
}
