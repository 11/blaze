
"""
commands:
- init: 
    - create a directory with the name if specified -- otherwise assume -it's the current directory
    - create the project structure depending on project type:

        STATIC STRUCTURE
        - src/
            - static/
                - js/
                - views/
                - css
            - entries/ 
            - index.html
        
        SINGLE PAGE STRUCTURE
        package.json
        webpack.config.js
        _redirects
        - src/
            - views/ JS files here
            - styles/ JS files here
            - components/ JS files here
            - entries/ md files here
            routes.json
            index.js
            index.html
        


- build:
    - STATIC: compile blogs into html
    - SPA: compile blogs into JSON files

- serve: 
    - run webpack dev server if single page app
    - run local file server and list for changes
"""