# Hyperion
## Installation
1. Follow the guide [here](http://www.bostongis.com/PrinterFriendly.aspx?content_name=postgis_tut01) 
to download and install postgres/postgis
1. [Create an empty postgis database in pgadmin](https://postgis.net/workshops/postgis-intro/creating_db.html) 
(i like calling it hyperion, i also [created](https://www.enterprisedb.com/postgres-tutorials/how-create-postgresql-database-and-users-using-psql-and-pgadmin) a hyperion user before i created the database and set it as the owner)
1. Using pycharm, [install a clone of the repository](https://youtu.be/ukbvdF5wqPQ)
1. Install the python project dependencies
    1. In the terminal run `pip install -r requirements.txt`
1. Copy the following text into the .env file (in hyperion/hyperion folder) and edit to point to your database
    ```
    DEBUG=on
    SECRET_KEY=*e_fa35p522(y3q+x8y0ttk&_t!x1ac-3xz4ilmcd6l^-ev4ki
    DATABASE_URL=postgis://user:password@127.0.0.1:3306/dbname
    ```
1. Run migrations (dont make migrations until you've checked out your own branch)
    1. `python manage.py migrate`
1. Create your superuser `python manage.py createsuperuser`
1. Run the server to see if its working
1. Don't worry about the windows_setup.bat file in the world folder unless you keep your
database on a separate machine from where you're running your pycharm

