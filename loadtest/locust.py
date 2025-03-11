import time
import random
from locust import HttpUser, task, between


class User(HttpUser):


    wait_time = between(1, 2)


    @task
    def user_page(self):
        user_id = str(random.randint(0, 3))
        self.client.get(url="/users?id=" + user_id,name="Users" )
    # @task
    # def user_page(self):
       
    #     self.client.get(url="/hello" )