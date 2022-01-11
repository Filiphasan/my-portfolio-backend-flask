from db import db

from src.utils.role_enum import Roles
from src.models.users import UsersModel
from src.models.about_me import AboutMeModel

def seed_data():
    user = UsersModel.query.filter_by(email="test@test.com").first()
    if not user:
        user1 = UsersModel(id="e6af78d6-3bed-4a8b-8498-d7bcedf3bfb0",first_name="Hasan", last_name="Erdal",username="deneme",email="test@test.com",password_hash="e10adc3949ba59abbe56e057f20f883e", role=Roles.admin.value)
        user1.email_confirmed = True
        #password=123456
        db.session.add(user1)
        db.session.commit()
    about_me = AboutMeModel.query.get("c5caf159-690c-4285-be93-186b14df6f35")
    if not about_me:
        about_me1 = AboutMeModel(id="c5caf159-690c-4285-be93-186b14df6f35",full_name="Hasan Erdal",job_title="Jr. Full Stack Developer",short_desc="I am a Jr. Full Stack Developer. I'm interested in .Net, Asp.Net, Reactjs, JavaScript, React Native",profile_photo="",birth_date="1998-06-17",phone_number="+905370352059",email="hasaerda@hotmail.com",short_adress="Şahinbey/Gaziantep, Turkey")
        db.session.add(about_me1)
        db.session.commit()