# Fix apache server issue                                                  

exec{'fix-phpfile':
command => 'sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php',
path    => '/bin',
}

