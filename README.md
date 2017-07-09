# Apprendre

Python 3

## Still **TO DO**

see [view README](https://github.com/tourfl/Apprendre/tree/master/view/#readme)

## Objectifs

- Développer une application permettant d'apprendre les fondamentaux d'une langue (vocabulaire, expression, structures) de la manière la plus efficace possible.

En effet, pour l'apprentissage du vocabulaire, lire plusieurs fois une liste ne permet pas d'être certain de connaître le vocabulaire, quoi de mieux que de l'apprendre en se testant de multiples fois ? Fastidieux à l'écrit, cela devient rapide en utilisant un ordinateur.

- Mettre en oeuvre un système struturé comprenant une API minimale et un SGBD.

## Organisation

- api:    model, i.e. api & database;
- view:   view & controller.

```
README.md
apprendre.py
api/
    README.md
    main.py
    static/

view/
    README.md
    main.py
    templates/
    static/
```

## Modules Python utilisés

inspired from [Techarena51](https://techarena51.com/blog/buidling-a-database-driven-restful-json-api-in-python-3-with-flask-flask-restful-and-sqlalchemy/)

- Web Server: **Flask** for both view and API
- SGBD: **SQLite**
- ORM: **SQLAlchemy**
- API: **Flask-RESTful**
- JSON validator: **Marshmallow**
- template renderer: **Jinja2**