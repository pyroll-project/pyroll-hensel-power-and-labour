import logging
import webbrowser
from pathlib import Path

from pyroll.core import Profile, Roll, ThreeRollPass, Transport, RoundGroove, CircularOvalGroove, PassSequence, \
    root_hooks


def test_solve3(tmp_path: Path, caplog):
    caplog.set_level(logging.DEBUG, logger="pyroll")

    import pyroll.hensel_force_torque

    in_profile = Profile.round(
        diameter=55e-3,
        temperature=1200 + 273.15,
        strain=0,
        material=["C45", "steel"],
        flow_stress=100e6,
        length=1,
    )

    sequence = PassSequence([
        ThreeRollPass(
            label="Oval I",
            roll=Roll(
                groove=CircularOvalGroove(
                    depth=8e-3,
                    r1=6e-3,
                    r2=40e-3,
                    pad_angle=30,
                ),
                nominal_radius=160e-3,
                rotational_frequency=1
            ),
            gap=2e-3,
        ),
        Transport(
            label="I => II",
            duration=1
        ),
        ThreeRollPass(
            label="Round II",
            roll=Roll(
                groove=RoundGroove(
                    r1=3e-3,
                    r2=25e-3,
                    depth=11e-3,
                    pad_angle=30,
                ),
                nominal_radius=160e-3,
                rotational_frequency=1
            ),
            gap=2e-3,
        ),
    ])

    try:
        sequence.solve(in_profile)
    finally:
        print("\nLog:")
        print(caplog.text)

    try:
        from pyroll.report import report

        report = report(sequence)
        f = tmp_path / "report.html"
        f.write_text(report, encoding="utf-8")
        webbrowser.open(f.as_uri())

    except ImportError:
        pass

    assert sequence[0].has_cached("deformation_resistance")
    assert sequence[0].has_cached("lever_arm_coefficient")
