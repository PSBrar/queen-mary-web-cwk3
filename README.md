# queen-mary-web-cwk3
Hobbies web app using Vue Django for QM Web coursework

# Build & Run
You can create a conda environment or just install Django and the rest should be able to be automatically grabbed by IntelliJ.

To create the conda environment run this command using the spec file in the conda_spec_env_files folder:

conda create --name myenv --file spec-file.txt

The spec-file2.txt has some more dependcies that may or may not be automatically picked up by that command so if not just go through and add them yourself

After that just do conda activate <ENV_NAME> and then just do python manage.py runserver and thats it
