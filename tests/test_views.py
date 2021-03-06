""" Provide a set of tests cases to demonstrate a basic gui that meets
wasatch needs. This includes menu bar, buttons, and text controls. Verify that
logging from the views with default setup is available to the capturelog
fixture.
"""

import pytest

from PySide import QtCore, QtTest

from fastpm100 import views

@pytest.mark.skipif(pytest.config.getoption("--appveyor"),
                    reason="need --appveyor option to disable tests")
class TestStripChart:

    @pytest.fixture(scope="function")
    def strip_form(self, qtbot, request):
        """ Create the view at every setup, close it on final.
        """
        new_form = views.StripWindow()

        def form_close():
            new_form.close()
        request.addfinalizer(form_close)

        return new_form

    def test_form_has_default_setup(self, strip_form, qtbot):
        assert strip_form.ui.labelMinimum.text() == "0.0"
        assert strip_form.width() >= 900
        assert strip_form.height() >= 318

    def test_form_has_pyqtgraph_widget(self, strip_form, qtbot):
        assert strip_form.ui.plot.width() >= 700
        assert strip_form.ui.plot.height() >= 300

    def test_form_has_toolbar_action_buttons(self, strip_form, qtbot):
        strip_wfo = strip_form.ui.toolBar.widgetForAction
        widget = strip_wfo(strip_form.ui.actionPause)
        assert widget.width() >= 24
        assert widget.height() >= 24

        widget = strip_wfo(strip_form.ui.actionContinue)
        assert widget.width() >= 24
        assert widget.height() >= 24



@pytest.mark.skipif(pytest.config.getoption("--appveyor"),
                    reason="need --appveyor option to disable tests")
class TestBlueGraphSkin:

    @pytest.fixture(scope="function")
    def strip_form(self, qtbot, request):
        """ Create the view at every setup, close it on final.
        """
        new_form = views.BlueGraphStripChart()

        def form_close():
            new_form.close()
        request.addfinalizer(form_close)

        return new_form

    def test_form_has_default_setup(self, strip_form, qtbot):
        assert strip_form.ui.labelMinimum.text() == "0.0"
        assert strip_form.width() >= 900
        assert strip_form.height() >= 318

    def test_form_has_pyqtgraph_widget(self, strip_form, qtbot):
        assert strip_form.ui.plot.width() >= 700
        assert strip_form.ui.plot.height() >= 300

    def test_form_has_toolbar_action_buttons(self, strip_form, qtbot):
        strip_wfo = strip_form.ui.toolBar.widgetForAction
        widget = strip_wfo(strip_form.ui.actionPause)
        assert widget.width() >= 24
        assert widget.height() >= 24

        widget = strip_wfo(strip_form.ui.actionContinue)
        assert widget.width() >= 24
        assert widget.height() >= 24

""" Enablement of this test group will fail on travis, but not on local with message:
      File "/home/travis/build/WasatchPhotonics/FastPM100/fastpm100/control.py",
      line 530, in update_history self.render_graph() File
      "/home/travis/build/WasatchPhotonics/FastPM100/fastpm100/control.py", line
      544, in render_graph curve.setData(self.hist[2]) File
      "/home/travis/mc/envs/test_env/lib/python2.7/site-packages/pyqtgraph-0.9.10-py2.7.egg/pyqtgraph/graphicsItems/PlotDataItem.py",
      line 460, in setData self.updateItems() File
      "/home/travis/mc/envs/test_env/lib/python2.7/site-packages/pyqtgraph-0.9.10-py2.7.egg/pyqtgraph/graphicsItems/PlotDataItem.py",
      line 486, in updateItems self.curve.setData(x=x, y=y, **curveArgs) File
      "/home/travis/mc/envs/test_env/lib/python2.7/site-packages/pyqtgraph-0.9.10-py2.7.egg/pyqtgraph/graphicsItems/PlotCurveItem.py",
      line 299, in setData self.updateData(*args, **kargs) File
      "/home/travis/mc/envs/test_env/lib/python2.7/site-packages/pyqtgraph-0.9.10-py2.7.egg/pyqtgraph/graphicsItems/PlotCurveItem.py",
      line 330, in updateData self.prepareGeometryChange() RuntimeError:
          Internal C++ object (PlotCurveItem) already deleted.
"""
#class TestAllStripWindow:
#
#    @pytest.fixture(scope="function")
#    def strip_form(self, qtbot, request):
#        """ Create the view at every setup, close it on final.
#        """
#        # x, y, w, h
#        geometry = [100, 100, 920, 433]
#        new_form = views.AllStripWindow(geometry=geometry)
#
#        def form_close():
#            new_form.close()
#        request.addfinalizer(form_close)
#
#        return new_form
#
#    def test_form_has_default_setup(self, strip_form, qtbot):
#        assert strip_form.ui.labelMinimum.text() == "0.0"
#        assert strip_form.width() >= 900
#        assert strip_form.height() >= 318
#
#        qtbot.wait(3000)

