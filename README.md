# agencia_de_buses
Prueba técnica de destacame

# For run the project, you need write then the next in yours terminal:

- mkdir test   
- cd test/
- git clone https://github.com/elPintozo/agencia_de_buses.git
- cd agencia_de_buses/agencia/
- cp .env_example .env

copy the key generate with the next command

- openssl rand -base64 32 
- nano .env
- 
paste the key in the line number three and write True in the line number six.
Save data and close file.

- cd ..
- python3 -m venv .
- source bin/activate
- pip install -r requirement.txt
- python agencia/manage.py makemigrations
- python agencia/manage.py migrate

Project is ready for run in local

- python agencia/manage.py runserver

Go to your web browser and write the next link

- http://127.0.0.1:8000/
