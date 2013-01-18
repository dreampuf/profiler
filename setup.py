from setuptools import setup

setup(name='profiler',
      version='0.1',
      description='Python library of profile tools',
      url='https://github.com/dreampuf/profiler',
      author='Huang, Xin',
      author_email='soddyque@gmail.com',
      license='MIT',
      packages=['.'],
      install_requires=['line_profiler==dev', 'memory_profiler==dev', 'objgraph'],
      dependency_links=[
          "https://github.com/dreampuf/lprofiler/tarball/master#egg=line_profiler-dev"
          "https://github.com/dreampuf/memroy_profiler/tarball/master#egg=memory_profiler-dev"
      ],
      test_suite='profiler',
      zip_safe=False)
