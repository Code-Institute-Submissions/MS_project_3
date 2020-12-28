<h1 align="center">
  <a href="https://bird-nl-project.herokuapp.com/">Save Birds</a>
</h1>

<img src="/static/images/heroimage.png" alt="Landing Page"/>

<div align="center">
    <h2>Birds population is rapidly descreaing worldwide. 
    We need volunteers' help to provide the number of the birds sightings in different areas.</h2>

[Save Birds - Your Volunteering Organization](https://bird-nl-project.herokuapp.com/)
</div>

<br>

## Table of Contents
1. [**UX**](#ux)
    - [**Project Goals**](#project-goals)
    - [**Visitor goals**](#visitor-goals)
    - [**Site  owner goals**](#site-owner-goals)
    - [**User stories**](#user-stories)
    - [**Design choices**](#design-choices)
    - [**Wireframes**](#wireframes)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)

3. [**Technologies used**](#technologies-used)

4. [**Testing**](#testing)

5. [**Deployment**](#deployment)
    - [**Heroku Deployment**](#heroku-deployment)
    - [**Local Deployment**](#local-deployment)

6. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Code**](#code)
    - [**Acknowledgements**](#acknowledgements)

7. [**Disclaimer**](#disclaimer)


## UX

### Project goals

The main goal of the project is to provide an environment for volunteers to collect the number and locations of their sightings. The target audience of the "Save Birds" is:
- Individuals who would like to contribute to the preservation of the natural environment
- Professionals who have been working on collecting endangered species data but need external support.


### Visitors' goals

Target audience - anyone who is interested in bird watching, wants to understand more about local species and contribute to the preservation of endangered birds by recording locations of their habitat. 

- Clear contribution to the preservation of the natural environment.
- Recognizing endangered birds in the local area.
- Understanding birds' characteristics and visual appearance.
- Understanding why these bird species are endangered.
- Effortless input of the sightings.
- Review of the logged-in sightings.
- Providing additional information to the sightings.

### Site Owner's goals

Target audience - local environmental organizations and ornithological institutions, who want to involve volunteers for educational and supporting purposes.

- Bring awareness about endangered bird species to the public.
- Explain which birds are endangered and why.
- Involve volunteers for collaboration.
- Monitor and leverage the data collected by volunteers.

### User Stories

#### As a first time visitor I want:
1. Understand whats the mission of the website and how I can contribute to it;
2. Get a quick overview of which birds are endangered according to the guidance;
3. If I am interested to learn more about a specific bird, I can click on the "learn more" button to receive additional information on preservation, physical description, and nesting;
4. Jump on top of the list from the bottom;
5. If I would like to collaborate, I can quickly register and provide my input.

#### As a user of this website, I want:
1. Have a quick login option to access my inputs;
2. I want to directly jump to the "add sighting" page as this is my primary use of the website;
3. While filling in the "add sighting" form, I want the form to highlight mandatory or incomplete input by underlining the fields green or red;
4. Quick access to my records "my sightings";
5. To edit my records and see new values right away;
6. To delete a sighting if needed;
7. Receive a prompt if I want to delete a sighting if I clicked on delete by mistake.

#### As a site owner, I want to:
1. Engage the first comers by explaining the mission of the website;
2. Enable users to have a quick registration: on from page or on the registration page;
3. Enable users to have quick and effortless data input on the "add sighting" page;
4. Have a guided data input - to keep the integrity of the data high.
5. Have a data extract in excel format when needed.

### Design Choices

[Materialize](https://materializecss.com/about.html) version 1.0.0. was used in the project, namely:

- Card component for the styling of the bird images on the Home page;
- Navbar component for responsive navbar link - new or logged-out user has a different display if compared with the logged-in user.
- JS Parallax for the styling of the hero image.
- JS Collapsable for the styling of Add/Edit sighting
- Autocomplete Form for the styling of the Registration form.

**Fonts**
'Open Sans' sans-serif font was used as it's an easily readable font that matches the team of the website.

**Icons**
Feater icon was used for the navigation to home page [Font Awesome](https://fontawesome.com/icons/feather)

**Colors**
[Materialize](https://materializecss.com/color.html) teal-darken pallet was used for styling of the website and contrasting orange darken-4 from Materialize for the styling of the "jump on the top feature".

### Wireframes
 


## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
1. **Navigation Bar** displays pages based on the status of the user: if the user is registered and logged-in - "My Sightings" & "Add Sightings" are visible to this user; if its a new user or a logged-out user - "Register" and "Log In" are visible to this user.
2. **Endangered Birds list** every user can see a summary list of all birds on a Home page. If a user wants to learn more about a specific bird a feature "Learn More" is available. With a click on "Learn More" the user can read detailed information about a bird.
3. **Top** - is a small button on the right side of the screen that allows the user to jump on the top of the page.
4. **Register** - User can easily register as the signup form is very simple. The signup form has two fields username and password. The username requires input min 3 characters, the password requires input min 6 characters. While creating a new account, the user will be notified if the chosen username already exists. 
5. **Login** - If a username or/and password does not match user will be notified that the password and/or username are incorrect.
6. **Flash Messages** - To certify users' actions various flash messages were implemented: on the adding of a new sighting, on editing the sighting, on deleting the sighting; on registration and log in. 
7. **Logout** - ends running session and return to the login page.
8. **My Sightings** - allows a user to view the details of the recorded sighting; no other users' inputs are displayed on this page.
9. **Add Sighting** - allows creating a record of the sighting: name from the droplist, date from the date picker, the location from the droplist, and input free-text comments. The user is kept on the same page after a new sighting is added.
9. **Edit/Delete Sighting** - user can edit a sighting by changing input values in the form. If the user wants to delete a sighting, a question will appear if the action is correct and the user wants to delete the sighting.
10. **Cancel** - is displayed on the Edit page and allows a user to go back to the "My Sightings" page. 

### Features Left to Implement
- Another feature idea

## Technologies Used

- [JQuery](https://jquery.com) for enabling Materialize responsive elements.
- HTML5, CSS3, JavaScript, Python programming languages.
- [JQuery](https://jquery.com) is used to initialize the Materialize components.
- [Materialize](https://materializecss.com/about.html) front-end framework for responsive websites.
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Python microframework Flask is used to create this project.
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) - Jinja templating language is used with Flask in the HTML code.
- [Balsamiq](https://balsamiq.com/) - Balsamiq is used to create wireframes for the project.
- [PyMongo](https://pymongo.readthedocs.io/en/stable/) - Python toolkit to work with MongoDB.
- [MongoDB](https://www.mongodb.com/2) - NoSQL database to store data at the backend.
- [Google_Fonts](https://fonts.google.com/) - Google fonts Balsamiq Sans and Krona One are used in the project.
- [Git&Github](https://github.com/) - Used for version control.
- [Heroku](https://www.heroku.com/#) - It is used as a hosting platform to deploy the project.
- [HTML_Formatter](https://webformatter.com/html) - Used to format and beautify my code.


## Testing

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.


## Deployment

### Local Deployment

1. Go to Recipebook Github Repository
2. Click on Code beside Gitpod.
3. A drop-down menu opens, then click on Download Zip
4. Unzip the downloaded zip file.
5. Open app.py file and install requirements.txt by running command pip3 install -r requirements.txt.
6. Create a database in MongoDB following this structure - ADD PDF
7. Create env.py file and add MONGO_URI and SECRET_KEY.
8. Now run the app.py by running code python3 app.py

### Heroku Deployment

[Save Birds live page](http://bird-nl-project.herokuapp.com/)
[Save Birds Github Repository](Elena-Pakhmurskaia/MS_project_3)

1. Login to your Heroku account.
2. Click on New at the right top corner and click on Create new app.
3. Choose App name and a region. Then click on Create app.
4. Go to the terminal window and create requirements.txt by running the command pip3 freeze --local > requirements.txt
5. Then create Procfile by running the command echo web: python app.py > Procfile Remember P is capital
6. Add these files to the staging area by running the command git add requirements.txt & git add Procfile.
7. Then commit these files respectively by running command git commit -m "Added requirements.txt & git commit -m "Added Procfile.
8. Then push these files to GitHub by running the command git push
9. Go back to Heroku to your App and click on the Deploy tab.
10. Next, go to Deployment Method and click on Github Connect to Github.
11. Next, make sure your Github Profile is displayed and add your repository name and click on Search.
12. Once it finds your repository then click on Connect.
13. Now go to Settings at the top. Then click on Reveal Config Vars.
14. In Config Vars add IP with value 0.0.0.0 then add PORT as 5000 then add SECRET_KEY then add MONGO_URI and then add MONGO_DBNAME which is the name of the database.
15. Now go back to the Deploy tab and click on Enable Automatic Deploys.
16. Now click on Deploy Branch
17. It will take a minute and display a message that Your app was successfully deployed.
18. Click on View to launch your deployed app.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Code

### Acknowledgements

- I received inspiration for this project from X
