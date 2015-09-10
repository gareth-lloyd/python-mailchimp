"""
Mailchimp v3 Api SDK

"""
from mailchimpclient import MailChimpClient
from entities.authorizedapp import AuthorizedApp
from entities.automation import Automation
from entities.message import Message
from entities.campaign import Campaign
from entities.feedback import Feedback
from entities.conversation import Conversation
from entities.abuse import Abuse
from entities.activity import Activity
from entities.client import Client
from entities.list import List
from entities.growth import Growth


class MailChimp(MailChimpClient):
    """
    MailChimp class to communicate with the v3 API
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the class with your user_id and secret_key
        """
        super(MailChimp, self).__init__(*args, **kwargs)
        self.authorized_app = AuthorizedApp(self)
        self.automation = Automation(self)
        self.campaign = Campaign(self)
        self.campaignfeedback = Feedback(self)
        self.conversation = Conversation(self)
        self.message = Message(self)
        self.activity = Activity(self)
        self.abuse = Abuse(self)
        self.client = Client(self)
        self.list = List(self)
        self.growth = Growth(self)