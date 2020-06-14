from locust import HttpUser, TaskSet, task, between
import os
import yaml

#CONFIG
workdir = os.path.abspath(os.getcwd())
with open(workdir + "/config.yaml") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

#Tasks to be performed by a locust
class Tasks(TaskSet):
    @task(1)
    def post(self):
        print("post")
        files = {"content": open("data/content.jpg", "rb"), "style": open("data/style.jpg", "rb")}
        self.client.post("/", files=files)

#Locust is a simulated user with a task set
class Locust(HttpUser):
    host = config["host"]
    wait_time = between(2, 5)
    tasks = [Tasks]