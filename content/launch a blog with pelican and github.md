title: Start blogging with Pelican and Github
date: 12/02/2019
tags: pelican, git
keywords: pelican, git, blogging
category: pelican
slug: start_blogging_with_pelican_and_github
author: John Yu
summary: Pelican is a Python based static site generator great for making blogs with simply text. The content can be written in reStracutred or Markdown syntax. Both are easy to learn. Here I take notes on how to set up a Pelican site on GitHub. There are various ways to make such a site but I found the following to be most streamlined. I assume you are familiar with Python, MacOS/Linux command line, git commands.
lang: en
status: published



Pelican is a Python based static site generator great for making blogs with simply text. The content can be written in reStracutred or Markdown syntax. Both are easy to learn. Here I take notes on how to set up a Pelican site on GitHub. There are various ways to make such a site but I found the following to be most streamlined. I assume you are familiar with Python, MacOS/Linux command line, git commands.

## Install Pelican
There are a few packaged to be installed before we can get Pelican running. Type in the following lines in your terminal. It's recommended to use a virtual environment.

	$ pip install pelican markdown 


## Set up username.github.io repositories
If already registered an account, log in to Github and create two new repositories, username.github.io-src and username.github.io. The username.github.io-src repository will hold the sources of your blog and the username.github.io repository will contain the output HTML files Pelican generates. To add the output directory as a submodule, initialize it with a README file.


Clone the source repository you created:

	git clone git@github.com:username/username.github.io-src blog
	
Then change directory to the site:

	cd blog

## Set up the blog with Pelican
Double check that you’re working in the source git repository using:

	git remote -v
You should see that you are using the username.github.io-src repository. Then, clone the output repository as a git submodule (substitute your Github username):

	git submodule add git@github.com:username/username.github.io.git output
Pelican provides an excellent quickstart command. Run it:

	$pelican-quickstart
	Welcome to pelican-quickstart v4.0.1	
	This script will help you create a new Pelican-based website.
	
	Please answer the following questions so this script can generate the files
	needed by Pelican.


	> Where do you want to create your new web site? [.] .
	> What will be the title of this web site? Blog Title Goes Here
	> Who will be the author of this web site? Author Name Goes Here
	> What will be the default language of this web site? [English] en
	> Do you want to specify a URL prefix? e.g., https://example.com   (Y/n) y
	> URL prefix: http://username.github.io
	> Do you want to enable article pagination? (Y/n) y
	> How many articles per page do you want? [10] 5
	> What is your time zone? [Europe/Paris] asia/shanghai
	> Do you want to generate a tasks.py/Makefile to automate generation and publishing? (Y/n) y
	> Do you want to upload your website using FTP? (y/N) n
	> Do you want to upload your website using SSH? (y/N) n
	> Do you want to upload your website using Dropbox? (y/N) n
	> Do you want to upload your website using S3? (y/N) n
	> Do you want to upload your website using Rackspace Cloud Files? (y/N) n
	> Do you want to upload your website using GitHub Pages? (y/N) y
	> Is this your personal page (username.github.io)? (y/N) y
	
	Done. Your new project is available at /Users/username/PycharmProjects/blog_test/src/blog


You will receive an error message because the output directory already exists. It is OK.

Open the publishconf.py file and set the DELETE\_OUTPUT\_DIRECTORY variable to False. 

## Publish the first post
Write a quick post, I'd like to use Markdown but reStructured would work fine as well. Put the new post into the content folder and it's ready to go.

Build your blog and test the results:

	make devserver
This builds the blog, and then runs a local webserver on port 8000. Check in the browser if everything turned out as intended. If everything is checks out, generate the website:

	make publish
Then add your files to git tracking, commit them, and push to the repositories. 

	cd output
	git add .
	git commit -m "First post."
	git push -u origin master
Due to the use of a submodule, you should do this with your output files before you push the source files.

	cd ..
	git add .
	git commit -m "First commit."
	git push -u origin master
Now, you can visit the <https://username.github.io> and check out the new site.



