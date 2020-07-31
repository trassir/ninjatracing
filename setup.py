import setuptools

setuptools.setup(
    name="ninjatracing",
    description="Convert .ninja_log files to chrome's about:tracing format.",
    version="1.0",
    author="nico",
    url="https://github.com/nico/ninjatracing",
    # py_modules=, not packages=, taken from https://agapow.net/programming/python/setuptools-and-the-single-file/
    py_modules=['ninjatracing'],
    entry_points={
        'console_scripts': [
            'ninjatracing = ninjatracing:main',
        ]
    }
)
