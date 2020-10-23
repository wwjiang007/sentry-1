from __future__ import absolute_import

import logging

from django import forms

from sentry.models import Integration
from sentry.rules.actions.base import IntegrationEventAction

logger = logging.getLogger("sentry.rules")


class AzureDevopsNotifyServiceForm(forms.Form):
    # TODO 2.0 Add form fields.

    def __init__(self, *args, **kwargs):
        super(AzureDevopsNotifyServiceForm, self).__init__(*args, **kwargs)

    def clean(self):
        return super(AzureDevopsNotifyServiceForm, self).clean()


class AzureDevopsCreateTicketAction(IntegrationEventAction):
    form_cls = AzureDevopsNotifyServiceForm
    label = u"TODO Create a {name} AzureDevops workitem"
    prompt = "Create a AzureDevops workitem"
    provider = "vsts"

    def __init__(self, *args, **kwargs):
        super(AzureDevopsCreateTicketAction, self).__init__(*args, **kwargs)
        # TODO 2.1 Add form_fields
        self.form_fields = {}

    def render_label(self):
        integration_id = None
        try:
            integration_name = Integration.objects.get(
                provider="vsts", organizations=self.project.organization, id=integration_id,
            ).name
        except Integration.DoesNotExist:
            integration_name = "[removed]"

        return self.label.format(name=integration_name)
