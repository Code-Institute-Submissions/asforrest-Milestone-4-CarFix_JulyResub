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


### Python Database Migrations

Before preforming any migrations to the Python database Dry Run's were utilized to make sure that there were no errors first.

![Migrations Dry Run](/media/readme-images/making-migrations-dry-run.png)

Then after making the migrations to check the models are correct then Plan option was used.

![Migrations Dry Run](/media/readme-images/making-migrations-plan.png)


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
1. IDE Update, Crash, and Repair during 23rd Hour
During the final week of this project Gitpod updated there systems which made it uncompatible with the Code Institute template and it's elements. After a failed attempt at fixing the issue and reaching out to tutoring support: the solution was to switch to the new environment while the workspace was still running. 


1. Requiring expanded versions of jQuery
I ran into an interesting issue where I needed to use the $.post function from jQuery in order to complete the project in the same maner as the lesson material. I had used the slim minified version which doesn't contain this. The solution was to load full Query.


1. Spreadsheet > CSV > JSON > Django (The Creative Solution)
I had an issue when creating my database of mechanics. This was made in Apple Pages and exported to CSV. From there this was converted to JSON using the online converter [CSV to JSON](https://csvjson.com/csv2json). 

After getting the data into JSON file I realised that it wasn't possible to import this so I though of a creative solution. I created an extra column for "field" with the value of "{" and then procdeeded to use find and replace to fix the rest of the syntax so that the JSON file would be correctly formatted to be important as a Django Fixture.

![Find and replace](/media/bugs/json-to-django-solution-find-and-replace.png)

1. Duplicate data cleaning after creating filters and speeding up loading times
After creating filters for my mechanics data I realised that I had some duplicate data. Since the mechanics data I used had 1530 rows, removing the duplicate data would leave me with only about 30% of around 500 entries. I've noticed some slow down due to the large number of entries, so removing the extra entries also increases loading times significantly.

![Find and replace](/media/bugs/removing-dubble-data.png)

## Deployment

This project is saved to a [repository on GitHub](https://github.com/asforrest/KATT-App) and as such is open to the public.

This project has also been [published to Heroku](https://katt-app.herokuapp.com/) both for evaluation by Code Institute and so that users can access and use the Web App.

### Requiements for  Deployment to Heroku

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

### Steps For Deployment on Heroku & AWS with GitHub and GitPod

#### Heroku
1. Check that GitHub repisotry is update to date with latest commit.
1. Create a free account on Heroku
1. Create a new app
1. Install Add-on Heroku Postgres
1. Go back to gitpod and install dj_database_url (pip3 install dj_database) and psychopg2-binary (pip3 install psychopg2-binary) to use Postgres
1. Setup new dj_database in settings.py
1. Migrate the database to the new location
1. Load fixtures into the new database
1. Create a superuser
1. Install Gunicorn in gitpop (pip3 install gunicorn)
1. Create procfile
1. Add allowed hosts to settings.py
1. Deploy app by adding and committing changes and connecting to Heroku
1. Login in on the Heroku webportal, connect to GitHub and enable automatic deploys
1. Generate a Django key and add to Heroku
1. Setup hidden key in settings.py
1. Commit - now it's automatically connected to GitHub
1. Click Deploy
1. The App builds and is then available, this app is available via https://asforrest-carfix.herokuapp.com/

#### AWS
1. Sign up for an account.
1. Login and open S3
1. Create a new bucket
1. Allow public access of the bucket
1. Turn on static web hosting
1. On the Permissions tab paste in CORS configuration
1. Create AWS Policy
1. Add ARN and bucket policy
1. Set List Objects to Everyone
1. Create user, group and policy in IAM
1. Go to Gitpod and install boto3 (pip3 install boto3) and django-storages (pip3 install django-storages)
1. Connect Django to S3
1. Add keys to settings
1. Go to Heroku and add AWS keys to config vars
1. Add SECRET_KEY to GitPod
1. Push to GitHub and Heroku is auto deployed
1. Got to Amazon S3
1. Upload Media files
1. Add stripe webhook to point to Heroku




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