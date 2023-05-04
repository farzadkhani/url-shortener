# url-shortener
create url shortener and redirect to long url with soft delete system in django framework and bootstrap 5

## attentions
this project is base on python 3.8


## run project
1. clone project
2. go to src directory
3. in src direcotry open command line
4. in comman line:
	1. install pip by this command: sudo apt install python3-pip
	2. install virtualenv by this command: pip install virtualenv
	3. create virtualenv base on python 3.8 by this command: pip install virtualenv --python=python3.8 venv
	4. activate virtualenv by this command: source venv/bin/activate
	5. install requirements by this command: pip install -r requirements.txt
5. go to core directory
6. create local_settings.py file
7. in local_settings.py file define:
	1. BASE_DIR
	2. SECRET_KEY
	3. DEBUG
	4. ALLOWED_HOSTS
8. migrate datebase in src directory:
	1. python manage.py makemigrations
	2. python manage.py migrate
9. run project in src directory with this command: python manage.py runserver
