import random

from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def basic(self):
        request_json = {
            "num_list": [random.randint(-1_000_000, 100_00_000) for _ in range(10_000)],
            "top_n": random.randint(10_000,20_000)
        }
        self.client.post("/api/v1/nlargest", json=request_json)
