from setuptools import setup, find_packages

setup(
    name='gifresizer',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'Pillow>=8.0.0',
    ],
    entry_points={
        'console_scripts': [
            'gif-resizer=gif_resizer.__main__:main',
        ],
    },
    author='Your Name',
    description='A command-line tool for resizing GIFs',
    url='https://github.com/yourusername/gifresizer',  # Replace with your GitHub URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
