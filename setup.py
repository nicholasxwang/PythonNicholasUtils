from distutils.core import setup
setup(
  name = 'PythonNicholasUtils',         # How you named your package folder (MyLib)
  packages = ['PythonNicholasUtils'],   # Chose the same as "name"
  version = '1.4',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'PythonNicholasUtils a library with all the import Utils in Python.',   # Give a short description about your library
  author = 'Nicholas Wang',                   # Type in your name
  author_email = 'nicholas.x.wang@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/nicholasxwang/PythonNicholasUtils',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/nicholasxwang/PythonNicholasUtils/archive/refs/tags/v_1.4.tar.gz',    # I explain this later on
  keywords = ['UTILS'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          "werkzeug",
          "selenium",
          "requests",
          "schoolopy",
          "bs4",
          "random",
          "time"
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
