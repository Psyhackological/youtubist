<p align="center">
  <img width="20%" align="center" src="youtubist.ico" alt="youtubist logo">
</p>
<h1 align="center">Youtubist</h1>

<p align="center">
    Basically fork of yt-dlp python module to my needs. 
    <br>
    You can paste URL or channel link  on the YouTube. 
    <br>
    It will automatically format to special hyperlink format in Todoist [displayed_text](url). 
    <br>
    Then you can copy text from .txt file and then paste it into Todoist.
</p>

<p align="center">
  <a style="text-decoration:none" href="https://github.com/Psyhackological/youtubist/releases">
    <img src="https://img.shields.io/github/v/release/Psyhackological/youtubist?color=FF0000&style=flat-square" alt="Releases">
  </a>
  <a style="text-decoration:none" href="https://choosealicense.com/licenses/gpl-3.0/">
      <img src="https://img.shields.io/badge/License-GPL%20v3-FF0000.svg" alt="GPLv3">
  </a>
  <a style="text-decoration:none" href="https://www.python.org/downloads/release/python-379/">
    <img src="https://img.shields.io/badge/python-3.7+-blue.svg?color=FFFFFF&style=flat-square" alt="Python Version">
  </a>
  <a style="text-decoration:none" href="https://www.codefactor.io/repository/github/psyhackological/youtubist">
    <img src="https://img.shields.io/codefactor/grade/github/Psyhackological/youtubist/main?color=FF0000" alt="CodeFactor">
  </a>
  <a style="text-decoration:none" href="https://github.com/Psyhackological/youtubist/releases">
    <img src="https://img.shields.io/github/downloads/psyhackological/youtubist/total?color=FF0000&style=flat-square" alt="Downloads">
  </a>
</p>

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#features">Features</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#dependencies">Dependencies</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

##  Features
- Saves a lot of time if you like to create Todoist tasks from playlist/channel videos
- Easy and intuitive to use
- yt-dlp is still in development so my repo will never be static

## Installation
Pre-built binaries are available from the [releases](https://github.com/Psyhackological/youtubist/releases/) page. (Windows only)

##  Dependencies
You need only 1 additional modules:
- [yt-dlp](https://pypi.org/project/yt-dlp/)

It can be installed at once by pasting this command into a terminal:
```terminal
pip install yt-dlp
```
If the installation fails due to lack of access rights, try this:
```terminal
pip install --user yt-dlp
```

## Usage
Paste this command into the terminal (at the youtubist folder):
```terminal
python youtubist.py
```

## Contributing
Never have I had one, but I am imperfect human, so I am open for pull requests.

## License
[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-with-text-136x68.png)](https://choosealicense.com/licenses/gpl-3.0/)

Software licensed under the [GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/).