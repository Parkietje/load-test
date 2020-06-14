from locust import HttpUser, TaskSet, task, between
import os
import yaml

#CONFIG
workdir = os.path.abspath(os.getcwd())
with open(workdir + "/config.yaml") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

class Tasks(TaskSet):
    @task(1)
    def post(self):
        print("post")


class Locust(HttpUser):
    host = config["host"]
    wait_time = between(2, 5)
    tasks = [Tasks]
