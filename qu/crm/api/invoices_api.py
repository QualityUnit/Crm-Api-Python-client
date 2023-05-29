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

from pydantic import Field, StrictInt, StrictStr

from typing import Any, Dict, List, Optional, Union

from qu.crm.models.invoice import Invoice
from qu.crm.models.refund import Refund
from qu.crm.models.refund_request import RefundRequest

from qu.crm.api_client import ApiClient
from qu.crm.api_response import ApiResponse
from qu.crm.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class InvoicesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @overload
    async def download_invoice(self, invoice_number : StrictStr, **kwargs) -> bytearray:  # noqa: E501
        ...

    @overload
    def download_invoice(self, invoice_number : StrictStr, async_req: Optional[bool]=True, **kwargs) -> bytearray:  # noqa: E501
        ...

    @validate_arguments
    def download_invoice(self, invoice_number : StrictStr, async_req: Optional[bool]=None, **kwargs) -> Union[bytearray, Awaitable[bytearray]]:  # noqa: E501
        """Download invoice  # noqa: E501

        Download invoice  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.download_invoice(invoice_number, async_req=True)
        >>> result = thread.get()

        :param invoice_number: (required)
        :type invoice_number: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: bytearray
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the download_invoice_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.download_invoice_with_http_info(invoice_number, **kwargs)  # noqa: E501

    @validate_arguments
    def download_invoice_with_http_info(self, invoice_number : StrictStr, **kwargs) -> ApiResponse:  # noqa: E501
        """Download invoice  # noqa: E501

        Download invoice  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.download_invoice_with_http_info(invoice_number, async_req=True)
        >>> result = thread.get()

        :param invoice_number: (required)
        :type invoice_number: str
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
        :rtype: tuple(bytearray, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'invoice_number'
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
                    " to method download_invoice" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['invoice_number']:
            _path_params['invoiceNumber'] = _params['invoice_number']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/pdf'])  # noqa: E501

        # authentication setting
        _auth_settings = ['privileges']  # noqa: E501

        _response_types_map = {
            '200': "bytearray",
        }

        return self.api_client.call_api(
            '/invoices/{invoiceNumber}/_download', 'GET',
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
    async def get_invoice(self, invoice_number : StrictStr, **kwargs) -> Invoice:  # noqa: E501
        ...

    @overload
    def get_invoice(self, invoice_number : StrictStr, async_req: Optional[bool]=True, **kwargs) -> Invoice:  # noqa: E501
        ...

    @validate_arguments
    def get_invoice(self, invoice_number : StrictStr, async_req: Optional[bool]=None, **kwargs) -> Union[Invoice, Awaitable[Invoice]]:  # noqa: E501
        """Invoice  # noqa: E501

        Returns invoice  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_invoice(invoice_number, async_req=True)
        >>> result = thread.get()

        :param invoice_number: (required)
        :type invoice_number: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Invoice
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_invoice_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.get_invoice_with_http_info(invoice_number, **kwargs)  # noqa: E501

    @validate_arguments
    def get_invoice_with_http_info(self, invoice_number : StrictStr, **kwargs) -> ApiResponse:  # noqa: E501
        """Invoice  # noqa: E501

        Returns invoice  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_invoice_with_http_info(invoice_number, async_req=True)
        >>> result = thread.get()

        :param invoice_number: (required)
        :type invoice_number: str
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
        :rtype: tuple(Invoice, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'invoice_number'
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
                    " to method get_invoice" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['invoice_number']:
            _path_params['invoiceNumber'] = _params['invoice_number']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['privileges']  # noqa: E501

        _response_types_map = {
            '200': "Invoice",
        }

        return self.api_client.call_api(
            '/invoices/{invoiceNumber}', 'GET',
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
    async def get_invoices(self, page : Annotated[Optional[StrictInt], Field(description="Page to display. Used only if _from is not defined.")] = None, per_page : Annotated[Optional[StrictInt], Field(description="Results per page. Used only if _page is used.")] = None, sort_dir : Annotated[Optional[StrictStr], Field(description="Sorting direction ASC or DESC")] = None, sort_field : Annotated[Optional[StrictStr], Field(description="Sorting field")] = None, filters : Annotated[Optional[StrictStr], Field(description="Filters (json object {column:value, ...})")] = None, var_from : Annotated[Optional[StrictInt], Field(description="Result set start. Takes precedence over _page if defined.")] = None, to : Annotated[Optional[StrictInt], Field(description="Result set end. Used only if _from is used.")] = None, **kwargs) -> List[Invoice]:  # noqa: E501
        ...

    @overload
    def get_invoices(self, page : Annotated[Optional[StrictInt], Field(description="Page to display. Used only if _from is not defined.")] = None, per_page : Annotated[Optional[StrictInt], Field(description="Results per page. Used only if _page is used.")] = None, sort_dir : Annotated[Optional[StrictStr], Field(description="Sorting direction ASC or DESC")] = None, sort_field : Annotated[Optional[StrictStr], Field(description="Sorting field")] = None, filters : Annotated[Optional[StrictStr], Field(description="Filters (json object {column:value, ...})")] = None, var_from : Annotated[Optional[StrictInt], Field(description="Result set start. Takes precedence over _page if defined.")] = None, to : Annotated[Optional[StrictInt], Field(description="Result set end. Used only if _from is used.")] = None, async_req: Optional[bool]=True, **kwargs) -> List[Invoice]:  # noqa: E501
        ...

    @validate_arguments
    def get_invoices(self, page : Annotated[Optional[StrictInt], Field(description="Page to display. Used only if _from is not defined.")] = None, per_page : Annotated[Optional[StrictInt], Field(description="Results per page. Used only if _page is used.")] = None, sort_dir : Annotated[Optional[StrictStr], Field(description="Sorting direction ASC or DESC")] = None, sort_field : Annotated[Optional[StrictStr], Field(description="Sorting field")] = None, filters : Annotated[Optional[StrictStr], Field(description="Filters (json object {column:value, ...})")] = None, var_from : Annotated[Optional[StrictInt], Field(description="Result set start. Takes precedence over _page if defined.")] = None, to : Annotated[Optional[StrictInt], Field(description="Result set end. Used only if _from is used.")] = None, async_req: Optional[bool]=None, **kwargs) -> Union[List[Invoice], Awaitable[List[Invoice]]]:  # noqa: E501
        """Invoice list  # noqa: E501

        Returns list of invoices  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_invoices(page, per_page, sort_dir, sort_field, filters, var_from, to, async_req=True)
        >>> result = thread.get()

        :param page: Page to display. Used only if _from is not defined.
        :type page: int
        :param per_page: Results per page. Used only if _page is used.
        :type per_page: int
        :param sort_dir: Sorting direction ASC or DESC
        :type sort_dir: str
        :param sort_field: Sorting field
        :type sort_field: str
        :param filters: Filters (json object {column:value, ...})
        :type filters: str
        :param var_from: Result set start. Takes precedence over _page if defined.
        :type var_from: int
        :param to: Result set end. Used only if _from is used.
        :type to: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[Invoice]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_invoices_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.get_invoices_with_http_info(page, per_page, sort_dir, sort_field, filters, var_from, to, **kwargs)  # noqa: E501

    @validate_arguments
    def get_invoices_with_http_info(self, page : Annotated[Optional[StrictInt], Field(description="Page to display. Used only if _from is not defined.")] = None, per_page : Annotated[Optional[StrictInt], Field(description="Results per page. Used only if _page is used.")] = None, sort_dir : Annotated[Optional[StrictStr], Field(description="Sorting direction ASC or DESC")] = None, sort_field : Annotated[Optional[StrictStr], Field(description="Sorting field")] = None, filters : Annotated[Optional[StrictStr], Field(description="Filters (json object {column:value, ...})")] = None, var_from : Annotated[Optional[StrictInt], Field(description="Result set start. Takes precedence over _page if defined.")] = None, to : Annotated[Optional[StrictInt], Field(description="Result set end. Used only if _from is used.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Invoice list  # noqa: E501

        Returns list of invoices  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_invoices_with_http_info(page, per_page, sort_dir, sort_field, filters, var_from, to, async_req=True)
        >>> result = thread.get()

        :param page: Page to display. Used only if _from is not defined.
        :type page: int
        :param per_page: Results per page. Used only if _page is used.
        :type per_page: int
        :param sort_dir: Sorting direction ASC or DESC
        :type sort_dir: str
        :param sort_field: Sorting field
        :type sort_field: str
        :param filters: Filters (json object {column:value, ...})
        :type filters: str
        :param var_from: Result set start. Takes precedence over _page if defined.
        :type var_from: int
        :param to: Result set end. Used only if _from is used.
        :type to: int
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
        :rtype: tuple(List[Invoice], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'page',
            'per_page',
            'sort_dir',
            'sort_field',
            'filters',
            'var_from',
            'to'
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
                    " to method get_invoices" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('page') is not None:  # noqa: E501
            _query_params.append(('_page', _params['page']))

        if _params.get('per_page') is not None:  # noqa: E501
            _query_params.append(('_perPage', _params['per_page']))

        if _params.get('sort_dir') is not None:  # noqa: E501
            _query_params.append(('_sortDir', _params['sort_dir'].value))

        if _params.get('sort_field') is not None:  # noqa: E501
            _query_params.append(('_sortField', _params['sort_field']))

        if _params.get('filters') is not None:  # noqa: E501
            _query_params.append(('_filters', _params['filters']))

        if _params.get('var_from') is not None:  # noqa: E501
            _query_params.append(('_from', _params['var_from']))

        if _params.get('to') is not None:  # noqa: E501
            _query_params.append(('_to', _params['to']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['privileges']  # noqa: E501

        _response_types_map = {
            '200': "List[Invoice]",
        }

        return self.api_client.call_api(
            '/invoices', 'GET',
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
    async def refund_invoice(self, invoice_number : StrictStr, refund : RefundRequest, **kwargs) -> Refund:  # noqa: E501
        ...

    @overload
    def refund_invoice(self, invoice_number : StrictStr, refund : RefundRequest, async_req: Optional[bool]=True, **kwargs) -> Refund:  # noqa: E501
        ...

    @validate_arguments
    def refund_invoice(self, invoice_number : StrictStr, refund : RefundRequest, async_req: Optional[bool]=None, **kwargs) -> Union[Refund, Awaitable[Refund]]:  # noqa: E501
        """Refund invoice  # noqa: E501

        Refund invoice  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.refund_invoice(invoice_number, refund, async_req=True)
        >>> result = thread.get()

        :param invoice_number: (required)
        :type invoice_number: str
        :param refund: (required)
        :type refund: RefundRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Refund
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the refund_invoice_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.refund_invoice_with_http_info(invoice_number, refund, **kwargs)  # noqa: E501

    @validate_arguments
    def refund_invoice_with_http_info(self, invoice_number : StrictStr, refund : RefundRequest, **kwargs) -> ApiResponse:  # noqa: E501
        """Refund invoice  # noqa: E501

        Refund invoice  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.refund_invoice_with_http_info(invoice_number, refund, async_req=True)
        >>> result = thread.get()

        :param invoice_number: (required)
        :type invoice_number: str
        :param refund: (required)
        :type refund: RefundRequest
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
        :rtype: tuple(Refund, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'invoice_number',
            'refund'
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
                    " to method refund_invoice" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['invoice_number']:
            _path_params['invoiceNumber'] = _params['invoice_number']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['refund'] is not None:
            _body_params = _params['refund']

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
            '200': "Refund",
        }

        return self.api_client.call_api(
            '/invoices/{invoiceNumber}/_refund', 'POST',
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
    async def regenerate_invoice(self, invoice_number : StrictStr, **kwargs) -> object:  # noqa: E501
        ...

    @overload
    def regenerate_invoice(self, invoice_number : StrictStr, async_req: Optional[bool]=True, **kwargs) -> object:  # noqa: E501
        ...

    @validate_arguments
    def regenerate_invoice(self, invoice_number : StrictStr, async_req: Optional[bool]=None, **kwargs) -> Union[object, Awaitable[object]]:  # noqa: E501
        """Regenerate invoice pdf  # noqa: E501

        Regenerate invoice pdf  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.regenerate_invoice(invoice_number, async_req=True)
        >>> result = thread.get()

        :param invoice_number: (required)
        :type invoice_number: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the regenerate_invoice_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.regenerate_invoice_with_http_info(invoice_number, **kwargs)  # noqa: E501

    @validate_arguments
    def regenerate_invoice_with_http_info(self, invoice_number : StrictStr, **kwargs) -> ApiResponse:  # noqa: E501
        """Regenerate invoice pdf  # noqa: E501

        Regenerate invoice pdf  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.regenerate_invoice_with_http_info(invoice_number, async_req=True)
        >>> result = thread.get()

        :param invoice_number: (required)
        :type invoice_number: str
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
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'invoice_number'
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
                    " to method regenerate_invoice" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['invoice_number']:
            _path_params['invoiceNumber'] = _params['invoice_number']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['privileges']  # noqa: E501

        _response_types_map = {
            '200': "object",
        }

        return self.api_client.call_api(
            '/invoices/{invoiceNumber}/_regenerate_pdf', 'POST',
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