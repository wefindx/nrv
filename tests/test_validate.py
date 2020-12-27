import pytest

from nrv import validate_name

def test_none():
    result = None
    expect = None
    assert(result == expect)

def test_():
    versionless_batch_1 = [
        '0oo.li/Intent::category',
        '0oo.li/Method::method',
        '0oo.li/Project::system:organization',
        '0oo.li/Result::resource',
        '0oo.li/Operation::request:order',
        '0oo.li/Tool::method:equipment',
    ]
    versioned_batch_2 = [
        '0oo.li/Place::v1/location',
        '0oo.li/Event::v1/resource:record',
        '0oo.li/Comment::v1/resource:record',
        '0oo.li/Product::v1/resource:method',
    ]
    failure_batch_3 = [
        '0oo.li/Order::v2/request:order',
        '0oo.li/Trade::v3/resource:record',
        '0oo.li/Person::v2/system:person'
    ]

    b1 = all([validate_name(name) for name in versionless_batch_1])
    b2 = all([validate_name(name) for name in versioned_batch_2])
    b3 = not all([validate_name(name) for name in failure_batch_3])

    assert(b1 and b2 and b3)
