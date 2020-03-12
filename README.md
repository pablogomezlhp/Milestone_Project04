# The recipes - CRUD
Time to find a good recipe!
A web application that allows users to store and easily access cooking recipes.
https://milestoneproject04pablosilva.herokuapp.com

## Goal

Create a web applications which enables users to create, read, update and delete (CRUD) their online cookbook. Users can fabricate their recipe database by collecting recipes. The application can be used by non-enrolled users but registred user can use the like/dislike feature.

The core focus of this project is on functional app logic created with Python while utilising the Flask framework and MongoDB NoSQL database.

## UX
The idea was to create a simple and easily accessible CRUD page. For this it was necessary to initially design for mobile devices so that we can discard what was not really necessary. 

## User Stories
As a user of this site, I would like to see details about the recipes, such as method and necessary ingredients. I would also like to see the recipe photo as inspiration and be able to access which recipes had a large number of likes / dislikes


### Desktop 

<img width="1440" alt="Screenshot 2020-03-12 at 18 48 07" src="https://user-images.githubusercontent.com/51464234/76556839-3840e000-6492-11ea-889a-069a13940ee5.png">
<img width="1440" alt="Screenshot 2020-03-12 at 18 48 15" src="https://user-images.githubusercontent.com/51464234/76556877-4b53b000-6492-11ea-9040-77866f189394.png">
<img width="1440" alt="Screenshot 2020-03-12 at 18 48 20" src="https://user-images.githubusercontent.com/51464234/76556913-5c9cbc80-6492-11ea-9af6-4a3c2118e9f6.png">
<img width="1440" alt="Screenshot 2020-03-12 at 18 48 46" src="https://user-images.githubusercontent.com/51464234/76556940-69b9ab80-6492-11ea-8f24-4f4673790cc9.png">
<img width="1440" alt="Screenshot 2020-03-12 at 18 48 56" src="https://user-images.githubusercontent.com/51464234/76556964-73431380-6492-11ea-8f04-1cf99a2b1aa7.png">

### Ipad


<img width="511" alt="Screenshot 2020-03-12 at 18 55 32" src="https://user-images.githubusercontent.com/51464234/76558742-c4a0d200-6495-11ea-9371-40852e55e492.png">
<img width="511" alt="Screenshot 2020-03-12 at 19 02 47" src="https://user-images.githubusercontent.com/51464234/76558777-d1bdc100-6495-11ea-8165-b84a17756683.png">
<img width="511" alt="Screenshot 2020-03-12 at 19 02 59" src="https://user-images.githubusercontent.com/51464234/76558800-db472900-6495-11ea-8d32-53b29d689a8e.png">

<img width="511" alt="Screenshot 2020-03-12 at 19 14 18" src="https://user-images.githubusercontent.com/51464234/76558829-ea2ddb80-6495-11ea-828c-4ebf0bbab02e.png">





### Mobile
<img width="363" alt="Screenshot 2020-03-12 at 19 16 39" src="https://user-images.githubusercontent.com/51464234/76558979-324cfe00-6496-11ea-9142-e5296ea2e926.png"> <img width="363" alt="Screenshot 2020-03-12 at 19 16 51" src="https://user-images.githubusercontent.com/51464234/76559000-3c6efc80-6496-11ea-8dca-58fad25f0a81.png">
<img width="363" alt="Screenshot 2020-03-12 at 19 16 59" src="https://user-images.githubusercontent.com/51464234/76559013-4264dd80-6496-11ea-8d6e-e60c9aae7baa.png"> <img width="363" alt="Screenshot 2020-03-12 at 19 17 18" src="https://user-images.githubusercontent.com/51464234/76559024-47c22800-6496-11ea-87c6-59f0dea2637b.png">
<img width="363" alt="Screenshot 2020-03-12 at 19 17 28" src="https://user-images.githubusercontent.com/51464234/76559035-4e509f80-6496-11ea-8d77-3ad9f3b4a943.png"> <img width="363" alt="Screenshot 2020-03-12 at 19 17 41" src="https://user-images.githubusercontent.com/51464234/76559058-5577ad80-6496-11ea-99c5-4dfa318f4eb1.png">
<img width="363" alt="Screenshot 2020-03-12 at 19 17 50" src="https://user-images.githubusercontent.com/51464234/76559072-5a3c6180-6496-11ea-9f15-4b9c8062c135.png">

### Template Style

I opted for the Materialize framework. As a tool, Bootstrap is excellent to get started, but I feel it cannot create a real quality UI without the need to write a considerable amount of custom CSS to get anywhere close to the look and feel of Materialize which looks great even out of the box.

### Font

The Source Sans Pro choice was selected. The typeface is geometric, elegant, and has a vintage feeling; thus, helping to emphasise a soft natural vibe to the displayed text content which I felt was appropiate for a food app; a subjective opinion, of course.


### Navigation

A navigation bar takes up space and a fixed bar. in this case and that there is a lot of content to be displayed in the form of recipes, etc., I found that it was not necessary to fix the navigation, as there was no real advantage.

## Database Structure
<img width="642" alt="Screenshot 2020-03-12 at 19 29 26" src="https://user-images.githubusercontent.com/51464234/76559922-fadf5100-6497-11ea-87fa-510f2925c362.png"> <img width="684" alt="Screenshot 2020-03-12 at 19 30 01" src="https://user-images.githubusercontent.com/51464234/76559924-fc107e00-6497-11ea-8d1e-6abd890623d7.png">

## Features
### Existing features
Existing Features

* Home Page

It is used to access the user registration page field, account page, recipes page, create/edit page, sign out link, sign in/sign up page.

* Sign Up

I have used for a user to register for an account so they can log in into the app.

* Sign In

Used for a user to login to the app so to access and utilise all available features.

* MongoDB (NoSQL Database)

Stores recipe and user objects.

* Create Page
It is applied for a user to create recipe data.

* Edit Page

For user to update and delete recipe data.

* View Page

It is for a user to update and delete recipe data.

* Recipe Page

Allows a user to read all recipes within the app.

* Account Page

Allows a user to read all recipes created by themselves.

### Features left to implement


* Upgrade current and add additional sifting features
* Include tags on the recipe view page which contains a word or two offering additional recipe related details.
* Add the likelihood to include more than one picture or give pictures to each progression.
* Include remarks area plans
* Add capacity to transfer user photographs
* Add capacity to alter user profile, change the username, password or email.

### Testing


* HTML

Freeformatter

The W3C Markup Validation Service

* CSS

The W3C Markup Validation Service

* Python

Python Formatter

* Phones


Galaxy Note 9
Galaxy S5
Galaxy S9/S9+
iPhone 5/SE
iPhone 6/7/8 (simulated and real device)
iPhone 6/7/8 Plus
iPhone X
LG Optimus L70
Microsoft Lumia 550
Microsoft Lumia 950
Nexus 5X
Nexus 6P
Nokia 8110 4G
Pixel 2
Pixel 2 XL
Tablets

iPad (simulation and actual device)
iPad Mini
iPad Pro (10.5-inch)
iPad Pro (12.9-inch) (simulated and real device)
Kindle Fire HDX
Nexus 10
Nexus 7

* Laptops

MacBook Pro (simulated and real device)
Asus UX 305 (simulation and actual device)

* Televisions

1080p Full HD Television (simulated and real device)
Website responsiveness was also tested by resizing the window with every addition of a new code sequence.
#### Tested Sections 1 HTML & CSS

* External links to third party websites and code authors GitHub repository.

* Checked button sizes so, they were responsive and large enough to be clicked.

* Ensured individual section headers resized and appeared well when viewed on various device screens and added opacity to the navigation bar to allow for more visibility of section header area on smaller devices.

* Spell checked all text content.

* HTML and CSS validation via w3.org.

* Checked margins and padding of the container (sections) to ensure the content within it did not look disproportionate on various screen sizes, individually smaller devices.

* Tested Sections 2 Python

Manual testing was embraced for this application and acceptably passed. An example of the tests directed are as per the following:

### Deployment

#### How the project got deployed to Heroku

1. Make a requirements.txt file utilizing the terminal command 'pip freeze > requirements.txt

2. Make a Procfile with the terminal command echo web: python app.py > Procfile

3. git add and git commit the new prerequisites from the requirements.txt file and Procfile, then 'git push' the undertaking to GitHub.

4. Go to Heroku website.

5. Make another application (app) on the Heroku website by tapping the "New" button on your dashboard. Name your app, followed by selecting Europe as your region.

6. Select application

7. In the "Deployment Method" section, check to see if the application is already connected to GitHub. If not connected then click the relevant button to link the Heroku website to the dashboard.

8. Affirm the connecting of the Heroku application to the right GitHub repository.

9. In the application dashboard, click on "Settings" > "Reveal Config Vars".

10. Set the accompanying config vars:

<table>
     <thead>
          <th>Key</th>
          <th>Value</th>
     </thead>
     <tbody>
          <tr>
               <td>DEBUG</td>
               <td>FALSE</td>
               </tr>
          <tr>
               <td>MONGO_URI</td>
               <td>mongodb+srv://<username>:<password>@cluster0-0oagu.gcp.mongodb.net/recipebook?retryWrites=true</td>
                    </tr>
</table>
              
              PORT | 5000 SECRET_KEY | <your_secret_key>

To retrieve your MONGO_URI please reference the official MongoDB Atlas documentation here
On the dashboard click "Deploy or alternatively in the "Automatic Deployment" section enable "Automatic Deploys" (optional).

In the "Manual Deploy" section, set the branch to "master" then click "Deploy Branch."




Tools and Methods Used for Testing
### Technologies used in this project:
HTML5:
https://en.wikipedia.org/wiki/HTML CSS3:
https://en.wikipedia.org/wiki/Cascading_Style_Sheets Bootstrap 4:
https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework) Javascript:
https://en.wikipedia.org/wiki/JavaScript jQuery
https://en.wikipedia.org/wiki/JQuery d3.js
TMDB api https://www.themoviedb.org/documentation/api
Fontawesome https://fontawesome.com
GoogleFonts https://fonts.google.com
## User Testing
The following test cases have been performed to test functionality:
     -	Alert pop-up
* Expected Behavior = Informs that the name entered has no data available for reading
Form input movie name 
* Expected Behavior = All movies having the entered word are listed in the field below
Click on Movie Details 
* Expected Behavior = Page Reloads with Movie Info 
hover over IMDB icon  
* Expected Behavior = Hover is enabled by changing the color icon. 
Click on IMDB icon 
* Expected Behavior = Website loads IMDB page for movie 
 Click on the "Visit Movie Site" link 
* Expected Behavior = Movie Site Page (If Existing) Will Load 
 Pass Clicking on the "Go back" link on the header 
 Expected Behavior = Site Returns Home


HTML validated via https://validator.w3.org/ - Pass CSS validated via https://jigsaw.w3.org/css-validator/ - Pass Deployment
For this project, I have used Atom to deployed my project and Github Pages to host the application.
Below are the steps I have taken to achieve this:
Navigate to "settings"; Scroll down to "GitHub Pages" section (see image below); Selected "master branch" and deployed. Deployment
## Github Pages Link
https://pablogomezlhp.github.io/TestNonius/
Credits https://www.themoviedb.org/documentation/api
Copyright 2020 - Pablo Patrick




