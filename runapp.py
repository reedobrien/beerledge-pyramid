from paste.deploy import loadapp

application = loadapp('config:beerledge/production.ini', relative_to='.')
