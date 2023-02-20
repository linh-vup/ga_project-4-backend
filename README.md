# A Rainbow A Day - General Assembly Project 4

[Project Overview](#project-overview) | [Getting Started](#getting-started) | [Project Brief and Timeframe](#project-brief-and-timeframe) | [Technologies Used](#technologies-used) | [Demonstration](#demonstration) | [Process](#process) | [Wins](#wins) | [Challenges](#challenges) | [Bugs & Future Improvements](#bugs--future-improvements) | [Key Learnings](#key-learnings)

# Project Overview

A Rainbow A Day is a full-stack application where users can log their daily food intake according to the “eat the rainbow” food guide. It’s the final project of my General Assembly Software Engineering Immersive course and was built as a solo project using the Django REST framework and React.

**Link to deployment:** [a-rainbow-a-day.netlify.app](https://a-rainbow-a-day.netlify.app/)

Test account credentials: email:`testme@testme.com`, password: `Password!1`

# Getting Started

- Clone or download this and the [frontend's](https://github.com/linh-vup/ga-project-4-frontend) source code
- In backend CLI:
  - Pre-requisites: Python, Pip
  - Install dependencies: `pip install pipenv`
  - Install django and create shell: `pipenv install django`
  - Enter shell for project: `pipenv shell`
  - Run seed: `./seed.sh`
  - Start server: `python manage.py runserver`
- In frontend CLI
  - Install node modules: `npm i`
  - Run server: `npm start`

# Project Brief and Timeframe

Timeframe: 8 days

| Technical Requirements                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Deliverables                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <ul><li>Build a full-stack application by making your own backend and your own front-end</li><li>Use a Python Django API using Django REST Framework to serve your data from a Postgres database</li><li>Consume your API with a separate front-end built with React</li><li>Be a complete product which most likely means multiple relationships and CRUD functionality for at least a couple of models</li><li>Implement thoughtful user stories/wireframes that are significant enough to help you know which features are core MVP and which you can cut</li><li>Have a visually impressive design to kick your portfolio up a notch and have something to wow future clients & employers. ALLOW time for this.</li><li> Be deployed online so it's publicly accessible.</li></ul> | <ul><li>A working app hosted on the internet</li><li>A link to your hosted working app in the URL section of your Github repo</li><li>A git repository hosted on Github, with a link to your hosted project, and frequent commits dating back to the very beginning of the project</li><li>A readme.md file with:<ul><li>An embedded screenshot of the app</li><li>Explanations of the technologies used</li><li>A couple paragraphs about the general approach you took</li><li>Installation instructions for any dependencies</li><li>Link to your user stories/wireframes – sketches of major views / interfaces in your application</li><li>Link to your pitch deck/presentation – documentation of your wireframes, user stories, and proposed architecture</li><li>Descriptions of any unsolved problems or major hurdles you had to overcome</li></ul></li></ul> |

# Technologies Used

- JavaScript (ES6)
- React
- Python
- Django
- PostgreSQL
- HTML5, CSS, Sass
- MUI
- Axios
- JWT
- Bcrypt
- CORS
- Cloudinary
- Postman
- TablePlus
- Git/GitHub
- Figma
- Trello

# Demonstration

![Eat the Rainbow Walkthrough - Home page and Today Log](./assets/project_walkthrough1.gif 'Eat the Rainbow Walkthrough - Home page and Today Log')

![Eat the Rainbow Walkthrough - Past Logs, Sharing and Stats Page](./assets/project_walkthrough2.gif 'Eat the Rainbow Walkthrough - Past Logs, Sharing and Stats Page')

User Flow:

- On the home page, the CTA navigates the user to the login page or to the food log page (depending on the status of the user). New users can register through a link in navbar (where they can also find links to logs and stats).
- On food log pages, users can use the search bar to search for a food item and to add them to the logged food list.
- Users can add or remove food items from current and past food logs.
- A status bar indicates which colors have been logged for that day and once the user logs a full rainbow, a success message appears as well as a social sharing button with which the user can send a tweet (includes a link to the application).
- Users can access food logs from the past through the “Yesterday” tab, where they can select any past date in a calendar and then get redirected to that date’s log.
- On the stats page, users can see an overview of foods eaten, including the amount of times they’ve eaten it (all times).

# Process

## Planning

I got the idea for this project because I used to log my attempts at “eating the rainbow” in a Google spreadsheet and thought that it’d be a great project to create a simpler but more fun application to do so. As I had to build a full-stack application by myself, I wanted to focus on having fewer but engaging and well designed features. The plan was to be able to log foods for current and past days, as well as being able to see stats about the food logs. As a stretch goal, I wanted users to be able to set individual goals and to track them.

I then created an Entity Relationship Diagram for the database architecture as the model for my backend and a simple mock up of the main feature pages.

![Eat the Rainbow Spreadsheet](./assets/readme_spreadsheet.png 'Eat the Rainbow Spreadsheet')  
_Screenshot of my manual spreadsheet tracker_  
![Figma Mock-Up](./assets/readme_figma_mockup.png 'Figma Mock-Up')
![Entity Relationship Diagram](./assets/etr.png 'Entity Relationship Diagram')

(Screenshot of my original “eat the rainbow” spreadsheet log which lacks a lot of white food, app food log mock-up created on Figma and ERD using Quick Database Diagrams)

## Execution

I started my development process by creating my backend and testing the database and endpoints before moving to build out my frontend. While this was a solo project, I still joined the class daily morning stand-up where we updated each other on our progress. I also used Trello to keep track of tickets I created for different tasks.

### Backend

For my backend, I used the Django REST Framework to create a SQL database with RESTful features. While I had only started learning and using Python and Django for the first time just days before I built the project, I found it relatively straight-forward to work with (mostly). Before building out the frontend, I used Postman to test if my back-end requests were working.

Models, Views and Serializers

The database is based on four models:

- User
- Food
- Colors
- User Day

The user days model is the main model with most relationships to others. Rather than having more models or many fields on them, my instructor suggested keeping the attributes and relationships simple, and to render needed information through the frontend.

```python
class UserDay(models.Model):
  user = models.ForeignKey('jwt_auth.User', related_name='user_days', on_delete=models.CASCADE)
  day_logged = models.DateField(blank=True)
  foods_consumed = models.ManyToManyField('foods.Food', related_name='user_days', blank=True)
```

This model holds all the food logs for all users with relations to the user and food model and includes the date the food log is created for (hence the day_logged field has the blank argument set to true, rather than setting the date with `auto_now` or `auto_now_add`).

### Featured Code Snippet:

```python
def post(self, request):
  request.data['user'] = request.user.id
  user_day_to_add = UserDaySerializer(data=request.data)
  try:
      user_day_to_add.is_valid()
      user_day_to_add.save()
      return Response(user_day_to_add.data, status=status.HTTP_201_CREATED)

  except IntegrityError as e:
      res = {
          "detail": str(e)
      }
      return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

  except AssertionError as e:
      return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

  except:
      return Response({"detail": "Unprocessable Entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
```

This is the post request to create a user day entry with error handling, with the `IntegrityError` raising an error when the relational integrity of the database is affected, the `AssertionError` to catch programming errors and the default exception to detect errors like invalid user input.

### Frontend

From day 3 onwards, I started creating the frontend. I connected the backend and frontend using CORS. While working on the frontend, I had to go back to tweak the backend and create additional populated serializers in order to display needed information.

### Featured Code Snippet:

```javascript
let viewedDate = new Date();

if (location.pathname === '/foodlog/today') {
  viewedDate = new Date();
} else if (location.pathname === '/foodlog/yesterday') {
  viewedDate.setDate(viewedDate.getDate() - 1);
} else if (location.pathname === `/foodlog/past/${id}`) {
  viewedDate.setDate(id.slice(8, 10));
  viewedDate.setMonth(id.slice(5, 7) - 1);
  viewedDate.setYear(id.slice(0, 4));
}
viewedDate = viewedDate.toJSON().slice(0, 10);
```

```javascript
API.GET(API.ENDPOINTS.getAllUserDays, API.getHeaders())
      .then(({ data }) => {
        const userDay = data.find((day) => day.day_logged === viewedDate);
        if (userDay) {
          setHasUserDayEntry(true);
          setUserDay(userDay);
          setFoods(userDay.foods_consumed);
d);
          setUserDayId(userDay.id);
          setIsUpdated(false);
        } else {
// rest of API call body
```

I used one common component `FoodListDisplay` to render the main content for the food log pages. Therefore, I used a date variable set based on the `location.pathname` to filter the user day table to check for existing entries for a given day.

### Styling

- After getting all the features to work, I worked on a more detailed design for the pages with Figma and using icons from [vecteezy.com](https://www.vecteezy.com/free-vector/fruit-icon)
- I initially used MUI components to easily provide an interim UI for some of my components like the search bar or the food item cards. For the final design however, I found it easier to use custom styling so I used JSX elements and SCSS for most of my styling, but I kept using the MUI grid system to make the pages responsive.

# Wins

Given the brief and the tight deadline, I’m really proud of the result. It may not be as feature rich as previous group projects, but it does meet the main user need I defined for this project and I think that the design details make it fun to use. I also got a lot more comfortable using Python and Django fundamentals and feel like I now really “got the hang of" React (with the features I’ve used so far).

# Challenges

- While I had my ERD planned and signed off, I did have to go back and add populated serializers and amend my views to render the frontend the way I needed to, which took a good chunk out of my development time.
- I initially planned to display stats based on selected timeframes (e.g. food logs by week or months). As I worked on the stats page last, I struggled to find a solution to filter the user day database based on various date ranges in time so had to be okay with only creating the current stats list.

# Bugs & Future Improvements

- When changing between logs, sometimes it doesn't fetch the correct date's data. I only discovered this bug towards the deadline of the project and couldn't find the pattern or reason in time to fix. This would definitely be something I'd go back to to investigate.
- Refactor my codebase: I didn’t allow enough time towards the end of my projects to review my code and to refactor it more. I know that I’m using some states in my FoodListDisplay component that I could leave out by relying on other given states (e.g. rendering information based on state conditions).
- I want to add functionality to the stats page to filter by week and months and/or to display information in graphs for a visually engaging overview.
- At the moment, there’s no UI for admin functionality (e.g. to add more food items and currently there’s only a limited amount of food items available to add from), so I’d like to add that in future iterations.

# Key Learnings

- For future projects, I’d spend more time for more in-depth planning of what I want my frontend to display and how my backend therefore would have to look like.
- Managing expectations: Before presenting the project, I felt like I didn’t have enough features to show for, despite working long hours for the final result. But in reality, we were only given a week to create a full-stack application by ourselves. Now I have a much better idea of the scope I can manage for a given brief and timeline.
- For this project, I found that working with Django as a backend framework was easier than with Express.js, mainly because a lot of the code is boilerplate and easily adaptable. For future projects, I want to dive deeper into the pros and cons of using Django and Express.js.
