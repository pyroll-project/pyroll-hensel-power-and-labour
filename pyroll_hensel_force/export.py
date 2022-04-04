from pyroll import RollPass
from pyroll.ui.exporter import Exporter
from pyroll.utils import applies_to_unit_types


@Exporter.hookimpl
@applies_to_unit_types(RollPass)
def columns(unit: RollPass):
    return dict(
        roll_gap_ratio=f"{unit.roll_gap_ratio:.2f}",
        deformation_resistance=f"{unit.deformation_resistance:.4g}",
        lever_arm_coefficient=f"{unit.lever_arm_coefficient:.2f}",
        rolling_efficiency=f"{unit.rolling_efficiency:.2f}"
    )