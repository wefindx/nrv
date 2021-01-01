import pytest

from nrv import validate

def test_none():
    result = None
    expect = None
    assert(result == expect)

def test_():
    versionless_batch_1 = [
        '0oo.li/Intent::v1/category',
        '0oo.li/Method::v1/method',
        '0oo.li/Project::v1/system:organization',
        '0oo.li/Result::v1/resource',
        '0oo.li/Operation::v1/request:order',
        '0oo.li/Tool::v1/method:equipment',
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
    triple_batch_4 = [
        '0oo.li/Trade::v1/resource:operation:contract',
    ]
    v2_test_5 = [
        '0oo.li/Location::v2/resource:location',
        '0oo.li/Location::v2/150',
    ]

    b1 = all([validate(name, include_top=True) for name in versionless_batch_1])
    b2 = all([validate(name, include_top=True) for name in versioned_batch_2])
    b3 = not all([validate(name, include_top=True) for name in failure_batch_3])
    b4 = all([validate(name, include_top=True) for name in triple_batch_4])
    b5 = all([validate(name) for name in v2_test_5])

    assert(b1 and b2 and b3 and b4 and b5)
