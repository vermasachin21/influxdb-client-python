# coding: utf-8

"""
    Influx API Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BucketRetentionRules(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'type': 'str',
        'every_seconds': 'int'
    }

    attribute_map = {
        'type': 'type',
        'every_seconds': 'everySeconds'
    }

    def __init__(self, type='expire', every_seconds=None):  # noqa: E501
        """BucketRetentionRules - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._every_seconds = None
        self.discriminator = None

        self.type = type
        self.every_seconds = every_seconds

    @property
    def type(self):
        """Gets the type of this BucketRetentionRules.  # noqa: E501


        :return: The type of this BucketRetentionRules.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BucketRetentionRules.


        :param type: The type of this BucketRetentionRules.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def every_seconds(self):
        """Gets the every_seconds of this BucketRetentionRules.  # noqa: E501

        duration in seconds for how long data will be kept in the database.  # noqa: E501

        :return: The every_seconds of this BucketRetentionRules.  # noqa: E501
        :rtype: int
        """
        return self._every_seconds

    @every_seconds.setter
    def every_seconds(self, every_seconds):
        """Sets the every_seconds of this BucketRetentionRules.

        duration in seconds for how long data will be kept in the database.  # noqa: E501

        :param every_seconds: The every_seconds of this BucketRetentionRules.  # noqa: E501
        :type: int
        """
        if every_seconds is None:
            raise ValueError("Invalid value for `every_seconds`, must not be `None`")  # noqa: E501
        if every_seconds is not None and every_seconds < 1:  # noqa: E501
            raise ValueError("Invalid value for `every_seconds`, must be a value greater than or equal to `1`")  # noqa: E501

        self._every_seconds = every_seconds

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BucketRetentionRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
