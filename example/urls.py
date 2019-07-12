from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from graphene_sentry import SentryGraphQLView,\
    SentryFileUploadGraphQLView

from .schema import schema  # Your graphQL schema

urlpatterns = [
    url(
      r'^graphql',
      csrf_exempt(SentryGraphQLView.as_view(schema=schema)),
      name='graphql',
    ),
    url(
      r'^file_graphql',
      csrf_exempt(
          SentryFileUploadGraphQLView.as_view(schema=schema)),
      name='file_graphql',
    ),
    url(
      r'^graphiql',
      csrf_exempt(SentryGraphQLView.as_view(graphiql=True, schema=schema)),
      name='graphiql',
    ),
    url(
      r'^file_graphiql',
      csrf_exempt(
          SentryFileUploadGraphQLView.as_view(graphiql=True, schema=schema)),
      name='file_graphiql',
    ),
]
