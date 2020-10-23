from __future__ import absolute_import

import logging

from django import forms

from sentry.models import Integration
from sentry.rules.actions.base import IntegrationEventAction

logger = logging.getLogger("sentry.rules")


class JiraNotifyServiceForm(forms.Form):
    # TODO 1.0 Add form fields.

    def __init__(self, *args, **kwargs):
        super(JiraNotifyServiceForm, self).__init__(*args, **kwargs)

    def clean(self):
        return super(JiraNotifyServiceForm, self).clean()


class JiraCreateTicketAction(IntegrationEventAction):
    form_cls = JiraNotifyServiceForm
    label = u"TODO Create a {name} Jira ticket"
    prompt = "Create a Jira ticket"
    provider = "jira"

    def __init__(self, *args, **kwargs):
        super(JiraCreateTicketAction, self).__init__(*args, **kwargs)
        # TODO 1.1 Add form_fields
        self.form_fields = {}

    def render_label(self):
        integration_id = None
        try:
            integration_name = Integration.objects.get(
                provider="jira", organizations=self.project.organization, id=integration_id,
            ).name
        except Integration.DoesNotExist:
            integration_name = "[removed]"

        return self.label.format(name=integration_name)
