def test_import_kuberentes():
    """Tests each generated kubernetes library can import"""
    from gybe import kubernetes
    assert kubernetes
