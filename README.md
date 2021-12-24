[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GNU License][license-shield]][license-url]


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">Deduplicator</h3>

  <p align="center">
    File hasher and deduplicator
    <br />
    <br />
    <a href="https://github.com/HenryBlackie/Deduplicator/issues">Report Bug</a>
    ·
    <a href="https://github.com/HenryBlackie/Deduplicator/issues">Request Feature</a>
  </p>
</p>


<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project

A simple tool for hashing and removing duplicate files from datadumps.

This tool will identify and hash all files within the input directory (recursive). Unique files will then be copied to the output directory. The tool will also attempt to preserve file metadata.

### Built With

* [Python 3.8](https://www.python.org/)

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.


### Prerequisites
Required python packages:
* psutil==5.8.0
* termcolor==1.1.0


### Installation

1. Clone the repo
```sh
git clone https://github.com/HenryBlackie/Deduplicator.git
cd Deduplicator
```
2. [Optional] Create a virtual environment
```sh
python3 -m venv .
source bin/activate
```
3. Install the required packages
```sh
python3 -m pip install -r requirements.txt
```
4. [Optional] Create an input folder and import files. The tool will search recursively and does not respect the file structure when copying the file, so you should run the tool in multiple batches if this is required.
```sh
mkdir input
```


<!-- USAGE EXAMPLES -->
## Usage

* Deduplicate files in directory named 'input'
```sh
python3 hasher.py
```


<!-- ROADMAP -->
## Roadmap

* Filetype/extension filtering
* Directory structure mirroring
* Hash logging
* Output file validation

See the [open issues](https://github.com/HenryBlackie/Deduplicator/issues) for a list of proposed features (and known issues).


<!-- CONTRIBUTING -->
## Contributing

This is an open-source project, any contributions are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/FeatureName`)
3. Commit your Changes (`git commit -m 'Add some FeatureName'`)
4. Push to the Branch (`git push origin feature/FeatureName`)
5. Open a Pull Request


<!-- LICENSE -->
## License

Distributed under the GNU General Public License v3.0 License. See `LICENSE` for more information.


<!-- CONTACT -->
## Contact

Henry Blackie - [@henry_blackie](https://twitter.com/henry_blackie)

Project Link: [https://github.com/HenryBlackie/Deduplicator](https://github.com/HenryBlackie/Deduplicator)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/HenryBlackie/repo.svg?style=flat-square
[contributors-url]: https://github.com/HenryBlackie/Deduplicator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/HenryBlackie/repo.svg?style=flat-square
[forks-url]: https://github.com/HenryBlackie/Deduplicator/network/members
[stars-shield]: https://img.shields.io/github/stars/HenryBlackie/repo.svg?style=flat-square
[stars-url]: https://github.com/HenryBlackie/Deduplicator/stargazers
[issues-shield]: https://img.shields.io/github/issues/HenryBlackie/repo.svg?style=flat-square
[issues-url]: https://github.com/HenryBlackie/Deduplicator/issues
[license-shield]: https://img.shields.io/github/license/HenryBlackie/repo.svg?style=flat-square
[license-url]: https://github.com/HenryBlackie/Deduplicator/blob/master/LICENSE.txt
