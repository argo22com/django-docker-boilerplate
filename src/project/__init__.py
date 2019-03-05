from __future__ import absolute_import, unicode_literals

import os


DSN = os.environ.get('SENTRY_DSN', None)
if DSN is not None:
    import sentry_sdk
    sentry_sdk.init(DSN)

from .celery import app as celery_app


# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.

__all__ = ('celery_app',)
