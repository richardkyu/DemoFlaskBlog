# DemoFlaskBlog
A minimal application in flask that allows for account creation, post creation, post updating and deletion, and email validation with a backend using SQLAlchemy.

# Tree structure
A tree visualization of the directories to show the changes made as a result of blueprints and configurations. Shown to give a high-level summary of the anatomy of the application.

├── flaskblog
│   ├── config.py
│   ├── main
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-37.pyc
│   │   │   └── routes.cpython-37.pyc
│   │   ├── forms.py
│   │   └── routes.py
│   ├── models.py
│   ├── posts
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-37.pyc
│   │   │   ├── forms.cpython-37.pyc
│   │   │   └── routes.cpython-37.pyc
│   │   ├── forms.py
│   │   └── routes.py
│   ├── site.db
│   ├── static
│   │   ├── main.css
│   │   └── profile_pics
│   │       ├── 8a56eaac4efdbb9d.jpg
│   │       ├── d1016652d3055017.jpg
│   │       └── default.jpg
│   ├── templates
│   │   ├── about.html
│   │   ├── account.html
│   │   ├── create_post.html
│   │   ├── home.html
│   │   ├── layout.html
│   │   ├── login.html
│   │   ├── post.html
│   │   ├── register.html
│   │   ├── reset_request.html
│   │   ├── reset_token.html
│   │   └── user_posts.html
│   └── users
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-37.pyc
│       │   ├── forms.cpython-37.pyc
│       │   ├── routes.cpython-37.pyc
│       │   └── utils.cpython-37.pyc
│       ├── forms.py
│       ├── routes.py
│       └── utils.py
└── run.py
