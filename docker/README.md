# SIR Model Calculator

This project aims to use the [SIR Model](https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology) to simulate
an epidemic outbreak in a closed population. This was originally a coursework question for my [Degree](https://www.open.ac.uk/courses/computing-it/degrees/bsc-computing-it-software-q62-soft)
which I found particularly intriguing, so I figured I'd redo my answer in Python and add some nifty data visualisation to boot.

This docker image represents a containerised version you can just 'plug and go' with. 

## Tags
- `dev` refers to an image that has been built off of a branched piece of work - UNSTABLE
- `qa` refers to work that has been merged into main - POTENTIALLY UNSTABLE
- `\d.\d.\d` version will refer to a specific release - STABLE
  - The last release will also be what `latest` refers to as well

## Getting Started

### Prerequisities


In order to run this container you'll need docker installed.

* [Windows](https://docs.docker.com/windows/started)
* [OS X](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)

### Usage

#### Container Parameters

- Displays help information
```shell
docker run sudoblark/sir-model-calculator -h
```

- Define a basic run
```shell
docker run sudoblark/sir-model-calculator output closed_population initial_infection days transmission_rate recovery_rate
```

- Define output location for csv/matplotlib
```shell
docker run sudoblark/sir-model-calculator output closed_population initial_infection days transmission_rate recovery_rate --outputLocation <location>
```

- Change log level
```shell
docker run sudoblark/sir-model-calculator output closed_population initial_infection days transmission_rate recovery_rate --logLevel <level>
```

- Open shell inside container
```shell
docker run --entrypoint "/bin/bash" sudoblark/sir-model-calculator
```

#### Examples
- Show license info
```shell
docker run sudoblark/sir-model-calculator terminal 150 4 60 0.43 0.18 -l
```

- Output to terminal
```shell
docker run sudoblark/sir-model-calculator terminal 150 4 60 0.43 0.18
```

- Output to terminal with debug output
```shell
docker run sudoblark/sir-model-calculator terminal 150 4 60 0.43 0.18 --logLevel DEBUG
```

- Output to csv file
```shell
docker run sudoblark/sir-model-calculator csv 150 4 60 0.43 0.18 --outputLocation /output/output.csv
```

- Output csv to mounted directory so results are available on host
```shell
docker run -v D:\output:/output sudoblark/sir-model-calculator csv 150 4 60 0.43 0.18 --outputLocation /output/output.csv
```

- Output matplotlib to mounted directory so results are available on host
```shell
docker run -v D:\output:/output sudoblark/sir-model-calculator matplotlib 150 4 60 0.43 0.18 --outputLocation /output/output.png
```

#### Arguments

- `output` determines how to display results
  - `terminal` will just output to the terminal
  - `csv` will output to a csv
  - `matplotlib` will output to a line graph 
- `population` is the size of our closed population
- `initial_infection` is the number of infected individuals on day 0
- `days` is the number of days our simulation should model
- `transmission_rate` is how infectious infected individual ares
- `recovery_rate` is how quickly individuals move into recovered state
- `--outputLocation` defines where to save csv/matplotlib output
- `--logLevel` allows you to set log level for the application

#### Useful File Locations

* `/output` - Recommended location to store output
  
* `/opt/sir_model_calculator` - Root of the application

## Find Us

* [GitHub](https://github.com/Sudoblark/sir_model_calculator)

## Contributing

Please read [the Github readme](https://github.com/Sudoblark/sir_model_calculator) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the 
[tags on this repository](https://github.com/Sudoblark/sir_model_calculator/tags). 

## Authors

* **Sudoblark** - *Initial work* - [Github](https://github.com/Sudoblark)

## License

Distributed under the GNU General Public License. See [LICENSE.txt](https://github.com/Sudoblark/sir_model_calculator/blob/main/LICENSE.txt) for more info.