# Full Stack Frameworks Milestone Project: CarFixPro

This project has been [deployed to GitHub Pages](https://asforrest.github.io/) and the source code is available in a [repository on GitHub](https://github.com/asforrest/milestone-2-budgetcalc)

This is a web app created for the 2nd Milestone Project for [Code Institute course: Full Stack Development](https://codeinstitute.net/full-stack-software-development-diploma/).

This web app will make use of technologies covered in the course up to this point including HTML, CSS, and JavaScript (including JQuery and connecting with APIs) in order to demonstrate an understanding of these technologies.

This web app aims to solve a real-world problem by assisting users with their financial planning.

## UX (User Experience)


### User Stories


### Wireframes


### Colors


### Fonts
The font-family used for this website comes from Google Fonts and is a sans-serif font: 'Montserrat'. This font is professional and playful and therefor suits the goals of this project.

### Framework


## Methodolgy

### Datbase data
The information obtained for the mechanics database was adapted frmo a dataset from Kaggle. After finding a dataset with 4 column, I could use 3 of them to stand in for fields needed in my data model.

This is how I will use the fields:

Name of Celebrity = Name of mechanic
Pay (USD millions) = (unused)
Year of the pay = Year Since a Member of the Platform
Category of celebrities fame = Specialty (This will be achieved by using a find-and-repalce on the variable used in the data to suit my own categries)



The creator of this web app, Alexander, found it easy to put himself in the shoes of potential user due to using the product himself. 

Alexander has a background in video production which gives him a unique perspective when trying to look at a problem from multiple viewpoints.

The methodology of this project will be based on one core principals during development:

- #### The principle of always delivering a [Potentially Shippable Product](https://less.works/less/framework/potentially-shippable-product-increment)
    1. This means that the product is always working after a coding session, albeit in a basic form.
    1. The product could potentially be submitted at any time.
    1. Constantly having a working product gives more room for refinement.

## Process
When taking the methodology into account the following process has been created:
- #### Planning

- #### Creating basic functionality
 
- #### Creating basic user interface and structure
  
- #### Evaluation
   
- #### Repeat Where Needed


## Features
### Existing Features
1. 

### Features Left To implement
1. 


## Technologies Used

### Languages Used
-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
-   [Python3](http://https://en.wikipedia.org/wiki/Python_(programming_language))
-   [Jinja](https://en.wikipedia.org/wiki/Jinja_(template_engines))

### Frameworks, Libraries & Programs Used

1. [DJango Frameworks:](https://.com/)
    - Django was .
1. [Python3:](https://.com/)
    - Python3 was .
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [GitPod:](https://gitpod.io/)
    - GitPod was used for the bulk of development and as a local server for testing.
1. [Adobe Comp:](https//:www.)
    - Adobe Comp was .
1. [django-allauth](https://.com/)
    - Open source secure .
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
1. [Kaggle:](https://www.kaggle.com/)
    - Kaggle has used to get preloaded data to stand in for mechanic data.



*ADD WHEN NEEDED*
1. [Materialize:](https://materializecss.com/)
    - Materialize was used to assist with the responsiveness and styling of the website.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Titillium Web' font into the style.css file which is used on all pages throughout the project.
1. [jQuery:](https://jquery.com/)
    - jQuery came with Bootstrap to make the modals work properly, as well as simplifies DOM manipulation.
1. [StackOverflow](https://stackoverflow.com/)
    - Stack Overflow was used as a reference and to ask questions about issues that were difficult to code.
1. [Photoshop:](https://www.adobe.com/ie/products/photoshop.html)
    - Photoshop was used for resizing images and editing photos for the website.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes](https://github.com/) during the design process.
1. [Heroku](https://www.heroku.com/)
    - Heroku is a web app deployment environment that also supports Python.
1. [MongoDB](https://www.mongodb.com/)
    - MongoDB is non relational database software.


## Testing

### Testing Methodology


### Code Validation

#### CSS Validation


#### HTML Validation


#### JavaScript Validation


#### Python Validation


### Interesting and Ongoing Bugs
1. Spreadsheet > CSV > JSON > Django (The Creative Solution)
I had an issue when creating my database of mechanics. This was made in Apple Pages and exported to CSV. From there this was converted to JSON using the online converter [CSV to JSON](https://csvjson.com/csv2json). 

After getting the data into JSON file I realised that it wasn't possible to import this so I though of a creative solution. I created an extra column for "field" with the value of "{" and then procdeeded to use find and replace to fix the rest of the syntax so that the JSON file would be correctly formatted to be important as a Django Fixture.

![Find and replace](/media/bugs/json-to-django-solution-find-and-replace.png)

## Deployment

This project is saved to a [repository on GitHub](https://github.com/asforrest/KATT-App) and as such is open to the public.

This project has also been [published to Heroku](https://katt-app.herokuapp.com/) both for evaluation by Code Institute and so that users can access and use the Web App.

### Requiements for Automatic Deployment to Heroku

1. GitHub account
1. Mongo DB Account
1. Heroku account
1. Heroku Config Vars must be set to the same value as env.py
1. env.py - to run locally, including:
    1. IP
    1. PORT
    1. SECRET_KEY
    1. MONGO_URI
    1. MONGO_DB

### Steps For Deployment on Heroku

1.  Check that GitHub repisotry is update to date with latest commit.
1.  Create a free account on Heroku
1.  Go to Settings for the app and add the configuration variables from env.py, these are the security keys and not shared via Github.
1.  Link GitHub and Heroku via the options under delpoyment in the Heroku web app.
1.  Click Deploy
1.  The App builds and is then available, this app is available via https://katt-app.herokuapp.com/

### Running The Code Locally

If you wish to download a copy of the code in order to run the code locally, this is also possible. To do this go to the [KATT repository on GitHub](https://github.com/asforrest/KATT-App) click on 'Code' in the top right and select the method you want to use to download and run the code locally.

### Running The Code Online In Your Own Environment

If you wish to look at or work on the code in an online IDE, then it's recommended to use GitPod. If your using Google Chrome and you install the [Google Chrome GitPod extension](https://chrome.google.com/webstore/detail/gitpod-dev-environments-i/dodmmooeoklaejobgleioelladacbeki?hl=en) then you will see green 'Gitpod' button above [the repository](https://github.com/Code-Institute-Solutions/readme-template) and this will load the code into your own Gitpod environment.

## Contact

If you have any questions about this project or updates then you can contact the developer [Alexander Forrest via his GitHub user profile](https://github.com/asforrest) or alternatively you can send an email to [mailto](mailto:asforrest@icloud.com).

## Credits

The following is an overview of credits for the different people and sources used.

### Content / Sources

The following were done in conjunction with the code institute lessons:
1. Installation and setup of django-allauth
1. 


All sources used have been documented throughout the code in the website through the use of comments. The structure of these comment starts with an explanation of what has been adapted for this project and then the source is given.

The main source for this project was the mini-project from the code institute. This project deals with creating a Task Manager app. The data model is similar to the data model for KATT and was therefore used to create the main structure after an design was decided upon.

The README.md was constructed with elements from the original template provided by Code Instiute and some elements which are still true for this project have been copied from the README.md of Milestone 2 project also created by Alexander Forrest.

### Media

The image used on the homepage is an embedded image hosted on Giphy. This is attributed.

### Personal Acknowledgements

I would like to thank:
- My mentor Jonathan for his patience, knowledge, experience and support.
- Kevin, Michael, and all the other tutors at Code Institute, who took the time to check my workspace, my project and lead me towards the answers I was looking for without just giving me the answers.
- My wife, Alba, for her patience and for taking care of our newborn baby, Zoë, while finishing up this project.
- Code Institute Student Care for checking in with me, keeping me motivated, and being understanding about the fact that becoming a new father meant that my priorities were split between my studies, work and childcare duties.