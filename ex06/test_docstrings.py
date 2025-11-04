from ft_filter import ft_filter


def test_ft_filter_docstring_exists():
    assert ft_filter.__doc__ is not None, \
        "ft_filter function is missing a docstring."


def test_ft_filter_docstring_content():
    actual_doc = ft_filter.__doc__.strip()
    expected_doc = filter.__doc__.strip()

    assert actual_doc == expected_doc, (
        "ft_filter docstring content mismatch.\n"
        f"Expected:\n{expected_doc}\n\n"
        f"Actual:\n{actual_doc}"
    )
