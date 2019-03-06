from setuptools import setup, find_packages

setup(name='marsrover',
      version='0.1',
      description='ThoughtWorks MarsRover Solution',
      url='https://github.com/HeidiNeuhaeuser/marsrover',
      author_email='info@heidineuhaeuser.de',
      package_dir={'': '.'},
      packages=find_packages('.'),
      install_requires=[
          "pytest"
      ],
      zip_safe=False,
      entry_points={},
      setup_requires=[],
      tests_require=["pytest"],)
