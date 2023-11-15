import pytest
import responses

from python_package_publish.client import HttpClient
from python_package_publish.errors import ServiceHTTPError


@responses.activate
def test_service_http_error_for_522_with_no_body() -> None:
    responses.add(
        responses.GET,
        "http://generic-url/request-path",
        json=None,
        status=522,
    )

    with pytest.raises(ServiceHTTPError) as error:
        HttpClient(url="http://generic-url", has_exception=True).get("request-path")

    service_http_error: ServiceHTTPError = error.value  # type: ignore[annotation-unchecked]

    assert isinstance(service_http_error, ServiceHTTPError)
    assert service_http_error.response
    assert service_http_error.response.status_code == 522
    assert service_http_error.error_id is None


@responses.activate
def test_service_http_error_for_522_with_empty() -> None:
    responses.add(
        responses.GET,
        "http://generic-url/request-path",
        json={},
        status=522,
    )

    with pytest.raises(ServiceHTTPError) as error:
        HttpClient(url="http://generic-url", has_exception=True).get("request-path")

    service_http_error: ServiceHTTPError = error.value  # type: ignore[annotation-unchecked]

    assert isinstance(service_http_error, ServiceHTTPError)
    assert service_http_error.response
    assert service_http_error.response.status_code == 522
    assert service_http_error.error_id is None
