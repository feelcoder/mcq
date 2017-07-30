# mcq 

This is a python project build in Flask. It is an MCQ management information system

Folder structure

 root
  -- app
     -- __init__.py
     -- module_one # module name
         -- __init__.py
         -- controllers.py # route controllers
         -- models.py # database 
         -- forms.py
    -- templates
      -- module_one
        -- *.html
  -- config.py # application wide configurations 
  -- run.py # serves the app

  #Running the application

  cd mcq
  python run.py

  # Got to browser

  http://localhost:8080

  e.g http://localhost:8080/auth/signin