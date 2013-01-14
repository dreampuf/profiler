from setuptools import setup

setup(name='profiler',
      version='0.1',
      description='Python library of profile tools',
      url='https://github.com/dreampuf/profiler',
      author='Huang, Xin',
      author_email='soddyque@gmail.com',
      license='MIT',
      packages=['.'],
      install_requires=['line_profiler', 'memory_profiler', 'objgraph'],
      test_suite='profiler',
      zip_safe=False)
