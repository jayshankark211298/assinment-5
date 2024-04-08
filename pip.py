C:\Users\User>pip install Flask
Requirement already satisfied: Flask in c:\python312\lib\site-packages (3.0.2)
Requirement already satisfied: Werkzeug>=3.0.0 in c:\python312\lib\site-packages (from Flask) (3.0.2)
Requirement already satisfied: Jinja2>=3.1.2 in c:\python312\lib\site-packages (from Flask) (3.1.3)
Requirement already satisfied: itsdangerous>=2.1.2 in c:\python312\lib\site-packages (from Flask) (2.1.2)
Requirement already satisfied: click>=8.1.3 in c:\python312\lib\site-packages (from Flask) (8.1.7)
Requirement already satisfied: blinker>=1.6.2 in c:\python312\lib\site-packages (from Flask) (1.7.0)
Requirement already satisfied: colorama in c:\python312\lib\site-packages (from click>=8.1.3->Flask) (0.4.6)
Requirement already satisfied: MarkupSafe>=2.0 in c:\python312\lib\site-packages (from Jinja2>=3.1.2->Flask) (2.1.5)

C:\Users\User>pip install check-requirements-txt
Collecting check-requirements-txt
  Downloading check_requirements_txt-1.2.1-py3-none-any.whl.metadata (3.0 kB)
Downloading check_requirements_txt-1.2.1-py3-none-any.whl (6.1 kB)
Installing collected packages: check-requirements-txt
Successfully installed check-requirements-txt-1.2.1

C:\Users\User>pip list
Package                Version
---------------------- ----------
blinker                1.7.0
certifi                2023.11.17
charset-normalizer     3.3.2
check-requirements-txt 1.2.1
click                  8.1.7
colorama               0.4.6
Flask                  3.0.2
idna                   3.6
itsdangerous           2.1.2
Jinja2                 3.1.3
MarkupSafe             2.1.5
pip                    24.0
requests               2.31.0
urllib3                2.1.0
Werkzeug               3.0.2

C:\Users\User>pip uninstall flask
Found existing installation: Flask 3.0.2
Uninstalling Flask-3.0.2:
  Would remove:
    c:\python312\lib\site-packages\flask-3.0.2.dist-info\*
    c:\python312\lib\site-packages\flask\*
    c:\python312\scripts\flask.exe
Proceed (Y/n)? y
  Successfully uninstalled Flask-3.0.2

C:\Users\User>pip list
Package                Version
---------------------- ----------
blinker                1.7.0
certifi                2023.11.17
charset-normalizer     3.3.2
check-requirements-txt 1.2.1
click                  8.1.7
colorama               0.4.6
idna                   3.6
itsdangerous           2.1.2
Jinja2                 3.1.3
MarkupSafe             2.1.5
pip                    24.0
requests               2.31.0
urllib3                2.1.0
Werkzeug               3.0.2
