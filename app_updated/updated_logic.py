class Task:

    def __init__(self,title,notification_service=None):
        self.title=title
        self.notification_service=notification_service

    def complete(self):
        if self.notification_service:
            self.notification_service.send(
                f"Task completed:{self.title}"
            )
print("hello world")