__author__ = 'marvindean'

from locust import HttpLocust, TaskSet, task
import random, string

class NodeEndpoints(TaskSet):

    @task(25)
    def getAllQuotes(self):
        self.client.get("/", name="All Quotes GET")

    @task(10)
    def getRandomQuote(self):
        self.client.get("/quote/random", name="Random Quote GET")

    @task(15)
    def getQuoteByIndex(self):
        self.client.get("/quote/" + str(random.randrange(0, 3)), name="/quote/:id GET")

    @task(30)
    def postNewQuote(self):
        randomauth = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))
        randomtext = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(50))
        self.client.post("/quote", {'author': randomauth, 'text': randomtext}, name="New Quote POST")

    @task(10)
    def updateQuote(self):
        randomauth = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))
        randomtext = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(50))
        self.client.put("/quote/3", {'author': randomauth, 'text': randomtext}, name="Update Quote PUT")

    @task(10)
    def deleteQuote(self):
        self.client.delete("/quote/2", name="Delete Quote DELETE")

class WebsiteUser(HttpLocust):
    task_set = NodeEndpoints
    min_wait = 500
    max_wait = 2000
