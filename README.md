<!-- PROJECT LOGO -->

<br />
<div align="center">
  <a href="https://github.com/Sam-Miller_mottmac/power-system-tools">
    <img src="python_logo.png" alt="Logo" width="300" height="300">
  </a>

<h3 align="center">power-system-tools</h3>

  <p align="center">
    <a href="https://github.com/Sam-Miller_mottmac/power-system-tools"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Sam-Miller_mottmac/power-system-tools">View Demo</a>
    ·
    <a href="https://github.com/Sam-Miller_mottmac/power-system-tools">Report Bug</a>
    ·
    <a href="https://github.com/Sam-Miller_mottmac/power-system-tools">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#contact">Contact</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This repository contains Python modules for using the APIs of various power system software suites. 

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

* Samuel Miller: sam.miller@mottmac.com

Use [GitHub Issues](https://github.com/Sam-Miller_mottmac/power-system-tools/issues) to share ideas, feedback, tasks, or spotted bugs in this Repository.
Or get in touch directly with one of the repository contributors.

Don't forget to give the project a :star: !

Project Link: [https://github.com/Sam-Miller_mottmac/power-system-tools](https://github.com/Sam-Miller_mottmac/power-system-tools)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

<!-- Add instructions specific to your project here. -->

1. Prerequisites

   Relevant software:
   - PSSE 
   - PowerFactory 
   - PSCAD (software specific scripts yet to be implemented)
   - ETAP (software specific scripts yet to be implemented)

   It is necessary to sync the 'Documents' folder of the PS ANZ sharepoint to gain access to the modelling project folders. Access to PS ANZ team should be requested to Samuel Miller or Omer Suliman. 


2. Installation instruction:

    - Install [Git](https://git-scm.com/downloads) or [GitHub Desktop](https://desktop.github.com/)


3. Create a local copy

   Download [latest release](https://docs.github.com/en/repositories/releasing-projects-on-github/viewing-your-repositorys-releases-and-tags#viewing-releases), if none available [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) the repository

 ```
    git clone https://github.com/Sam-Miller_mottmac/power-system-tools
 ```

 4. Environment Setup

```
# For pip
> python -m venv .\venv
> venv\Scripts\activate
> pip install -r requirements.txt

Note that the requirements.txt should be installed for each interpreter used with each software. For example, to install the requirements with a 32-bit interpreter used with PSSE, it could look like:

> & "C:\Program Files (x86)\Python37-32\python.exe" -m pip install -r requirements.txt

If Python 3.10 were being used for PowerFatory, the installation could take place with: 

> & "C:\Program Files\Python310\python.exe" -m pip install -r requirements.txt


# For conda
> conda create --name venv --file requirements.txt
> conda activate
```

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- Testing -->
## Testing
No Tests included

## License

Distributed under the MM License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>