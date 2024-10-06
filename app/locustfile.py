from locust import HttpUser, task, between
import random

class FastAPIUser(HttpUser):
    wait_time = between(1, 5)

    @task(2)
    def get_root(self):
        self.client.get("/")

    @task(1)
    def get_item(self):
        item_id = random.randint(1, 100)
        self.client.get(f"/items/{item_id}")
