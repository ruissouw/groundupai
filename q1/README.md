# Overall flow
1. Set up boiler plate Flask file
2. Work on the data analytics part using pandas
3. Dockerizing the project once I understood the dependencies

# Tech Stack
1. Flask: Since this is a super lightweight project, I felt Flask was a natural choice though FastAPI is another good choice
2. Pandas: Another obvious choice since I was dealing with CSV files and had to use simple mathematical formulas
3. Docker: As required by the task

# How to test
1. Ensure Docker is installed locally.
2. Run `cd q1` from root folder and then `docker compose up` to run the Flask server.
3. I have included the python script and CSV file provided in the task under the file `test.py` and `M6.csv`. To run the test script, run `python test.py`. 
4. To test another CSV file, simply drop it in the root folder and alter the folder path in `test.py`

# Credits/references used
1. https://flask.palletsprojects.com/
2. https://pandas.pydata.org/
3. https://docs.docker.com/