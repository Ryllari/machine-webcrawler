# machine-webcrawler
*A web crawler to scrapping machine information data from [Vultr Bare Metal](https://www.vultr.com/products/bare-metal/#pricing) site*


### Setting up
It is recommended to use a virtual environment to run the project (optional).

1.  Inside the project's root folder, install the project dependencies:
    ```
    $ pip install -r requirements.txt
    ```

### Running the project
To execute this project, you need run the ***run.py*** file with at least one of the following arguments:
 
 `-h` or `--help`: show the help message and exit
 
   `--print`: crawler the data and print to screen


 1. If you want crawler the data and print, run:
	```
	$ python run.py --print
	```

### Running tests
To execute the tests, run:
```commandline
python -m unittest -v
```

---
***This project was developed in an environment with Ubuntu 20.04 and Python 3.8.10. But, you can run in any system with Python 3.8.10+***