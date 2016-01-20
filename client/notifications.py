from client.base import BaseAPIClient


class NotificationsAPIClient(BaseAPIClient):
    def send_sms_notification(self, to, message):
        notification = {}
        notification.update({
            "to": to,
            "message": message
        })

        return self.post(
            '/notifications/sms',
            data={
                "notification": notification
            })

    def send_email_notification(self, to, from_, subject, message):
        notification = {}
        notification.update({
            "to": to,
            "from": from_,
            "subject": subject,
            "message": message
        })
        return self.post(
            '/notifications/email',
            data={"notification": notification})

    def get_notification_by_id(self, id):
        return self.get('/notifications/{}'.format(id))
