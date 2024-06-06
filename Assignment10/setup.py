from pathlib import Path
from setuptools import setup, find_packages


def post_install():
    """ Implement post installation routine """
    with open('./requirements.txt') as f:
        install_requires = f.read().splitlines()
    return install_requires


def pre_install():
    """ Implement pre installation routine """
    # read the contents of your README file
    global long_description
    this_directory = Path(__file__).parent
    long_description = (this_directory / "README.md").read_text()


pre_install()


setup(
    name='Iran_cities_info',
    version='0.1.2',
    description='Iran cities Information: python package to represent Iran\'s province and city information.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=["Iran_cities_info"],
    setup_requires=[],
    url='https://github.com/BenyaminZojaji/Iran_cities_info',
    license='',
    author='Benyamin Zojaji',
    author_email='benyamin.zojaji@gmail.com',
    include_package_data=True,
    install_requires=post_install(),
)