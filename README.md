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

paste the key in the line number three and write True in the line number six.
Save data and close file.

- cd ..
- python3 -m venv .
- source bin/activate
- pip install -r requirement.txt
- python agencia/manage.py makemigrations
- python agencia/manage.py migrate

# Project is ready for run in local

- python agencia/manage.py runserver

# Go to your web browser and write the next link

- http://127.0.0.1:8000/

Platforms

# Firts you need create some buses instances, go to the next link:

- http://127.0.0.1:8000/garage/api/bus/list
in the input Content, you can copy and paste the next examples separately:
  - Example bus 1: {"plate":"AABB11"}
    - click post Button
  - Example bus 2: {"plate":"XYZA22"}
    - click post Button
Now you can back to the main page and click Buses tab and see the list of buses.

You need to repeat this example for Chauffeur, Route and Schedule

Link: http://127.0.0.1:8000/garage/api/chauffeur/list
  - example 1: {"dni":"1111111-1"}
  - example 2: {"dni":"2222222-2"}

Link: http://127.0.0.1:8000/garage/api/route/list
  - example 1:{"name":"Santiago-Rancagua"}
  - example 2:{"name":"Rancagua-Santiago"}

Link: http://127.0.0.1:8000/garage/api/schedule/list
  - example 1:{"origin_date":"2022-05-20 15:00:00", "destination_date":"2022-05-20 20:30:00"}
  - example 2:{"origin_date":"2022-05-21 08:00:00", "destination_date":"2022-05-21 09:30:00"}

You have already generated enough information to make a trip.

Firts you copy and paste the next page:

- http://127.0.0.1:8000/garage/route/list/

assing bus to any route, next you can assing the same way Chauffeur and schedule  to the route.

Finally you can Buy a trip, go to the next page:

- http://127.0.0.1:8000/box_office/ticket/buy
  - select a trip and click in buy button
  - put your dni or the any passenger
  - put you seat number between 1 to 10 
  - click in pay button.


