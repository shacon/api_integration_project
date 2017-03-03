Python 2.7.6

# Installation Instructions (Ubuntu)

    If you don't already have python installed:

    sudo apt-get install python2.7.6

    Install pip

    sudo apt-get install python-pip

    Install the repo

    pip install git+https://github.com/shacon/api_integration_project.git


# Using the library

Open up a terminal and start running python:

    
    $ python
    >>

Import the library

    >> import customer_scoring_lib


Set up the client (enter a different base url as a constructor argmuent to the CustomerScoringClient if you wish)

    >> client = customer_scoring_lib.CustomerScoringClient()


For a user with an income of 40,000, zipcode of 60654, and age of 62, make a request to the api like this:

    >> client.make_request(40000, 60654, 62)
    {'propensity': 0.26532, 'ranking': 'C'}


Make a request for only the user ranking or propensity:

    >> r = client.make_request(40000, 60654, 62)
    >> client.ranking(r)
    'C'
    >> client.propensity(r)
    0.27272



# Running Tests

You can run this project's unit tests by calling python api_integration_app.py on the command line.
