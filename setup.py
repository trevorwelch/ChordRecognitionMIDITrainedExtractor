import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wuyimingchroma",
    version="0.0.2",
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
    package_data={"":["fullcnn_crossentropy_6000.model"]},
    install_requires=['chainer>=4.2.0',
                      'librosa>=0.6',
                      'mir_eval>=0.4',
                      'madmom',
                      'soundfile',
                      'joblib',
                      ],
    include_package_data=True,
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
