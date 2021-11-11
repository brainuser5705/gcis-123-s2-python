from hash import run_program

def test_hash():

    try:
        run_program()
        assert False
    except Exception:
        assert True

    
