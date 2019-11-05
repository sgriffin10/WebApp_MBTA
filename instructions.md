# Web App Development - MBTA Helper 

## Introduction

You may have used multiple Python packages to access information on the Internet. For example, `twython` or `tweepy` can get twitter information by interacting with twitter application programming interface (API). In this project, you will access web APIs directly and begin to write your own package to connect with new data sources. Then you will build a simple website containing some static pages with a small amount of dynamic content.

### Computational Skills Emphasized

- Web API connection
- Structured data (JSON) processing
- Web App Development

### Teaming Logistics:

- You must work in a team.
- Your partners should be in the same term-project team with you.
- Only one of you should fork the base repo for this project. The one that forks the repo should then add the other team members as collaborators on Github for that repo.


## Part 1: Geocoding and Web APIs

The goal for Part 1 to deal with geographical data. You will write a tool that takes an address or place name and returns the closest MBTA stop and the distance from the given place to that stop. For example: 
    
    >>>import mbta_helper
    >>>print(mbta_helper.find_stop_near("Boston Common"))
    Beacon St opp Walnut St

Note: There are already [a few Python packages](https://wiki.python.org/moin/GIS/Web_services) that interface with mapping services, but part of this project is seeing how you might write your own such package from scratch.

### Accessing web data programmatically
APIs let you make requests using specifically constructed URLs and return data in a nicely structured format.

There are three main steps to using any web API:

1. **Read the API documentation:**

    You should specifically look out for whether the API can provide the data you want, how to request that data, and what the return format will be.

2. **Request an API developer key:**

    Web services generally limit the number of requests you can make by requiring a unique user key to be sent with each request. In order to get a key you'll need to agree to their terms, which restrict how you can use the service. In this class we will never ask you to agree to terms you aren't comfortable with - contact your professor if you have an issue.

3. **Test out your application and launch to users**
    (A.K.A. the fun part):

    The first API we will use is the [*MapQuest*](https://developer.mapquest.com/documentation/geocoding-api/address/get/). This tool (among other things) allows you to specify a place name or address and receive its latitude and longitude. Take a few minutes to read the documentation (it's quite good). You need to sign up and get a free API Key from [here](https://developer.mapquest.com/). 

### Structured data responses (JSON)
Back? Ok cool, let's try it out in Python. We're going to request the response in JSON format, which we can decode using Python's [`json` module](https://docs.python.org/3.7/library/json.html).

    import urllib.request
    import json
    from pprint import pprint
    
    MAPQUEST_API_KEY = 'YOUR API KEY'

    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    pprint(response_data)


We used the [`pprint` module](https://docs.python.org/3/library/pprint.html) to "pretty print" the response data structure with indentation so it's easier to visualize. You should see something similar to the JSON response from the documentation, except built from Python data types. This response data structure is built from nested dictionaries and lists, and you can step through it to access the fields you want.

    >>> print(response_data["results"][0]["locations"][0]['postalCode'])
    02481


#### What you need to do
Write a function (maybe two) to extract the latitude and longitude from the JSON response.

### Speaking URL
In the above example we passed a hard-coded URL to the `urlopen` function, but in your code you will need to generate the parameters based on user input. Check out [*Understanding URLs*](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_URL) and their structure for a helpful guide to URL components and encoding.

You can build up the URL string manually, but it's probably helpful to check out [`urlencode` function](<https://docs.python.org/3.7/library/urllib.parse.html#urllib.parse.urlencode>) from `urllib.request` and its [examples](https://docs.python.org/3.7/library/urllib.request.html#urllib-examples).

#### What you need to do
Write a function that takes an address or place name as input and returns a properly encoded URL to make a  Mapquest geocode request.

### Getting local

Now that we can find the coordinates of a given place, let's take things one step further and find the closest public transportation stop to that location. 

To accomplish this, we will use the [*MBTA-realtime API*](https://api-v3.mbta.com/docs/swagger/index.html). Check out the details for `GET /stops` in the documentation.

**Note**: You need to request an API key from [*MBTA V3 API Portal*](https://api-v3.mbta.com).

#### What you need to do
Write a function that takes a latitude and longitude and returns the name of the closest MBTA stop and whether it is wheelchair accessible.

### To Wrap-up
Combine your functions from the previous sections to create a tool that takes a place name or address as input, finds its latitude/longitude, and returns the nearest MBTA stop and whether it is wheelchair accessible.

Note: Sadly there are no MBTA stops close enough to Babson College - you have to get out into the city!

### Making it cooler (Optional)

- Try out some other APIs - there are a lot of resources and we have barely scratched the surface
- By default, `stops` gives all types of transportation, including buses and commuter rail. Allow the user to specify how they'd like to travel (e.g. T only)
- Add in the MBTA realtime arrival data to help choose what station you should walk to
- Connect with other local services. Example: the City of Boston has [an app](https://www.boston.gov/departments/new-urban-mechanics/street-bump)  that uses a phone's GPS and accelerometer to automatically report potholes to be fixed. You can also see many other appsdeveloped for Boston residents [here](https://www.boston.gov/departments/innovation-and-technology/apps).

## Part 2: Web App
The goal for Part 2 is to build a simple website that uses the module `mbta_helper` you created in Part 1. 

`Flask` is a lightweight and powerful web framework for Python. It's easy to learn and simple to use, allowing you to build your web app in a short amount of time. 

### Get Started
You need to first install `Flask`. Run the following command:

    pip install Flask

### Why Flask?

In the introduction, we defined `Flask` as a 'web framework', but what does that actually mean? Let's dig deeper. Before this, let's develop a better understanding of how the internet works.

When you open up a web page in your browser (e.g. Chrome, Firefox, etc.), it makes an HTTP request to a server somewhere in the world. This could be something like GET me the home page. This server handles this request, sending back data (this can be in the form of HTML, JSON, XML, etc.), which is rendered by your browser.

This is where Flask comes in - it allows you to create the logic to make a web server quickly in Python. You can write logic that will execute when a request is made for one of your routes (e.g. www.mycoolwebsitefrompythonclass.com/home).

### Quickstart
Flask Quickstart documentation: <https://flask.palletsprojects.com/en/1.1.x/quickstart/>

Read the following sections

- A Minimal Application
- What to do if the Server does not Start    
    - Invalid Import Name
- Debug Mode
- Routing
    - Variable Rules
    - Unique URLs / Redirection Behavior
    - URL Building
    - HTTP Methods
- Static Files
- Rendering Templates
- Redirects and Errors

**Follow every single step in this tutorial. Replicate all the code. Make the server run!** 

### What you need to do next - build your own app by getting input from the user

What use is a web application if you can't get any data back from the user? Let's set up our MBTA helper app. Here are our end specifications:

1. Upon visiting the index page at `http://127.0.0.1:5000/`, the user will be greeted by a page that says hello, and includes an input **form** that requests a place name.
2. Upon clicking the 'Submit' button, the data from the form will be sent via a POST request to the Flask backend at the route `POST /nearest`
3. (Optional) Perform some simple validation on the user input. See [wtforms](https://flask.palletsprojects.com/en/1.1.x/patterns/wtforms/).
4. The Flask backend will handle the request to `POST /nearest_mbta`. Then your app will render a `mbta_station` page for the user - presenting nearest MBTA stop and whether it is wheelchair accessible. In this step, you need to use the code from Part 1.
5. If something is wrong, the app will render a simple error page, which will include some indication that the search did not work, in addition to a button (or link) that will redirect the user back to the home page.

It will be up to you to make this happen. If you feel confident in your ability to implement this, go for it! If you'd like more scaffolding, continue reading.

### Tips and tricks

To complete this project, the official Flask documentation will get you pretty far. There is the [*full documentation*](https://flask.palletsprojects.com/en/1.1.x/#user-s-guide).

- **HTML Forms:**. To make forms in HTML, check out [*w3schools*](https://www.w3schools.com/html/html_forms.asp). For even more information, check [*this*](https://lmgtfy.com/?q=html+forms) out.

- **Sending POST Requests:** To send the data from the form in a POST request, use an input with type `submit`, and set the action of the form to reflect the destination in your routes.

- **Handling POST Requests:** To learn more about handling post requests in Flask, read section [*HTTP Methods*](https://flask.palletsprojects.com/en/1.1.x/quickstart/#http-methods) again.

- **Accessing the Form Data:** To access the form data, check out section [*'The Request Object'*](https://flask.palletsprojects.com/en/1.1.x/quickstart/#the-request-object) on using the Flask `request` utility.

### Going further (Optional)

- **Learn more about [Django](<https://www.djangoproject.com/>)**  - an alternative to Flask. They don't have many major differences other than some small quirks in conventions and style. 
- **Want to keep track of some data in your web app?** Instead of using a .txt file or a pickle file, it's common practice in nearly any web app to use a database. A few especially well-known database choices are MySql, SQLite, or PostgreSQL, which all use SQL(Structured Query Language) to manipulate all stored, as do many other common relational databases. You also may have heard some buzz about MongoDb, which uses an unstructured data format in documents similar to JSON. Mongo is stupidly easy to set up and use, but I'd stop and think first before jumping right in. It may be the easy choice, but representing your data intelligently in a relational table can be much more effective and less of a headache later on.
- **But HTML is so ugly!** HTML alone is very ugly. That's why we use CSS (Cascading Style Sheets) to add some extra flair and style to our HTML. You can change pretty much anything about HTML - colors, shapes, sizes, placement, etc. with CSS rules. It's also pretty simple to write. Check [this resource](https://www.w3schools.com/css/css_intro.asp) out to learn more about CSS.
- **What about making my website dynamic?** Our class may be a class in Python, but we can venture out a little and use some jQuery. jQuery might seem scary, but you use it in a way similar to adding/linking CSS styling to your HTML. You write scripts in JavaScript (which isn't too difficult), which can allow you to add beautiful responsive and dynamic content to your web app.

## Project Wrap-up
### Getting Started

To start this project, you should fork and clone the base repo for this project in class Github. Remember, that you will want to have only one of your teammates fork the repo, and then the other members should be added as collaborators on Github for that repo. 


### Project Writeup and Reflection
Please prepare a short document (~1 page not including figures) with the following sections:

**Project Overview** [~1 paragraph]
Write a short abstract describing your project. Include all the extensions to the basic requirements.

**Project Reflection** [~2 paragraphs]
After you finish the Please prepare a short document for reflection [~2 paragraphs]

From a process point of view, what went well? What could you improve? Other possible reflection topics: Was your project appropriately scoped? Did you have a good plan for unit testing? What self-studying did you do? How will you use what you learned going forward? What do you wish you knew before you started that would have helped you succeed?

Also discuss your team process in your reflection. How did you plan to divide the work (e.g. split by class, always pair program together, etc.) and how did it actually happen? Were there any issues that arose while working together, and how did you address them? What would you do differently next time?

### Turning in your assignment

1. Push your completed code to the "master" Git repository (depending on which team member's repository is being used to work on the project).

2. Submit your Project Writeup/Reflection (1 per team, not 1 per person). This can be in the form of either:
    + a PDF document pushed to GitHub, or
    + a project web page (if you choose this route, make sure there is a link to your web page in your README.md file in your Github repo)

3. Create a pull request to the upstream repository

4. Zip all the files into a zip file, named *project_webapp_MemberLastNames.zip*. Upload it to Blackboard. In the comment area on Blackboard, specify names of all team members and url of GitHub repository. **Everyone in the team needs to submit the zip file to Blackboard and add comment.**


