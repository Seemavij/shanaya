! Shanaya is a ecommerce site. It sell Bridal dresses, Indo western dresses, Men sherwani & gown online.Variety of collection and clothes for sale on resonable rate.

You can reach the live site here.

Table of Contents:

* Business Model :

Shanaya is a B2C business. The business of Shanaya is to sell Men and Women clothes to the public and sell them online on a resonable price. Shanaya sell Bridal & Groom Dresses and other women dresses. We advertise on Facebook and other social Media platform and users can share the page to spread the word about Shanaya.

* User-Experience-Design :

!Site Goals

The site is aimed at anyone they can browse and see over new and all collection at very easily at there comfort zone, and anyone who wants to buy beautifull items. Without signing in the user can browse the online store and buy their items. They can also look at the site blog to see that are being helped by the site. They can log in to see a log of the items they have bought and leave a review of the site. They can also save their details for future purchases.

* Agile Planning :

! This project was developed using agile methodologies, delivering small features over 6 sprints spaced out over 6 weeks. Each issue was labelled must have, should have and could have. The must-have features were completed first, then the should have's, then the could have's. It was done this way to ensure a complete website is made with the nice-to-have features added if there is capacity.

! My kanban board was made using github projects which can be viewed here. Each view can be clicked in to obtain further information.

The user stories were grouped into different Epics

* Epic 1 - Set up

The base setup of the Django app was done first as nothing else can be completed before this is done. I completed the base html, and the header.

Epic 1 user stories

.  As a developer, I need to set up the project so that it is ready for implementing core features
.  As a developer, I want to create a base HTML page so that all pages can use the same format.
.  As a user, I want to be able to navigate around the site easily from any device
Epic 2 - Products and shopping bag

Setting up database model and admin functions and template pages to be able to view the products available to buy and have messages confirming when items have been added to the bag.

* Epic 2 User Stories

. As a shopper, I want to view a list of products so that I can select something to buy
. As a shopper, I want to be able to click into a product to view its details so I can see what size it is etc
. As a user, I want to be able to view what I have added to my shopping bag and the total price
. As a user, I want to be able to delete items from my bag when I decide I no longer want something.
. As a user I want to receive a confirmation when I have made changes ie, adding and removing items to my bag so that I know when a change has been completed.

! Epic 3 - payment and purchase confirmation emails.

* Epic 3 User Stories

Epic 3 User Stories

. As a shopper, I want to be able to easily enter my payment details so that I can purchase my chosen items.
. As a shopper, I want to see confirmation that my payment has gone through successfully and that my purchase is being sent to the correct address so that I know it has been done correctly
. As a shopper I want Shanaya to send me an email so that I can keep confirmation of purchase for my own records.

* Epic 4 Allauth User Stories

. As a new user, I want to be able to sign up easily and intuitively
. As a returning user, I want to be able to log in easily.
. As a user, I want to be able to log out of the site safely and easily.
. As a developer, I want to ensure the forms are all the same style and look good on all devices
. As a developer I want accounts to be secure with email confirmation.

* Epic 5 - Profile Page

. As a user, I want to be able to access a profile page so that I can see my order details
. As a user, I want to see what donations I have made in the past
. As a user, I want to be able to update my details if I have to add a new address.

* Epic 6 - Blog

. As a site user I want to be able to see where the money from the site is being sent so I can feel good about my purchases
. As a site owner I want to easily be able to add blog entries onto the Site
. As a site owner I want to be able to edit my blog posts so that I can make corrections easily
. As a site owner I want to be able to delete blog posts as necessary.
. As a site owner I want to be the only one who can create edit and delete blog posts.

* Epic 7 - Reviews

Epic 7 User Stories

. As a user, I would like to be able to read reviews about the site so I can decide if I want to use it
. As a site user who is logged in, I would like to be able to leave my own review so that I can tell others about my experience
. As a user, it would be nice to give my review a rating out of five for ease of reference
. As a site owner it would be nice to be able to reply to reviews to show a personal touch

* Epic 8 Footer

* Epic 8 User Stories

. As the site owner, I want to share social media links and contact details
. As the site owner, I want a nav bar for the site extras such as the blog, reviews and subscribe pages.

* Epic 9 - Documentation and styling

* Epic 9 Tasks

. Complete Styling on all pages and all screen sizes
. Complete Readme documentation
. Complete testing and writeup

* Scope

. Responsive Design
. Home page with information about Shanaya
. Ability to perform CRUD functionality on the Blog
. Restricted features for not logged in as users and superusers

Structure

Shanaya Features :

Navbar

. user story - As a user, I want to be able to navigate easily around the site from any device

. Navigation Menu

from the main top navigation bar, the user can log in or sign in. Once logged in they can access their profile page.

. They can browse all the site products and check their shopping bag. They can also search the site using the search bar.

* Home Page
. User Story - As a user I want the front page to be clear and self-explanatory so I know I am in the right place
. The front page contains an image of a website. This gives the initial impression of stuff.

. The front page also contains a tagline advising the user they can shop with a button to take them to either place on the website. This gives an immediate idea of what the website is for.

. Under this is information about the site and how to shop

* Footer

. User Story: As the site owner, I want to share social media links and contact details
User Story: As the site owner I want a nav bar for the site extras such as the blog, reviews and subscribe pages
. The Footer has been added to the bottom of the site and contains links to the site’s blog, reviews and donations form. Users can also subscribe to the site’s newsletter from here.

. underneath the footer navigation bar users can see the contact email for the site and links to the social media pages.

. Sign in, log in, log out

. As a new user, I want to be able to sign up easily and intuitively

. As a returning user, I want to be able to log in easily.

. As a user, I want to be able to log out of the site safely and easily.

. As a developer, I want to ensure the forms are all the same style and look good on all devices






* Deployment 
.To deploy my site to Heroku I followed the following steps

. Navigate to heroku and create/log into account
. Click the new button in the top right corner
. Select create new app
. Enter app name (kids-bored)
. Select region and click create app (europe)
. Click the resources tab and search for Heroku Postgres
. Select hobby dev and continue
. Go to the settings tab and then click reveal config vars
. Make sure the correct config bars are added
. AWS_ACCESS_KEY_ID (for access to AWS)
. AWS_SECRET_ACCESS_KEY (for access to AWS)
. SECRET_KEY: (Your secret key)
. DATABASE_URL: (This should already exist with add on of postgres)
. EMAIL_HOST_USER: (email address)
. EMAIL_HOST_PASS: (email app password)
. STRIPE_PUBLIC_KEY (Stripes public key)
. STRIPE_SECRET_KEY (Stripes secret key)
. STRIPE_WH_SECRET (Stripes Web Hook secret key)
. USE_AWS (set to True to use AWS)
. Click the deploy tab
. Scroll down to Connect to GitHub and sign in / authorize when prompted
. In the search box, find the repository you want to deploy and click connect
Scroll down to Manual deploy and choose the main branch
. Click Deploy
. The app should now be deployed

* References
. I used the django documentation
. I used the bootstrap documentation
. I used slack overflow
. I used CI slack community
. I followed the Boutique Ado walkthrough and used it as a base for the site.

* Acknowledgements

. I want to thank:
. My mentor & Tutor for all her guidance
. The wonderful slack community
