bind = 'unix:/local/run/shoresy.sock'

workers = 5
worker_class = 'gthread'
worker_timeout = 600

syslog = True
user = 'shoresy'
group = 'www-data'

preload_app = True
