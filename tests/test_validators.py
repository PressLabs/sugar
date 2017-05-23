import pytest

from django.core.exceptions import ValidationError
from pl_sugar import validators


def test_validate_dns_label():
    validators.validate_dns_label('a-a')
    validators.validate_dns_label('test-me-with-multiple-dashes')
    validators.validate_dns_label('123test-numbers')

    with pytest.raises(ValidationError):
        validators.validate_dns_label('multi--dash')

    with pytest.raises(ValidationError):
        validators.validate_dns_label('1234')

    with pytest.raises(ValidationError):
        validators.validate_dns_label('-leading-dash')

    with pytest.raises(ValidationError):
        validators.validate_dns_label('trailing-dash-')
