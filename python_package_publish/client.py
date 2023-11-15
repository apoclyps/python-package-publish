from typing import Any

import requests
from requests.exceptions import HTTPError

from python_package_publish.errors import ServiceHTTPError


class HttpClient:
    def __init__(
        self,
        url: str,
        timeout: Any = None,
        has_exception: bool = False,
    ) -> None:
        self._base_url = url
        self._has_exception = has_exception
        self._timeout = timeout

    def get(
        self,
        route: str,
        headers: dict | None = None,
        params: dict | None = None,
        timeout: int = 30,
    ) -> requests.Response:
        if headers is None:
            headers = {}

        if params is None:
            params = {}

        response = requests.get(
            url=f"{self._base_url}/{route}",
            headers=(self._headers() | headers),
            timeout=timeout,
            params=params,
        )
        if self._has_exception:
            try:
                response.raise_for_status()
            except HTTPError as exc:
                raise ServiceHTTPError(exception=exc)
        else:
            response.raise_for_status()
        return response

    def post(
        self,
        route: str,
        data: dict | list | None = None,
        headers: dict | None = None,
        timeout: int = 30,
    ) -> requests.Response:
        if headers is None:
            headers = {}

        response = requests.post(
            f"{self._base_url}/{route}",
            json=data or {},
            headers=(self._headers() | headers),
            timeout=timeout,
        )

        if self._has_exception:
            try:
                response.raise_for_status()
            except HTTPError as exc:
                raise ServiceHTTPError(exception=exc)
        else:
            response.raise_for_status()
        return response

    def put(
        self, route: str, data: dict, headers: dict | None = None, timeout: int = 30
    ) -> requests.Response:
        if headers is None:
            headers = {}

        response = requests.put(
            f"{self._base_url}/{route}",
            json=data,
            headers=(self._headers() | headers),
            timeout=timeout,
        )

        if self._has_exception:
            try:
                response.raise_for_status()
            except HTTPError as exc:
                raise ServiceHTTPError(exception=exc)
        else:
            response.raise_for_status()

        return response

    def patch(
        self,
        route: str,
        data: dict | None = None,
        headers: dict | None = None,
        timeout: int = 30,
    ) -> requests.Response:
        if headers is None:
            headers = {}

        response = requests.patch(
            f"{self._base_url}/{route}",
            json=data or {},
            headers=(self._headers() | headers),
            timeout=timeout,
        )

        if self._has_exception:
            try:
                response.raise_for_status()
            except HTTPError as exc:
                raise ServiceHTTPError(exception=exc)
        else:
            response.raise_for_status()

        return response

    def delete(
        self, route: str, headers: dict | None = None, timeout: int = 30
    ) -> requests.Response:
        if headers is None:
            headers = {}

        response = requests.delete(
            f"{self._base_url}/{route}",
            headers=(self._headers() | headers),
            timeout=timeout,
        )

        if self._has_exception:
            try:
                response.raise_for_status()
            except HTTPError as exc:
                raise ServiceHTTPError(exception=exc)
        else:
            response.raise_for_status()

        return response

    def _headers(self) -> dict:
        return {}
