from setuptools import setup

setup(
    name='ass',
    version='0.4.3',
    description='A library for parsing and manipulating Advanced SubStation Alpha subtitle files.',
    author='Tony Young',
    author_email='python-ass@chireiden.net',
    keywords='ass subtitle substation alpha',
    packages=['ass'],
    url='http://github.com/chireiden/python-ass',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Video',
        'Topic :: Software Development :: Libraries',
        'Topic :: Text Processing :: Markup',
    ],
    install_requires=['setuptools'],
    zip_safe=True,
)
