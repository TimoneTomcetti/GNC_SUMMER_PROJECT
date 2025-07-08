import nox

@nox.session(reuse_venv=True)
def test_time(session):
    session.install("-r", "requirements-test.txt")
    session.run("pytest", "tests/test_core/test_time.py")
    session.run("pylint", "src/core/time.py")

@nox.session(reuse_venv=True)
def coverage_test(session):
    session.install("-r", "requirements-test.txt")
    session.run("coverage", "run", "-m", "pytest", "tests")
    session.run("coverage", "report", "-m")
    session.run("coverage", "html")