# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package


def test_success():
    assert True


def test_encode():
    sample_text = "This is a sample text."
    import encoder
    passkey = encoder.encode_image(sample_text)
    return passkey


def test_decode(passkey):
    img_file = "output.png"
    import decoder
    text = decoder.decode_image(img_file, passkey)
    return text


def main():
    passkey = test_encode()
    text = test_decode(passkey)
    print text


if __name__ == "__main__":
    main()
