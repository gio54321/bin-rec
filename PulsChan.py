#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Pulsar Channelizer
# Author: IW5BHY
# Generated: Wed Apr 26 17:57:43 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from optparse import OptionParser
import osmosdr
import sip
import sys
import time
import os
from gnuradio import qtgui


class PulsChan(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Pulsar Channelizer")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Pulsar Channelizer")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "PulsChan")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.scale = scale = float(sys.argv[7])
        self.samp_rate = samp_rate = float(sys.argv[2])
        self.filename = filename = sys.argv[8]
        self.fft_size = fft_size = int(sys.argv[5])
        self.decimation = decimation = int(sys.argv[6])
        self.RFGain = RFGain = float(sys.argv[4])
        self.IFGain = IFGain = 12
        self.n_buffer = n_buffer = 26000
        self.Freq = Freq = float(sys.argv[3])
        self.ACQ_TIME = ACQ_TIME = int(sys.argv[1])
        print(len(sys.argv))
        print(ACQ_TIME)
        print(samp_rate)
        print(Freq)		
        print(RFGain)		
        print(fft_size)		
        print(decimation)
        print(scale)
        print(filename)
		
        ##################################################
        # Blocks
        ##################################################
        self.qtgui_vector_sink_f_0 = qtgui.vector_sink_f(
            fft_size/decimation,
            0,
            1,
            "CH",
            "POWER",
            "",
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0.set_update_time(0.2)
        self.qtgui_vector_sink_f_0.set_y_axis(0, 32767)
        self.qtgui_vector_sink_f_0.enable_autoscale(False)
        self.qtgui_vector_sink_f_0.enable_grid(True)
        self.qtgui_vector_sink_f_0.set_x_axis_units("")
        self.qtgui_vector_sink_f_0.set_y_axis_units("")
        self.qtgui_vector_sink_f_0.set_ref_level(0)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_vector_sink_f_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0.set_line_alpha(i, alphas[i])

        self._qtgui_vector_sink_f_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_vector_sink_f_0_win)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	fft_size, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.20)
        self.qtgui_const_sink_x_0.set_y_axis(-1, 1)
        self.qtgui_const_sink_x_0.set_x_axis(-1, 1)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_win)
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_source_0.set_clock_source('internal', 0)
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(Freq*1e6, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(RFGain, 0)
        self.osmosdr_source_0.set_if_gain(IFGain, 0)
        self.osmosdr_source_0.set_bb_gain(0, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
        self.osmosdr_source_0.set_min_output_buffer(n_buffer)

        self.fft_vxx_0 = fft.fft_vcc(fft_size, True, (window.rectangular(fft_size)), True, 1)
        self.fft_vxx_0.set_min_output_buffer(n_buffer)
        
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, fft_size)
        self.blocks_vector_to_stream_0.set_min_output_buffer(n_buffer)
        
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_float*1, fft_size/decimation)
        self.blocks_stream_to_vector_0_0.set_min_output_buffer(n_buffer)
        
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, fft_size)
        self.blocks_stream_to_vector_0.set_min_output_buffer(n_buffer)
        
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 1)
        self.blocks_short_to_float_0.set_min_output_buffer(n_buffer)

        
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((1000/decimation, ))
        self.blocks_short_to_float_0.set_min_output_buffer(n_buffer)
        
        self.blocks_integrate_xx_0 = blocks.integrate_ff(decimation, 1)
        self.blocks_integrate_xx_0.set_min_output_buffer(n_buffer)
        
        self.blocks_float_to_short_0 = blocks.float_to_short(1, scale)
        self.blocks_float_to_short_0.set_min_output_buffer(n_buffer)
        
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_short*1, filename, False)
        self.blocks_file_sink_0.set_min_output_buffer(n_buffer)
        
        self.blocks_file_sink_0.set_unbuffered(False)
        
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.blocks_complex_to_mag_0.set_min_output_buffer(n_buffer)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_integrate_xx_0, 0))
        self.connect((self.blocks_float_to_short_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_float_to_short_0, 0), (self.blocks_short_to_float_0, 0))
        self.connect((self.blocks_integrate_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_float_to_short_0, 0))
        self.connect((self.blocks_short_to_float_0, 0), (self.blocks_stream_to_vector_0_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.qtgui_vector_sink_f_0, 0))
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_complex_to_mag_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_vector_to_stream_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.qtgui_const_sink_x_0, 0))

        self.start(10000000)
        import threading
        threading.Timer(ACQ_TIME, self.kill_process).start()
        
    def kill_process(self):
        self.stop()
        self.wait()	
        time.sleep(2)		
        os._exit(0)

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "PulsChan")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_scale(self):
        return self.scale

    def set_scale(self, scale):
        self.scale = scale
        self.blocks_float_to_short_0.set_scale(self.scale)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)

    def get_filename(self):
        return self.filename

    def set_filename(self, filename):
        self.filename = filename
        self.blocks_file_sink_0.open(self.filename)

    def get_fft_size(self):
        return self.fft_size

    def set_fft_size(self, fft_size):
        self.fft_size = fft_size

    def get_decimation(self):
        return self.decimation

    def set_decimation(self, decimation):
        self.decimation = decimation
        self.blocks_multiply_const_vxx_0.set_k((1000/self.decimation, ))

    def get_RFGain(self):
        return self.RFGain

    def set_RFGain(self, RFGain):
        self.RFGain = RFGain
        self.osmosdr_source_0.set_gain(self.RFGain, 0)

    def get_IFGain(self):
        return self.IFGain

    def set_IFGain(self, IFGain):
        self.IFGain = IFGain
        self.osmosdr_source_0.set_if_gain(self.IFGain, 0)

    def get_Freq(self):
        return self.Freq

    def set_Freq(self, Freq):
        self.Freq = Freq
        self.osmosdr_source_0.set_center_freq(self.Freq*1e6, 0)

    def get_ACQ_TIME(self):
        return self.ACQ_TIME

    def set_ACQ_TIME(self, ACQ_TIME):
        self.ACQ_TIME = ACQ_TIME


def main(top_block_cls=PulsChan, options=None):
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable real-time scheduling."

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
