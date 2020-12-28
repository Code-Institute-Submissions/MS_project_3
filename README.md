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
    - [**How to run this project locally**](#how-to-run-this-project-locally)

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
Card component for the styling of the bird images on the Home page;
Navbar component for responsive navbar link - new or logged-out user has a different display if compared with the logged-in user.
JS Parallax for the styling of the hero image.
JS Collapsable for the styling of Add/Edit sighting
Autocomplete Form for the styling of the Registration form.

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
- 
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea

## Technologies Used

- [JQuery](https://jquery.com)


- HTML5, CSS3, JavaScript, Python programming languages
- [JQuery](https://jquery.com) is used to initialize the Materialize components.
- [Materialize](https://materializecss.com/about.html) front-end framework for responsive websites.
- [Flask]() - Python microframework Flask is used to create this project.
- [Jinja]() - Jinja templating language is used with Flask in the HTML code.
- [Balsamiq]() - Balsamiq is used to create wireframes for the project.
- [PyMongo]() - Python toolkit to work with MongoDB.
- [MongoDB]() - NoSQL database to store data at the backend.
- [Google_Fonts]() - Google fonts Balsamiq Sans and Krona One are used in the project.
- [Git&Github]() - Used for version control.
- [Heroku]() - It is used as a hosting platform to deploy the project.
- [HTML_Formatter]() - Used to format and beautify my code.


## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Code

### Acknowledgements

- I received inspiration for this project from X
