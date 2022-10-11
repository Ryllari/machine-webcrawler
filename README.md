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

`--save_json`: crawler the data and save the results into json file

`--save_csv`: crawler the data and save the results into csv file

1. If you want crawler the data and print, run:
	```
	$ python run.py --print
	```

2. If you want crawler the data and save into json file, run:
	```
	$ python run.py --save_json
	```

3. If you want crawler the data and save into csv file, run:
	```
	$ python run.py --save_csv
	```

**Note: You can use two or more arguments together**
1. If you want crawler the data, print and save into json file, run:
	```
	$ python run.py --print --save_json
	```

2. If you want crawler the data, print and save into csv file, run:
	```
	$ python run.py --print --save_csv
	```

3. If you want crawler the data, print, save into json file and save into csv file, run:
	```
	$ python run.py --print --save_json --save_csv
	```

4. If you want crawler the data, save into json file and save into csv file, run:
	```
	$ python run.py --save_json --save_csv
	```

### Running tests
To execute the tests, run:
```commandline
python -m unittest -v
```

---
***This project was developed in an environment with Ubuntu 20.04 and Python 3.8.10. But, you can run in any system with Python 3.8.10+***