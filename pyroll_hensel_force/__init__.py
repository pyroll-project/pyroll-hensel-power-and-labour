from pyroll import RollPass
from pyroll.ui.exporter import Exporter
from pyroll.ui.report import Report

from . import specs
from . import impls

RollPass.plugin_manager.add_hookspecs(specs)
RollPass.plugin_manager.register(impls)

from . import report

Report.plugin_manager.register(report)

from . import export

Exporter.plugin_manager.register(export)