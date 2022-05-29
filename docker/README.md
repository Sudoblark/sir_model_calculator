# sir-model-calculator

Dockerised version of [sir_model_calculator](https://github.com/Sudoblark/sir_model_calculator), a Python program
to model an epidemic outbreak within a closed population, using a basic SIR Model, offering multiple output types. 
## Getting Started

These instructions will cover usage information and for the docker container 

### Prerequisities


In order to run this container you'll need docker installed.

* [Windows](https://docs.docker.com/windows/started)
* [OS X](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)

### Usage

#### Container Parameters

List the different parameters available to your container

- To get help information
```shell
docker run sudoblark/sir-model-calculator -h
```

- Example terminal output

```shell
docker run sudoblark/sir-model-calculator terminal 150 4 60 0.12 0.18
```

- Example CSV output
```
docker run -v D:\Github\SIR_Model_Calculator\output:/output sudoblark/sir-model-calculator terminal 150 4 60 0.12 0.18
```

- Example matplotlib output TODO

#### Useful File Locations TODO

* `/opt/sir_model_calculator`

Home of the application, and thus place where outputted is stored unless relative/absolute path given

* `/output`

Recommended location to output csv/matplotlib data to using volume mounts.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the 
[tags on this repository](https://github.com/Sudoblark/sir_model_calculator/tags). 

## License

See the [Github repo](https://github.com/Sudoblark/sir_model_calculator) for licensing information.