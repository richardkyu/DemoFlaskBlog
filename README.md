# DemoFlaskBlog

An application coded using Flask, a micro-framework in Python. This site has functionalities that allow for account creation and updating, post creation, post updating and deletion, and email recovery of passwords with a back-end using SQLAlchemy, along with further security considerations.

## [Visit the demo site here](https://www.demoflaskblog.com/)

You can create a user account yourself or use the following test account details to try out the site.

**Email:** TestUser@demo.com

**Password:** testing

Table of contents
=================

<!--ts-->
   * [Tree Structure](#Tree-structure)
   * [Implementation of User Accounts](#User-Accounts)
   * [Implementation of Create, Read, Update, Delete Functions for Posting](#Posting-Functions)
   * [Site Security](#Security)
   * [Email Reset Password Link Generation](#Email-Reset-Password-Link-Generation)
   * [Linux Server Hosting](#Linux-Server-Hosting)

<!--te-->

![Site Image](https://i.imgur.com/65nwp4m.png)


# Tree structure
A tree visualization of the directories to show the changes made as a result of blueprints and configurations. Shown to give a high-level summary of the anatomy of the application.

This project makes use of Flask packages and blueprints, which are better shown in the picture below.

![tree_structure](https://i.imgur.com/AHIkylM.png)
