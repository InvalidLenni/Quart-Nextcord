from setuptools import setup 
requirements = [ 
     'Quart', 
     'pyjwt', 
     'oauthlib', 
     'Async-OAuthlib', 
     'cachetools', 
     'nextcord', 
 ]

on_rtd = os.getenv('READTHEDOCS') == 'True'
if on_rtd: 
     requirements.append('sphinxcontrib-napoleon') 
     requirements.append('sphinx_rtd_theme')
  
 extra_requirements = { 
     'docs': [ 
         'sphinx==1.8.3' 
     ] 
 }

setup(extra_requirements=extra_requirements)
