<div id="top"></div>

<br />
<div align="center">

<h3 align="center">SIR Model Animation</h3>

  <p align="center">
    Program to model an epidemic outbreak, using a basic SIR Model, then visualise in matplotlib
    <br />
    <a href="https://github.com/Sudoblark/SIR_Model_Animation"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Sudoblark/SIR_Model_Animation/issues">Report Bug</a>
    ·
    <a href="https://github.com/Sudoblark/SIR_Model_Animation/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project aims to use the [SIR Model](https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology) to simulate
an epidemic outbreak in a closed population. This was originally a coursework question for my [Degree](https://www.open.ac.uk/courses/computing-it/degrees/bsc-computing-it-software-q62-soft)
which I found particularly intriguing, so I figured I'd redo my answer in Python and add some nifty data visualisation to boot.

Note that instructions in the readme are for setting up a local development environment, whereas releases will contain 
instructions on how to utilise outside of a local development environment.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With
* [matplotlib](https://matplotlib.org/)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

The steps below detail how to get a local version up the program up and running.

### Prerequisites

* Windows
  * [Python 3](https://www.python.org/downloads/windows/)
* Linux
  * [Python 3](https://docs.python-guide.org/starting/install3/linux/)

### Installation

* Windows
    * Clone repo and cd into repo
    ```bash
    git clone https://github.com/Sudoblark/SIR_Model_Animation.git
    cd SIR_Model_Animation
    ```
    * Setup Python venv and activate
    ```bash
    python3 -m venv venv
    venv\Scripts\activate
    ```
    * Install dependencies
    ```bash
    pip3 install -r requirements
    ```

* Linux
    * Clone repo and cd into repo
    ```bash
    git clone https://github.com/Sudoblark/SIR_Model_Animation.git
    cd SIR_Model_Animation
    ```
    * Setup Python venv
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
    * Install dependencies
    ```bash
    pip3 install -r requirements.txt
    ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Now your virtual environment is setup, run help to determine what options are available:

```
(venv) C:\temp\SIR_Model_Animation>python -m main -h
------------------------------------------------
SIR Model Animation Copyright (C) 2022 Sudoblark
Run 'main -h' for more information
------------------------------------------------

usage: main.py [-h] [-l] [--csvFile CSVFILE]
               {csv,matplotlib,terminal} population initialInfection days transmissionRate recoveryRate

positional arguments:
  {csv,matplotlib,terminal}
                        Select output type
  population            Size of closed population
  initialInfection      Infected individuals on day 0
  days                  Number of days our simulation should model
  transmissionRate      How infectious infected individuals are
  recoveryRate          How quickly individuals move into recovered state

optional arguments:
  -h, --help            show this help message and exit
  -l                    Show licensing information
  --csvFile CSVFILE     Full path to CSV file to output to

```

For example, running the below will output a line graph showing SIR data:

```
(venv) C:\temp\SIR_Model_Animation>python -m main matplotlib 150 4 60 0.12 0.18
```
![Example SIR data](images/example_data.png "Example SIR data")



<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the GNU General Public License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Sudoblark - [@linkedin_handle](https://www.linkedin.com/in/benni/)

Project Link: [SIR_Model_Animation](https://github.com/Sudoblark/SIR_Model_Animation)

<p align="right">(<a href="#top">back to top</a>)</p>
