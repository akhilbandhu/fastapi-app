from locust import HttpUser, task, between
import random

class FastAPIUser(HttpUser):
    host = "http://127.0.0.1:60109"  # Update this to match your service's NodePort
    wait_time = between(1, 5)

    @task(2)
    def get_root(self):
        self.client.get("/")

    @task(1)
    def get_item(self):
        item_id = self.random_item_id()
        self.client.get(f"/items/{item_id}")

    def random_item_id(self):
        return random.randint(1, 100)
