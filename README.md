# Full Stack Frameworks Milestone Project: CarFixPro

This project has been [deployed to GitHub Pages](https://asforrest.github.io/) and the source code is available in a [repository on GitHub](https://github.com/asforrest/milestone-2-budgetcalc)

This is a web app created for the 2nd Milestone Project for [Code Institute course: Full Stack Development](https://codeinstitute.net/full-stack-software-development-diploma/).

This web app will make use of technologies covered in the course up to this point including HTML, CSS, and JavaScript (including JQuery and connecting with APIs) in order to demonstrate an understanding of these technologies.

This web app aims to solve a real-world problem by assisting users with their financial planning.

## UX (User Experience)

### User Stories
![CarFix User Stories](/media/readme-images/CarFix-UserStories.png "CarFix User Stories")

### Wireframes
The following are wireframes for the 2 main streams on the site. Purchasing a subscription and hiring a mechanic.

![Wireframes Subscriptions](/media/readme-images/Wireframes-Subscriptions.png "Wireframes Subscriptions")
![Wireframes Mechanics](/media/readme-images/Wireframes-Mechanics.png "Wireframes Mechanics")

### Colors
The colors chosen for this project are a combination of colors that compliment each other. The starting colors are the colors used as standard in Bootstrap and the Botique Ado project.

These have been supplemented with a color palette found on [Visme](https://visme.co/blog/website-color-schemes/). Number 23, the Clean and Modern look perfectly complements the existing colors.

![Color-Palette](/media/readme-images/Color-Palette.png "Color-Palette")


### Fonts
The font-family used for this website comes from Google Fonts and is a sans-serif font: 'Source Sans Pro'. This font is professional font and fits well.

### Framework
The Frameworks chosen for this project are:

1. Django - for the database and webapp structure
1. Boostrap - for the design elements
1. Code Institutes' Botique Ado Project - this was used for the basic stucture and as inspiration for the backbone and form of the site.

## Methodolgy

This final section of the Full Stack Development course at the Code Institute covers a lot of different aspects. From database management, webstore logic, defensive programming, and also builds upon all of the materials learnt during previous sections.

Therefore when planning for this project a clear decision was made to use the Botique Ado's structure as a basis for the project and use the lesson materials as inspiration in which to build my own ideas and data models.

An approach was taken where by the Botique Ado project was essentially split into 2 clear data streams. In this way an interesting project can be made and I am able to demonstrate my abiliy to take code, manipulate it and build upon it.

The main 2 data streams are:

1. Purchasing Credits - this is done through the purchase of subscriptions
1. Spending Credits - this is done through the hiring of mechanics

Spliting these out were challenging, but each challenge asked for creative solutions due to both the wealth of information provided in the Botique Ado project, as well as that being it's limitations as the project was originally built to function a standard webshop without any exra complications created once a credits variable is introduced.s

### Datbase data
The information obtained for the mechanics database was adapted frmo a dataset from Kaggle. After finding a dataset with 4 columns, I could use 3 of them to stand in for fields needed in my data model. Also by using a Find-and-Replace on the field for "Catefory of celebritites fame" and replacing the variables wih Car brands, I was able to generate a random set of data which would fit my purposes.

Data Source: https://www.kaggle.com/slayomer/forbes-celebrity-100-since-2005

The original fields and my interpretation:

Name of Celebrity = Name of mechanic
Pay (USD millions) = (unused)
Year of the pay = Year since a mechanic at CarFix
Category of celebrities fame = Brand (this will be changed with Find-and-Replace)


### Python Database Migrations

Before preforming any migrations to the Python database Dry Run's were utilized to make sure that there were no errors first.

![Migrations Dry Run](/media/readme-images/making-migrations-dry-run.png)

Then after making the migrations to check the models are correct then Plan option was used.

![Migrations Dry Run](/media/readme-images/making-migrations-plan.png)

## Process
When taking the methodology into account the following process has been created:
- #### Planning
    1. Brainstorming sessions about minimum required core elements.
    1. Brainstorming sessions about stretch goals and the future of the web app.
    1. Contact with the Code Institute appointed mentor for guidance and real world experience.
    1. Discussing the project with friends and family to get input.
    1. Drawing out the structure on paper and creating wireframes to server as a guideline for responsive development.

- #### Creating basic functionality
    1. The main focus of this project was getting the credits system to work. Other systems such as mechanics and clients connecting are ideas for future development.
    1. The goal here is to setup the project in a way that can be expanded on in multiple directions, whether that is creating more products, offering different types of products, or introducting more automation.
  
- #### Evaluation
    1. More brainstorming about potential user interactivity elements.
    1. More brainstorming about potential feature and functions, such as incorporating new potential API elements that benefit the product.
    1. Discussion with the Code Institute appointed mentor to see what areas need improvement.
   
- #### Stick to the basics, plan for the future
    1. Like in the planning phase, due to limited time for this first version of the webapp it's important to add good potential ideas to a backlog during the development process. This is in order to get all core functionality working correctly before expanding on exisitng ideas.
    1. These design principals also fall neatly into the concept of always delivering a [Potentially Shippable Product](https://less.works/less/framework/potentially-shippable-product-increment), a design element that has been at the core of all my Milestone Pojects at the Code Institute.


## Features
### Existing Features that have been Implimentented
1. Purchase a subscription - essentially a product with either 1 or 3 credits attatched to it.
1. Update the user profile with the new number of credits.
1. Let the user hire a mechanic and spend credits to do so.
1. The user can access and edit their personal information.
1. The user can see their credits balance.

### Features Left To implement
1. The user can schedule the appointment with the mechanic directly on the website.
1. The user can see their appintments on their account page.
1. The user can access different options based on their subscription tier, basic or pro (the basic bollean functionality is already built into the profile model).


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
    - Kaggle was used to get preloaded data to stand in for mechanic data.
1. [Gmail](https://www.gmail.com)
    - Gmail was used as the email server.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Titillium Web' font into the style.css file which is used on all pages throughout the project.
1. [jQuery:](https://jquery.com/)
    - jQuery came with Bootstrap to make the modals work properly, as well as simplifies DOM manipulation.
1. [Photoshop:](https://www.adobe.com/ie/products/photoshop.html)
    - Photoshop was used for resizing images and editing photos for the website.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes](https://github.com/) during the design process.
1. [Heroku](https://www.heroku.com/)
    - Heroku is a web app deployment environment that also supports Python.



## Testing

### Testing Methodology
The testing has been done manually and has been aan ongoing process throughout the project.

This was done by hosting a server on GitPod with a live version of the site running at all times while working on the site. When changes were made, these were tested straight away in order to keep the app working correctly.

Testing consisted of taking each user story and running through them once there was a sense of them being completed, or near completetion.

All these steps were done as both a user who was not logged in as a user who was logged in. This is due to a user only being able to make a purchase and update their credits total when they are logged in. Therefore users are forced and triggered to login/signup in mulpiple places, and all these places need to be checked for errors.

Testing steps:
1. Clicking all the available links and jumping back and forth in an attempt to break the links.
2. Random site navigation in an attempt to break the many hide/show elements, which revealed many bugs that were then fixed.
3. Google Chrome's Inspector was used with Console open as to catch any errors with pages or elements loading.
4. Friends and family have been asked to try making a subscription purchase on the website, as well as hire a mechanic, on multiple occasions throughout the development process, this was also beneficial with seeing how another use would used the site.
5. Since the App was built using the Google Chrome browser, which tends to cache information and often fails to update after changes, the page was constantly force-reloaded using the keyboard shortcut CMD/CTRL + Shift + R **before, during and after** changes were carried out.
6. Within Google Chrome's Inspector the mobile view emulation mode was used to test every page, link, button and input with the following emulators:
    -   iPhone X
    -   iPhone 7 Plus
    -   iPhone 7
    -   iPhone 5
    -   iPad
    -   Moto G4
7. Testing was also done in multiple browsers:
    -   Google Chrome
    -   Google Chrome Mobile
    -   Google Chrome Tablet
    -   Apple Safari
    -   Apple Safari Mobile
    -   Apple Safari Tablet
    -   Mozilla Firefox
    -   Mozilla Firefox Mobile
    -   Mozilla Firefox Tablet


### Code Validation

#### CSS Validation


#### HTML Validation


#### JavaScript Validation


#### Python Validation


### Interesting and Ongoing Bugs
1. IDE Update, Crash, and Repair during 23rd Hour - 1st round
During the final week of this project Gitpod updated there systems which made it uncompatible with the Code Institute template and it's elements. After a failed attempt at fixing the issue and reaching out to tutoring support: the solution was to switch to the new environment while the workspace was still running.

This however set development back 2 days. To compound this issue my wife was ill and due to the circumstances I was given another 10 days to finish the project without a penalty.


1. Requiring expanded versions of jQuery
I ran into an interesting issue where I needed to use the $.post function from jQuery in order to complete the project in the same maner as the contained in the lesson material. However dude to using a slim minified version of the CDN, this doesn't contain this that function. 

The solution was to edit the CDN I was targeting and load the full minified version of jQuery.


1. Spreadsheet > CSV > JSON > Django (Creative Solution)
I had an issue when creating the database of mechanics. This was made in Apple Pages and exported to CSV. From there this was converted to JSON using the online converter [CSV to JSON](https://csvjson.com/csv2json). 

After getting the data into JSON file I realised that it wasn't possible to import it so I though of a creative solution. I created an extra column for "fields" with the value of "{" and then procdeeded to use find and replace to fix the rest of the syntax and add the closing "}" at the end of each statement so that the JSON file would be correctly formatted to be important as a Django Fixture.

![Find and replace](/media/bugs/json-to-django-solution-find-and-replace.png)

1. Duplicate data cleaning after creating filters and speeding up loading times
After creating filters for my mechanics data I realised that I had some duplicate data. Since the mechanics data I used had 1530 rows, removing the duplicate data would leave me with only about 30% of around 500 entries.

I also noticed the database was slow with such a large number of entries, so removing the extra entries also increases loading times significantly.

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

#### How to run the code locally using GitPod

If you wish to look at or work on the code in an online IDE, then it's recommended to use GitPod. If your using Google Chrome and you install the [Google Chrome GitPod extension](https://chrome.google.com/webstore/detail/gitpod-dev-environments-i/dodmmooeoklaejobgleioelladacbeki?hl=en) then you will see green 'Gitpod' button above [the repository](https://github.com/Code-Institute-Solutions/readme-template) and this will load the code into your own Gitpod environment.

Once you've obtained the workspace, follow these steps:

1. Open the new workspace
1. Install the required programs by installing the apps located in "requirements.txt" do this in the commandline with: pip3 install -r requirements.txt
1. Migrate the modules to the database, you can do this in the command line with: python3 manage.py migrate
1. Import all the required data to fill the databases, make sure to use the correct order due to data hierarchy:
    - python3 manage.py loaddata brands
    - python3 manage.py loaddata mechanics
    - python3 manage.py loaddata categories
    - python3 manage.py loaddata subscriptions
1. Create a superuser if you want to access the database information with: python3 manage.py createsuperuser
1. run the server with: python3 manage.py runserver

## Contact

If you have any questions about this project or updates then you can contact the developer [Alexander Forrest via his GitHub user profile](https://github.com/asforrest) or alternatively you can send an email to [mailto](mailto:asforrest@icloud.com).

## Content / Sources
The main credits need to be given to the Code Institute for putting together the comprehensive Botique Ado project. 

The main source for this project was the Botique Ado project from the code institute. Code was adpated from this project along the way, with code being copied when it wasn't relevant to be rewritten. The code has been adapted as such that the concepts of Botique Ado are viasble throughout CarFix but so are my own complications and concepts were added along the way to fulfil the user stories.

Other projects have often used multiple sources for reference but the wealth of knowledge in this project has only been supplemented with contact with Tutor Support, to discuss ideas and processes for tackeling problems, Google searchs for more conceptual information, and framework documenation. 

The README.md was constructed with elements from the original template provided by Code Instiute and some elements which are still true for this project have been copied from the README.md of Milestone 2 and Milestone 3 projects also created by Alexander Forrest.

## Media

All stock imagery has been obtained from [unsplash](https://unsplash.com/) and still has the original name including the author in the title of the file.

## Credits & Personal Acknowledgements

### Family
Credit needs to be given where credit is due. I would like to thank my wife and daughter for being patient with me during this project. There have been many ups and downs, inluding a death in the family, and illness, but now everything is together, healthy, happy, and focussed on the future. 

So this project is dedicated to my family. This Covid-19 Pandemic has revealed what is important in life. They have been as much a part of getting this done by supporting me as I have done myself.

### Mentor
I would like to give a special mention to make knowledgable and empathetic tutor Jonathan Munz. Thank you Jonathan for guiding me and being someone I can bounce ideas and concepts off, while keeping my grounded in reality.

### Tutor Support
A massive thank you to tutor support. Without your assitance and guidance this course would not have been the amazing learning experience that it was. There are a few people I would like to give special mention, this are people who have really helped me along the way and for which I will always be grateful: Michael, Igot, Johann, Time & Kevin.