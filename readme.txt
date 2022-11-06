TITLE 

Description
-----------
Discord bot that converts pictures you send to LaTeX!

Dependencies
------------
Though user's don't have to install anything, the bot has a few depedencies. Firstly, it
uses an API wrapper for Discord found here: https://github.com/Rapptz/discord.py and is 
hosted on Heroku. 

The requests library is used to make API calls to the LaTeX-OCR API, which was built
from a docker image (https://hub.docker.com/r/lukasblecher/pix2tex) and deployed on
an AWS EC2 instance. The API can also directly be accessed by sending a POST request
to http://54.242.209.107/ (an example of this being done in Postman is in example.jpg). 

The CodeCogs Equation Rendering webservice (https://latex.codecogs.com/) is used to render
the output LaTeX to confirm the validity of the output LaTeX.

The bot also technically uses the platform and os libraries, but they are only used to
hide my discord token and don't provide functionality beyond that.

Get Started
-----------
You don't need to install anything! Just invite the bot to a server with this link:
https://discord.com/oauth2/authorize?client_id=1038541211746717776&permissions=67128320&scope=bot

To use, simply send a picture with the caption "latex", "LaTex", or anything with "tex" in it.