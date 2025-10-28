from ft_filter import ft_filter


def test_ft_filter_docstring_exists():
    """check that ft_filter function has a docstring."""
    assert ft_filter.__doc__ is not None, \
        "ft_filter function is missing a docstring."


def test_ft_filter_docstring_content():
    """check that ft_filter function docstring matches expected content."""
    # remove leading/trailing whitespace for accurate comparison
    actual_doc = ft_filter.__doc__.strip()
    expected_doc = filter.__doc__.strip()

    assert actual_doc == expected_doc, (
        "ft_filter docstring content mismatch.\n"
        f"Expected:\n{expected_doc}\n\n"
        f"Actual:\n{actual_doc}"
    )
