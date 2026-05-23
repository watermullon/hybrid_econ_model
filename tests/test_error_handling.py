from run_model import main


class FakeScenarioSet:
    scenarios = {}


def test_run_model_reports_locked_output_file(monkeypatch) -> None:
    def raise_permission_error(*args, **kwargs):
        raise PermissionError("locked file")

    monkeypatch.setattr("run_model.load_inputs", lambda input_dir: (object(), FakeScenarioSet(), None))
    monkeypatch.setattr("run_model.run_all_scenarios", lambda config, scenarios, deals: [])
    monkeypatch.setattr("run_model.write_outputs", raise_permission_error)

    try:
        main()
    except SystemExit as exc:
        message = str(exc)
    else:
        raise AssertionError("main() should exit when output files are locked")

    assert "close it and run python run_model.py again" in message
