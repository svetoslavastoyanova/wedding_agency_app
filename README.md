# wedding_agency_app
This is an app for a wedding agency
First I want to sincerely apologize that I hadn't added my ap to my main branch but in order not to ruin it in any way I left it like that.

#Description
This is an app for a wedding agency called "Your dream wedding".
The Navbar is consisted of theese sections: Home, About us, Prices, Testimonials, Comments, Gallery, Sign-in, Sign-out, Add Post
Home, About us and Prices are rendering just an html files with custom written css. For the CSS and html formatting I took inspiration from some youtubers from which I learned a lot.

Testimonials page is rendering the testimonials of all the authenticated users. All of the testimonials have 'see detail' buttons which when clicked are leading to their own details pages. 
Every testimonial detail's page can be viewed by everyone(authenticated and unauthenticated users) but only authenticated users can like the specified testimony. When clicking on the
heart button unauthenticated users will be redirecting to the 'sign-in' page. Authenticated users(users which posted their own testimony) have the chance to edit and delete their testimonials.
When button 'edit' is clicked it will redirect the user to an edit form page. They will be requested to write the title with an upper case letter in order to percieve, due to the validator I created for this purpose.
When button 'delete' is clicked it will redirect the user to a delete form page, asking the user whether he is sure he wants to delete it ot go back. When delete is cliked it will redirect them to the testimonials page.

Comment page. For this page I originally came up with the idea of creating a page with all of the authenticated users opinions(plus showing their photos, and review). I realised though that I will need at leats one post users will need to connect with in order to make a comment. Thats why I created one hidden endpoint(Add Post) which only admins will be able to see.
When added the post will be rendered in the Comment page, and by clicking the button, it will lead users to the comment sectionshowing all the comments (if they exist) and letting them comment as well. Of course only authenticated users are allowed to comment. When clicking the add comment button all of the unauthenticated users will be redirected again to the 'sign-in' form with the help of the @login_required decorator.

Gallery page is consisted again of HTML and CSS only. 

Add Post(hidden) connected to the Comment Page. The idea is for it to have only one main post, in which users can leave their opinions and comments.

Sign In and Sign Up page are rendering a form page decorated with CSS and HTML . I used the same template since I really do like the way it looks.

Sign Out is redirecting users to the home page.
When signed in users can go to their own profile page in which they can edit their profiles but they will see the same validator used in the testimonial edit form if they start their names with non capital letter.
They can also change their photos if they like. Other thing they can do from their profiles is the actual adding of a testimony. They can also use the edit and delete form from there.

Administration:
Only admins have an access to the administration. From there they have full CRUD functionalities.

Mandatory requirements/tests:
I tested mainly the views because they are connected to both the Models and the Forms.


Bonus requirements:
Extended Django user: For the profiles I used an extended django user with which the user can be authenticated by his email.
Class-Based Views: I used several CBV's in my wedding_auth app.

Database:
Postgress is used for this project.

I will continue working on this app but I hope you like it and I hope it has the needed functionalities.
Best wishes, stay safe!



