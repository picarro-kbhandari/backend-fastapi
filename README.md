
This is an python FastAPI backend. 
## project structure 
- models will contain schemas for the data as needed by the applicaiton.
- routes will caontain different api endpoints configured for the application.
- controller will contain all the logic to handle different endpoints. 
- config will contain all the nessory config for application.



## Git Flow Guidelines 

# master branch will be used only for deployment. 
# develop branch will be used for working/development. When working on a feature create a new branch from develop. 
Tips to avoid merge conflicts: 

# Work on separate files, and communicate with your partner. 
Initial setup of the back-end should be preferably done in pair, 
taking turns while coding and preferably coding on one laptop (pair programming). 
Do daily checkpoints with the co-worker part of the code tha you will be working on.
Make smaller commits, and write descriptive messages: 
Max. 50 characters
Use crucial e.g. : 
"Add session middleware to app.js " 
"Add UserModel.js" 
"Bugfix route '/login' in routes/auth.js " 
 
Working for the branches: 

For example 
the angle brackets < > indicate the identifier/parameter/argument values that are provided by the user. 
 
# Create a new branch and move to that branch 
git checkout -b <branch-name> 

# Move to an existing branch 
git checkout <branch-name> 
# Check the branch you are on and 
# List all the existing branches 
git branch 

# Delete a branch  
git branch -D <name-of-the-branch-to-delete> 
# Merge code from another branch into a current branch 
git merge <branch-from-which-to-merge> 
# List the created commits on the current branch 
git log 
