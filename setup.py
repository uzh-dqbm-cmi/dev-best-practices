from setuptools import setup, find_packages

setup(name='dev_best_practices',
      version='0.0.1',
      description='Develop good python habits',
      url='https://github.com/uzh-dqbm-cmi/dev-best-practices',
      packages=find_packages(),
      python_requires='>=3.7.0',
      install_requires=[
            'pandas',
            # 'plotly',
      ],
      zip_safe=False)
