from app.extentions import db

# to run raw queries on command prompt use "flask shell"
# run following commands to create a new user in DB
    # from app.extentions import db,User
    # from app.models import user
    # new_user = user(name="Waqas", email="w@mail.com")
    # new_user
    # db.session.add(new_user)
    # db.session.commit()
#run following command to print new user details
    #print(new_user.id, new_user.name, new_user.email)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)