from country import Country
from user import User
from post import Post
from member import Member
from relationship import Relationship
from userfamily import Userfamily
from photo import Photo
from job import Job
from myjob import Myjob
class Mydb():
  def __init__(self):
    print("hello")
    self.Country=Country()
    self.Job=Job()
    self.Myjob=Myjob()
    self.User=User()
    self.Post=Post()
    self.Member=Member()
    self.Userfamily=Userfamily()
    self.Relationship=Relationship()
    self.Photo=Photo()
