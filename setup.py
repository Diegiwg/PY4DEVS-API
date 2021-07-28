from setuptools import find_packages, setup

with open('README.md', encoding='utf-8') as f: long_description = f.read()

setup (
    name='py4devs_api',
    packages=find_packages(include=['py4devs_api']),
    version='0.2.0',
    description='A biblioteca py4devs tem por objetivo fornecer um meio simples de utilizar as incriveis ferramentas desenvolvidas pela equipe 4DEVS.COM.BR diretamente nos scripts/projetos python.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Diego Queiroz [Diegiwg]',
    author_email='diegiwg@gmail.com',
    license='MIT',
    url='https://github.com/Diegiwg/PY4DEVS-API',
    download_url = 'https://github.com/Diegiwg/PY4DEVS-API/archive/refs/tags/v0.2.0.tar.gz',
    install_requires=['requests==2.26.0','beautifulsoup4==4.9.3'],
    classifiers=[
	    'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
	    'Topic :: Software Development :: Build Tools',
	    'License :: OSI Approved :: MIT License',
	    'Programming Language :: Python :: 3',
	    'Programming Language :: Python :: 3.4',
	    'Programming Language :: Python :: 3.5',
	    'Programming Language :: Python :: 3.6'
	  ]
)