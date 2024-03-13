#pytest

def func(x):
    return x + 1

def test_func():
    assert func(3) == 5

def run_tests():
    results = {
        "pass": 0,
        "fail": 0,
        "error": 0
    }

    for (name, test) in globals().items():
        if not name.startswith("test_"):
            continue
        try:
            test()
            results["pass"] +=1
        except AssertionError:
            results["fail"] +=1 
        except Exception:
            results["error"] +=1

    print(f"pass {results['pass']}")
    print(f'fail {results['fail']}')
    print(f'error {results['error']}')


def main():
    run_tests()


if  __name__ == "__main__":
    main()