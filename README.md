Originally Created by [Jeff Lindsay](http://progrium.com)

Forked from [https://github.com/Runscope/requestbin](https://github.com/Runscope/requestbin)

License
-------
MIT

Self-hosted version
=====================
Modified to fit self-hosted environment by @aleohl.

## Modifications
* **Remove tracking scripts and images from the templates**
* Remove bugsnag dependency and the code where this was included
* Make the footer smaller whilst preserving the details of Runscope
* Add new css style for blue accent to be used in the logo text
* Change the title of all pages to contain "Self-hosted" and add "Self-hosted" to the logo text
* Define following as environment variables
    * ROOT_URL
    * SESSION_SECRET_KEY
    * MAX_REQUESTS (max request saved by the service, defaults to 20)
    * BIN_TTL (time to life for bins, in seconds, defaults to 48 hours (48*3600))
* Add cURL command to the request view, for faster testing
    * Add separate config option to ignore headers for the cURL command

Looking to self-host?
=====================

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Deploy your own instance using Heroku
Create a Heroku account if you haven't, then grab the RequestBin source using git:

`$ git clone git://github.com/aleohl/requestbin.git`

From the project directory, create a Heroku application:

`$ heroku create`

Add Heroku's redis addon:

`$ heroku addons:add heroku-redis`

Set an environment variable to indicate production:

`$ heroku config:set REALM=prod`

Now just deploy via git:

`$ git push heroku master`

It will push to Heroku and give you a URL that your own private RequestBin will be running.


## Deploy your own instance using Docker

On the server/machine you want to host this, you'll first need a machine with
docker and docker-compose installed, then grab the RequestBin source using git:

`$ git clone git://github.com/aleohl/requestbin.git`

Go into the project directory and then build and start the containers

```
$ sudo docker-compose build
$ sudo docker-compose up -d
```

Your own private RequestBin will be running on this server.


Contributors
------------
 * Barry Carlyon <barry@barrycarlyon.co.uk>
 * Jeff Lindsay <progrium@gmail.com>
