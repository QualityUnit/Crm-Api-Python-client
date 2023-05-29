# coding: utf-8

"""
    CRM API

    This page contains complete API documentation for CRM software.  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Contact: support@qualityunit.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated
from typing import overload, Optional, Union, Awaitable

from pydantic import StrictBool, constr, validator

from typing import Optional

from qu.crm.models.ids import Ids
from qu.crm.models.mass_response import MassResponse

from qu.crm.api_client import ApiClient
from qu.crm.api_response import ApiResponse
from qu.crm.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class MassActionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @overload
    async def mass_delete(self, ids : Ids, **kwargs) -> MassResponse:  # noqa: E501
        ...

    @overload
    def mass_delete(self, ids : Ids, async_req: Optional[bool]=True, **kwargs) -> MassResponse:  # noqa: E501
        ...

    @validate_arguments
    def mass_delete(self, ids : Ids, async_req: Optional[bool]=None, **kwargs) -> Union[MassResponse, Awaitable[MassResponse]]:  # noqa: E501
        """Delete multiple subscriptions  # noqa: E501

        Delete multiple subscriptions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.mass_delete(ids, async_req=True)
        >>> result = thread.get()

        :param ids: (required)
        :type ids: Ids
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: MassResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the mass_delete_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.mass_delete_with_http_info(ids, **kwargs)  # noqa: E501

    @validate_arguments
    def mass_delete_with_http_info(self, ids : Ids, **kwargs) -> ApiResponse:  # noqa: E501
        """Delete multiple subscriptions  # noqa: E501

        Delete multiple subscriptions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.mass_delete_with_http_info(ids, async_req=True)
        >>> result = thread.get()

        :param ids: (required)
        :type ids: Ids
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(MassResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'ids'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method mass_delete" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['ids'] is not None:
            _body_params = _params['ids']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['privileges']  # noqa: E501

        _response_types_map = {
            '200': "MassResponse",
        }

        return self.api_client.call_api(
            '/subscriptions/massAction/_delete', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @overload
    async def mass_suspend(self, ids : Ids, **kwargs) -> MassResponse:  # noqa: E501
        ...

    @overload
    def mass_suspend(self, ids : Ids, async_req: Optional[bool]=True, **kwargs) -> MassResponse:  # noqa: E501
        ...

    @validate_arguments
    def mass_suspend(self, ids : Ids, async_req: Optional[bool]=None, **kwargs) -> Union[MassResponse, Awaitable[MassResponse]]:  # noqa: E501
        """Suspend multiple subscriptions  # noqa: E501

        Suspend multiple subscriptions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.mass_suspend(ids, async_req=True)
        >>> result = thread.get()

        :param ids: (required)
        :type ids: Ids
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: MassResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the mass_suspend_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.mass_suspend_with_http_info(ids, **kwargs)  # noqa: E501

    @validate_arguments
    def mass_suspend_with_http_info(self, ids : Ids, **kwargs) -> ApiResponse:  # noqa: E501
        """Suspend multiple subscriptions  # noqa: E501

        Suspend multiple subscriptions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.mass_suspend_with_http_info(ids, async_req=True)
        >>> result = thread.get()

        :param ids: (required)
        :type ids: Ids
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(MassResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'ids'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method mass_suspend" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['ids'] is not None:
            _body_params = _params['ids']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['privileges']  # noqa: E501

        _response_types_map = {
            '200': "MassResponse",
        }

        return self.api_client.call_api(
            '/subscriptions/massAction/_suspend', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @overload
    async def mass_terminate(self, ids : Ids, **kwargs) -> MassResponse:  # noqa: E501
        ...

    @overload
    def mass_terminate(self, ids : Ids, async_req: Optional[bool]=True, **kwargs) -> MassResponse:  # noqa: E501
        ...

    @validate_arguments
    def mass_terminate(self, ids : Ids, async_req: Optional[bool]=None, **kwargs) -> Union[MassResponse, Awaitable[MassResponse]]:  # noqa: E501
        """Terminate multiple subscriptions  # noqa: E501

        Terminate multiple subscriptions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.mass_terminate(ids, async_req=True)
        >>> result = thread.get()

        :param ids: (required)
        :type ids: Ids
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: MassResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the mass_terminate_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.mass_terminate_with_http_info(ids, **kwargs)  # noqa: E501

    @validate_arguments
    def mass_terminate_with_http_info(self, ids : Ids, **kwargs) -> ApiResponse:  # noqa: E501
        """Terminate multiple subscriptions  # noqa: E501

        Terminate multiple subscriptions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.mass_terminate_with_http_info(ids, async_req=True)
        >>> result = thread.get()

        :param ids: (required)
        :type ids: Ids
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(MassResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'ids'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method mass_terminate" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['ids'] is not None:
            _body_params = _params['ids']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['privileges']  # noqa: E501

        _response_types_map = {
            '200': "MassResponse",
        }

        return self.api_client.call_api(
            '/subscriptions/massAction/_terminate', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @overload
    async def mass_update(self, ids : Ids, version : Optional[constr(strict=True)] = None, confirm : Optional[StrictBool] = None, **kwargs) -> MassResponse:  # noqa: E501
        ...

    @overload
    def mass_update(self, ids : Ids, version : Optional[constr(strict=True)] = None, confirm : Optional[StrictBool] = None, async_req: Optional[bool]=True, **kwargs) -> MassResponse:  # noqa: E501
        ...

    @validate_arguments
    def mass_update(self, ids : Ids, version : Optional[constr(strict=True)] = None, confirm : Optional[StrictBool] = None, async_req: Optional[bool]=None, **kwargs) -> Union[MassResponse, Awaitable[MassResponse]]:  # noqa: E501
        """Update multiple subscriptions  # noqa: E501

        Update multiple subscriptions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.mass_update(ids, version, confirm, async_req=True)
        >>> result = thread.get()

        :param ids: (required)
        :type ids: Ids
        :param version:
        :type version: str
        :param confirm:
        :type confirm: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: MassResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the mass_update_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.mass_update_with_http_info(ids, version, confirm, **kwargs)  # noqa: E501

    @validate_arguments
    def mass_update_with_http_info(self, ids : Ids, version : Optional[constr(strict=True)] = None, confirm : Optional[StrictBool] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Update multiple subscriptions  # noqa: E501

        Update multiple subscriptions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.mass_update_with_http_info(ids, version, confirm, async_req=True)
        >>> result = thread.get()

        :param ids: (required)
        :type ids: Ids
        :param version:
        :type version: str
        :param confirm:
        :type confirm: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(MassResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'ids',
            'version',
            'confirm'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method mass_update" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('version') is not None:  # noqa: E501
            _query_params.append(('version', _params['version']))

        if _params.get('confirm') is not None:  # noqa: E501
            _query_params.append(('confirm', _params['confirm']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['ids'] is not None:
            _body_params = _params['ids']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['privileges']  # noqa: E501

        _response_types_map = {
            '200': "MassResponse",
        }

        return self.api_client.call_api(
            '/subscriptions/massAction/_update', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))