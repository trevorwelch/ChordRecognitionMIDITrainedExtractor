import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wuyimingchroma",
    version="0.0.1",
    author="Wu Yiming",
    description="A Yiming Wu and Wei Li chroma extractor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/migperfer/ChordRecognitionMIDITrainedExtractor",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)