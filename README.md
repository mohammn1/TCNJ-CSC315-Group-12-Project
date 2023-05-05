#CAB Project 12 Readme/Installation Guide

## Purpose of Project
The purpose of this project is to combine lots of data provided by Sustainable Jersey and combine it in interesting ways to view the effectiveness of various energy programs across the municipalities in New Jersey.

## Installation and Usage

All the necessary set up and updates are contained in the .sh script below, so all the user must do is run the following command to set up everything necessary.
```
$> sh CreateCAB12_db.sh
```
Note that this may take a minute, so please be patient after running the command. You will also need your sudo password for some of the commands to run, and you will have to agree to installing certain updates as the system asks of you.

Now that the database is populated, the user can access the web GUI by first running the command:
```
flask run
```
Now, while that server is up, enter the following link into your web browser's url search:

http://127.0.0.1:5000

Note that you can also access this link from the output in the terminal.

This should bring you to a web page that looks like this:
![image](https://user-images.githubusercontent.com/123781077/234079548-2ca43cbc-74b7-43ff-b039-7702e8618a10.png)

Here, the user can make a variety of queries. For example, by entering a municipality's index number into the first field, you will receive the following result (here Ewing Township with the municipality index of 141 is being used):
![image](https://user-images.githubusercontent.com/123781077/234080190-fed185b6-89eb-46b9-bdfa-3617c143f5ff.png)

The user can also press the second "Submit" button to bring up a table that compares each municipality's greenhouse gas emissions to their number of completed energy efficiency programs:
![image](https://user-images.githubusercontent.com/123781077/234080591-2bab8fa8-90d3-4651-a363-515821efae2f.png)

This program also allows the user to see a municipality's median household income and population and how it relates to the number of energy efficiency programs in the municipality. Here the user can enter the municipality index of their desired municipality to bring up the following:
![image](https://user-images.githubusercontent.com/123781077/235371233-d17bcaba-5a61-4c8a-bcbf-31e33daba92e.png)

There is also another feature where the user can see the median household income and population of a municipality in relation to the municipality's electricity usage, and greenhouse gas emissions as such:
![image](https://user-images.githubusercontent.com/123781077/235371426-f9b6139a-0aa4-4929-a073-c694972bec68.png)


Also if the user is curious about a particular municipality's index, they can search for that municipality in the next input field. In this example the input "princeton" is being searched:
![image](https://user-images.githubusercontent.com/123781077/234080892-8aa28d5a-f20e-494f-97ce-6365dc22455c.png)

Lastly, there is an input field where users who are familiar with SQL can enter any SQL commands they desire (in this example, the input is "SELECT * FROM municipality_code;"):
![image](https://user-images.githubusercontent.com/123781077/234081454-7f646197-620f-4bec-99f8-4dc41f011655.png)

To shut off the server when you are done, go back into the terminal and press CTRL+C to shutdown the server.


P.S. Make sure to also run the following commands explained here to ensure Python, Flask, and Psycopg2 are installed:
https://github.com/jdegood/flask7dbs/blob/main/README.md


-------------------------------------------------------------------------------------------------------------------------------------------------



[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-8d59dc4de5201274e310e4c54b9627a8934c3b88527886e3b421487c677d23eb.svg)](https://classroom.github.com/a/-Nv0cKFk)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10762672&assignment_repo_type=AssignmentRepo)
