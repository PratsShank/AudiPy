from setuptools import setup, find_packages, Extension
import pybind11

#This is where the cpp files will go and the format of how it would be included
'''
ext_modules = [
    Extension(
        "AudioFileCpp",  # Name of the compiled C++ module
        [
            "src/audiofile.cpp",
            "src/audio_processing.cpp",
            "src/audio_utils.cpp"
            
        ],  # List all C++ source files here
        include_dirs=[pybind11.get_include()],  # Include pybind11 headers
        language="c++",
        extra_compile_args=["-std=c++11"],  # Ensure C++11+ support
    ),
]
'''
setup(
    name='AudioFile',
    version='0.1',
    description='A simple audio file reader',
    long_description='A simple audio file reader',
    author='Nick Stephens, Group 10 hackMT 2025',
    author_email='robert.nicholas.stephens@gmail.com',
    url='https://github.com/JustinEugene-CS/AudioFile',
    packages=find_packages(),
    install_requires=[
        'numpy'
                      ],
    # python_requires='>=3.6',
)


