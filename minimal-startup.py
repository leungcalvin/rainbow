from pychfpga import fpga_array
ca = fpga_array.FPGAArray(iceboards=['10.0.2.1', '10.0.2.2', '10.0.2.3', '10.0.2.4'], bitfile='/home/masuilab/pychfpga/pychfpga/fpga_bitstreams/chFPGA_MGK7MB_Rev2.bit', open=1,prog=1, stderr_log_level='debug', log_target='stream', log_level='debug')
for s, ib in enumerate(ca.ib):
    ib.slot = s
ca.ib.set_data_source('funcgen')
ca.ib.set_funcgen_function('ramp')
ca.ib.set_user_output_source('input', 'sma_a')
ca.set_sync_method(method='distributed_time', source='sma_a')
ca.set_operational_mode('shuffle16',frames_per_packet=2)
