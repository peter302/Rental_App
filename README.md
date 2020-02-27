### PROJECT NAME
Rentals
### PROJECT AUTHORS
John,Peter,Suad
### DESCRIPTION
This is a application that allow users to find and serch for houses for renting, Thursday Feb 27th 2020.
### FEATURES
* User can log in to application and view available houses.
* A user can search for houses by location.
* A user can update profile.
* Admin can add users and give them paermissions to add houses.
* Admin can delete users
### PREREQUISITES
1. Python3.6 
2. Postgress
3. Django framework
4. Python virtual 
### CLONING & RUNNING
Run the following command on the terminal:

      `https://github.com/johnopana/Rental_App.git`

### CREATE VENV
- To Create a virtual environment run the following command:
         
        `python3.6 -m venv <the name of your virtual>`

- Then activate the virtual with this command:

        `. virtual/bin/activate`       

### INSTALL DEPENDANCIES
nstall the dependancies that will create an environment for the app to run with this command:

                 `pip3 install -r requirements.txt`
      
### CREATE DATABASE
Run:

    ` psql
     CREATE DATABASE <the name of your database>;` 

### RUN MIGRATIONS
```
python3.6 manage.py makemigrations <the name of your App>
python3.6 manage.py migrate
```
## TECHNOLOGIES USED
* Css
* Django
* Postgres
* Python3.6
* JavaScript
* Bootstrap4
### DEPLOYING (LIVE LINK)

### BEHAVIOR DRIVEN DEVELOPMENT (SPECIFICATIONS)
| Behavior            | Input                         | Output                        |
| ------------------- | ----------------------------- | ----------------------------- |
| User visits the application and croll through  | User logs in to use the system | user can view available houses and features of a particular house |
If user has no account, they click on `sign up` | User signs up | User is redirected to the log in page |
|  Homepage loads | Click `profile` | User's profile appears |
| Homepage loads | Click `upload image` icon | User's redirected to a page where they can upload an image |
| Homepage loads | Click `settings` icon | A modal appears where one can change their password or logout |

### CONTACT 
JPS23@gamil.com
### LICENSE 
ermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files, to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


The project is under[MIT license](/blob/master/LICENSE)
Copyright &copy; 2020.All rigths reserved