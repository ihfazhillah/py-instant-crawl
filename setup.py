from setuptools import setup, find_packages

with open('README.md', 'r') as readme:
    long_desc = readme.read()

setup(
    name='pyinstantcrawl',
    version='1.0.1',
    description='scrape a website with json template',
    long_description=long_desc,
    url='https://github.com/ihfazhillah/py-instant-crawl',
    author='ihfazhillah',
    author_email='me@ihfazh.com',
    license='MIT',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'Click==7.0',
        'parsel==1.5.1',
        'requests==2.21.0'
    ],
    entry_points={
        'console_scripts': [
            'pyinstantcrawl=pyinstantcrawl.main:fetch'
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3 :: Only'
    ]
)
