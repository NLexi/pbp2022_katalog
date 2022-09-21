# Assignment 2 PBP/PBD

### Diagram
HTTP request -> urls -> (views <-> models) -> HTTP response(html)

### Why virtual environment is needed
because virtual environments create local environments so that each different project can have different dependencies and packages, if you don't have any virtual environments, you can only make one project without breaking system tools or other projects.

### How i implemented it
I followed the instructions on lab 1, by creating virtual environment then changing all necessary files, then changed some names on the catalogue and style the html so that it doesn't look messy.

[Heroku for Assignment 2](https://pbp2022-katalog.herokuapp.com/katalog/)

# Assignment 3 PBP/PBD

### Key Differences
json is used to represent objects, can't be commented, doesn't support namespaces, and doesn't use end tags.
xml is used to describe data items, can be commented, supports namespaces, dynamic, and uses end tags.
html is used to display data and does not carry it, static, limited tags that displays data, and the tags are predefined.

### Importance of Data Delivery
Typically an HTTP request response cycle is the standard data delivery procedure. The browser would request HTML, style, JPG, Javascript, and the last is the data. HTML would display the data and the data would be delivered in the form of XML and JSON. The importance of data delivery comes in when there's so much data on the website, so that it can display it in chunks based on the user's request and lighten the weight on the storage system.

### Process of completion
Step by step process:
- Create a new app named mywatchlist in pbp2022_katalog
- Added mymwatchlist into project django's settings and url
- Created models for mywatchlist and migrate the models
- Make a json file containing all the data and load the data
- Create the HTML file in templates and styled it briefly
- Connect views and models and the html
- Push the code to github and deploy it on heroku
- Download and screenshotted postman accessing mywatchlist
- Edit tests.py and test the server status code
- Write readme for assignment 3 in github

### Postman
![html](https://github.com/NLexi/pbp2022_katalog/blob/main/Images/assg3html.jpg)
![xml](https://github.com/NLexi/pbp2022_katalog/blob/main/Images/assg3xml.jpg)
![json](https://github.com/NLexi/pbp2022_katalog/blob/main/Images/assg3json.jpg)

[Heroku for Assignment 3](https://pbp2022-katalog.herokuapp.com/mywatchlist/html/)
