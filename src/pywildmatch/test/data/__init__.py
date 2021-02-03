
# VALIDATE DATA AND RETURN VALUES BY INDEX
def validate_data(dataset):
    r = lambda: repr(dataset)
    assert len(dataset) == 3, r()
    pattern, text, results = dataset[0], dataset[1], dataset[2]
    assert isinstance(pattern, (bytes,str)), r()
    assert isinstance(text, (bytes,str)), r()
    assert isinstance(results, dict), r()
    assert len(results) == 3, r()
    for result_name in results:
        expected = results[result_name]
        assert isinstance(expected, tuple), r()
        # max_flag
        if result_name == 'python_fnmatch':
            assert len(expected) == 2, r()
        elif result_name == 'libgit2':
            assert len(expected) == 4, r()
        elif result_name == 'pywildmatch':
            assert len(expected) == 6, r()
        else:
            print(r())
            print(result_name, 'has wrong number of flags', expected)
            raise Exception()
        for x in expected:
            assert x in (0,1), r()
    return pattern, text, results

