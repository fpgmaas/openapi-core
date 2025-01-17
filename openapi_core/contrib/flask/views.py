"""OpenAPI core contrib flask views module"""
from typing import Any

from flask.views import MethodView

from openapi_core.contrib.flask.decorators import FlaskOpenAPIViewDecorator
from openapi_core.contrib.flask.handlers import FlaskOpenAPIErrorsHandler
from openapi_core.spec import Spec


class FlaskOpenAPIView(MethodView):
    """Brings OpenAPI specification validation and unmarshalling for views."""

    openapi_errors_handler = FlaskOpenAPIErrorsHandler

    def __init__(self, spec: Spec):
        super().__init__()
        self.spec = spec

    def dispatch_request(self, *args: Any, **kwargs: Any) -> Any:
        decorator = FlaskOpenAPIViewDecorator(
            self.spec,
            openapi_errors_handler=self.openapi_errors_handler,
        )
        return decorator(super().dispatch_request)(*args, **kwargs)
