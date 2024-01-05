import test2

def test_submit():
    assert(test2.client.submit("hello", "world"), "hello world")
