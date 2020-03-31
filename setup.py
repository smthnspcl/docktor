from setuptools import setup, find_packages

setup(
    long_description_content_type="text/markdown",
    long_description=open("readme.md", "r").read(),
    name="docktor",
    version="0.42",
    description="starts n tor docker containers with an api",
    author="Pascal Eberlein",
    author_email="pascal@eberlein.io",
    url="https://github.com/smthnspcl/docktor",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
    keywords="docker tor python",
    packages=find_packages(),
    package_dir={'docktor': 'docktor'},
    package_data={
        "data": ["data/*"]
    },
    entry_points={'console_scripts': ['docktor = docktor.__main__:main']},
    install_requires=open("requirements.txt").readlines()
)
