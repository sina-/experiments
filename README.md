experiments
===========

Collection of hobby projects

how to git with eclipse
===========

- create the repository on git
- create the project structure in ecplipse
        - new -> PyDev Project ...
        - set the location to ~/workspace/{project}
        - add the stubs
                - add ./src
                - add ./src/{project}
                - add ./src/{project}/{module}.py
- connect the eclipse to git
        - right click on project -> team -> share project -> git
        - create repository in ~/git/{repository}
        - finish
- notice the repository-project structure of git
        - a repositroy resides in ~/git/{repository} and it could hold several projects
                - it is not recommended to mix different projects in one repository
                - it is recommended to create repository per project basis
        - ~/git/{repository}/.git holds the structure of the repositrory
        - ~/git/{repository}/{project} holds the working copy of the projects from ~/workspace 
        - ~/git/{repository}/{project}/.project holds the eclipse project settings
        - after sharing the project the ~/workspace/{project} is moved inside ~/git/{repository}/{project}
- add and commit the stub to local git
        - using egit
                - Team -> ...
        - command line
                - git add src
                - git commit -m 'added {project} stub
- connect the repo to github
        - git remote add origin https://github.com/{username}/{repository}.git
        - git pull origin master
        - git push -u origin master
		- -u flag will automatically add the configurations to track the remote master branch
- cloning the repo
        - clone from command line
                - git clone https://github.com/{username}/experiments.git
                - the following steps are NOT RECOMMENDED
                        - create a temp project to produce .project and .pydevproject files
                                - edit .project files
                                - move them inside ./experiments
                        - import experiments
                - note that in general git projects can not be in workspace since eclipse will complain a project with the same name exists
                - the method explained above is a workaround for this problem
