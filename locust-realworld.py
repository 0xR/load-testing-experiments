import uuid

from locust import HttpLocust, TaskSet, task


class WebsiteTasks(TaskSet):
    def __init__(self, parent):
        super(WebsiteTasks, self).__init__(parent)

    @task
    def profile(self):
        self.username = "user_%s" % str(uuid.uuid4()).replace("-", "")
        response = self.client.post(
            "/users",
            json={"user": {
                "username": self.username,
                "password": "asdf",
                "email": "%s@mail.com" % self.username,
            }},
        )

        self.headers = {"Autorization": "Token %s" % response.json()["user"]["token"]}
        self.client.get("/profiles/%s" % self.username, headers=self.headers)


class WebsiteUser(HttpLocust):
    host = "http://localhost:8080/api"
    task_set = WebsiteTasks
    min_wait = 0
    max_wait = 0


if __name__ == '__main__':
    x = WebsiteUser()
    x.run()
