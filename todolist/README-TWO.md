# Assignment 6 PBP/PBD

### Asynchronous Programming and Synchronous Programming
Asynchronous is multi-threading and non-blocking, so that operations will run in parallel and it will send multiple requests to the server, in contrast to that, Synchronous is single-thread which means only one operation can run at one time and will also send only one request at a time.

### Event-Driven Programming
Event-driven programming is a paradigm in which programs are executed when new events(clicks, keys), sensor outputs, or message passing from other programs. In this particular program there is a click event listener that listens a button with a certain ID to do a certain function namely `Add Task`

### Implementation of Asynchronous Programming
- Add `<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>` to html header.
- Add `<script>` tag inside your html body.
- Write ajax JQuery syntax inside your script, like `$.ajax()` to POST, DELETE, etc.
- Ajax will listen the event listener you write in script to perform the action you want.
- That action and response/data will be processed asynchronously in the server.
- The data will be shown in the page without needing to refresh.

### Process of Completion
Step by step process:
- Add all necessary scripts in `base.html`
- Add `show_json` in views
- Create a new function called `add` that posts data using AJAX in views
- Connect all new functions in `urls.py`
- Add a GET function in `todolist.html`
- Create the modal with bootstrap
- Add POST function in `todolist.html`
- Add, commit, and push the code onto GitHub
