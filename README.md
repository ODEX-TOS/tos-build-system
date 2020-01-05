[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


Tos build system is designed to work flawlessly with arch based systems.
All you need is this package installed and it will auto install all dependencies.
It is compromised of different subsystems that manages different parts of TOS.
Below you will find most of what you need if you wish to build tos yourself.


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/ODEX-TOS/tos-build-system">
    <img src="https://tos.pbfp.xyz/images/logo.svg" alt="Logo" width="150" height="200">
  </a>

  <h3 align="center">TOS build system</h3>

  <p align="center">
    This is a tool to build repositories, manage images, uploads to a server and manages installation dependencies
    <br />
    <a href="https://github.com/ODEX-TOS/tos-build-system"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/ODEX-TOS/tos-build-system">View Demo</a>
    ·
    <a href="https://github.com/ODEX-TOS/tos-build-system/issues">Report Bug</a>
    ·
    <a href="https://github.com/ODEX-TOS/tos-build-system/issues">Request Feature</a>
  </p>
</p>

## Installation

As described above you only need this package.
eg

```bash
# Install on arch (you need the tos repo)
pacman -Syu tos-build-system

# Or build the software manually
sudo pip install
```


## Usage example

A few motivating and useful examples of how your product can be used. Spice this up with code blocks and potentially more screenshots.

_For more examples and usage, please refer to the [Documentation](https://github.com/ODEX-TOS/tos-build-system)._

## Development setup

To extend this you should only need `python3` and `pacman` installed
If you wish to run unit tests simply do the following.
```sh
python -m unittest discover -s <module>/tests -p "*_test.py"
```

## Release History

* 0.0.1
    * Initial start

## Meta

F0xedb – tom@odex.be

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/F0xedb/tos-build-system](https://github.com/F0xedb/tos-build-system)

## Contributing

1. Fork it (<https://github.com/F0xedb/tos-build-system/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[contributors-shield]: https://img.shields.io/github/contributors/ODEX-TOS/tos-build-system.svg?style=flat-square
[contributors-url]: https://github.com/ODEX-TOS/tos-build-system/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ODEX-TOS/tos-build-system.svg?style=flat-square
[forks-url]: https://github.com/ODEX-TOS/tos-build-system/network/members
[stars-shield]: https://img.shields.io/github/stars/ODEX-TOS/tos-build-system.svg?style=flat-square
[stars-url]: https://github.com/ODEX-TOS/tos-build-system/stargazers
[issues-shield]: https://img.shields.io/github/issues/ODEX-TOS/tos-build-system.svg?style=flat-square
[issues-url]: https://github.com/ODEX-TOS/tos-build-system/issues
[license-shield]: https://img.shields.io/github/license/ODEX-TOS/tos-build-system.svg?style=flat-square
[license-url]: https://github.com/ODEX-TOS/tos-build-system/blob/master/LICENSE.txt
[product-screenshot]: https://tos.odex.be/images/logo.svg
