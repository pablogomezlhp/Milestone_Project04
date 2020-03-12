# The recipes - CRUD
Time to find a good recipe!
A web application that allows users to store and easily access cooking recipes.
https://milestoneproject04pablosilva.herokuapp.com

##Goal

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








### Mobile

<img width="378" alt="Screenshot 2020-02-07 at 22 13 10" src="https://user-images.githubusercontent.com/51464234/74071115-dd334d80-49fa-11ea-923c-0971e0b6f532.png">

<img width="378" alt="Screenshot 2020-02-07 at 22 13 20" src="https://user-images.githubusercontent.com/51464234/74071138-f20fe100-49fa-11ea-9991-e12a14aac5e5.png">

<img width="378" alt="Screenshot 2020-02-07 at 22 13 30" src="https://user-images.githubusercontent.com/51464234/74071157-018f2a00-49fb-11ea-9d72-0fd8e13fcb91.png">
  

## Features
### Existing features
The home page features archiving data through local storage, so the latest search is saved and made available without the customer having to type again. It also has an alert that tells you if there are data that relate to the text you entered.
After the movie is selected the site loads a new page that shows the original title of the movie, shows the duration, the company responsible for the production of the movie. It shows a brief introduction to the history of the movie and also has an icon that leads to the IMDB website.
The page also provides an official website of the company responsible for the production of the film.

### Features left to implement
The user Mark feature coudn't be add.
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




