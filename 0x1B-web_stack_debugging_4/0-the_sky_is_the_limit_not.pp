# script that use poppet to fix server

exec {'fix_server':
  command =>  'sed -i "s/15/4096/g" /etc/default/nginx && sudo service nginx restart',
  provier => 'shell',
}

