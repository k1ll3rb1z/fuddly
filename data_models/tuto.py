import sys
sys.path.append('.')

from fuzzfmk.plumbing import *

from fuzzfmk.data_model import *
from fuzzfmk.value_types import *
from fuzzfmk.data_model_helpers import *

class MyDF_DataModel(DataModel):

    file_extension = 'df'
    name = 'mydf'

    def absorb(self, data, idx):
        pass

    def build_data_model(self):

        test_node_desc = \
        {'name': 'TestNode',
         'contents': [
             # block 1
             {'section_type': MH.Ordered,
              'duplicate_mode': MH.Copy,
              'contents': [
                  
                  {'contents': BitField(subfield_sizes=[21,2,1], endian=VT.BigEndian,
                                        subfield_val_lists=[None, [0b10], [0,1]],
                                        subfield_val_extremums=[[500, 600], None, None]),
                   'name': 'val1',
                   'qty': (1, 5)},
                  
                  {'name': 'val2'},
                  
                  {'name': 'middle',
                   'mode': MH.NotMutableClone,
                   'separator': {'contents': {'name': 'sep',
                                              'contents': String(val_list=['\n'], absorb_regexp=b'\n+'),
                                              'absorb_csts': AbsNoCsts(regexp=True)}},
                   'contents': [{
                       'section_type': MH.Random,
                       'contents': [
                           
                           {'contents': String(val_list=['OK', 'KO'], size=2),
                            'name': 'val2',
                            'qty': (1, 3)},
                           
                           {'name': 'val21',
                            'clone': 'val1'},
                           
                           {'name': 'USB_desc',
                            'export_from': 'usb',
                            'data_id': 'STR'},
                           
                           {'type': MH.Generator,
                            'contents': lambda x: Node('cts', values=[x[0].to_bytes() \
                                                                      + x[1].to_bytes()]),
                            'name': 'val22',
                            'node_args': [('val21', 2), 'val3']}
                       ]}]},
                  
                  {'contents': String(max_sz = 10),
                   'name': 'val3',
                   'sync_qty_with': 'val1',
                   'alt': [
                       {'conf': 'alt1',
                        'contents': SINT8(int_list=[1,4,8])},
                       {'conf': 'alt2',
                        'contents': UINT16_be(mini=0xeeee, maxi=0xff56),
                        'determinist': True}]}
              ]},
             
             # block 2
             {'section_type': MH.Pick,
              'weights': (10,5),
              'contents': [
                  {'contents': String(val_list=['PLIP', 'PLOP'], size=4),
                   'name': 'val4'},
                  
                  {'contents': SINT16_be(int_list=[-1, -3, -5, 7]),
                   'name': 'val5'}
              ]},
            
             # block 3
             {'section_type': MH.FullyRandom,
              'contents': [
                  {'contents': String(val_list=['AAA', 'BBBB', 'CCCCC']),
                   'name': ('val21', 2)},
                  
                  {'contents': UINT8(int_list=[2, 4, 6, 8]),
                   'qty': (2, 3),
                   'name': ('val22', 2)}
              ]}
         ]}


        def keycode_helper(blob, constraints, node_internals):
            off = blob.find(b'\xd2')
            if off > -1:
                return AbsorbStatus.Accept, off, None
            else:
                return AbsorbStatus.Reject, 0, None

        abstest_desc = \
        {'name': 'AbsTest',
         'contents': [

             {'name': 'prefix',
              'contents': UINT8(int_list=[0xcc, 0xff, 0xee])},

             {'name': 'variable_string',
              'contents': String(max_sz=20),
              'set_attrs': [NodeInternals.Abs_Postpone]},

             {'name': 'keycode',
              'contents': UINT16_be(int_list=[0xd2d3, 0xd2fe, 0xd2aa]),
              'absorb_helper': keycode_helper},

             {'name': 'variable_suffix',
              'contents': String(val_list=['END', 'THE_END'])}
         ]}


        abstest2_desc = \
        {'name': 'AbsTest2',
         'contents': [

             {'name': 'prefix',
              'contents': UINT8(int_list=[0xcc, 0xff, 0xee])},

             {'name': 'variable_string',
              'contents': String(max_sz=20),
              'set_attrs': [NodeInternals.Abs_Postpone]},

             {'name': 'keycode',
              'contents': UINT16_be(int_list=[0xd2d3, 0xd2fe, 0xd2aa])},

             {'name': 'variable_suffix',
              'contents': String(val_list=['END', 'THE_END'])}
         ]}


        separator_desc = \
        {'name': 'separator',
         'separator': {'contents': {'name': 'sep_nl',
                                    'contents': String(val_list=['\n'], absorb_regexp=b'[\r\n|\n]+'),
                                    'absorb_csts': AbsNoCsts(regexp=True)},
                       'prefix': False,
                       'suffix': False,
                       'unique': True},
         'contents': [
             {'section_type': MH.FullyRandom,
              'contents': [
                  {'name': 'parameters',
                   'separator': {'contents': {'name': ('sep',2),
                                              'contents': String(val_list=[' '], absorb_regexp=b' +'),
                                              'absorb_csts': AbsNoCsts(regexp=True)}},
                   'qty': 3,
                   'contents': [
                       {'section_type': MH.FullyRandom,
                        'contents': [
                            {'name': 'color',
                             'determinist': True,  # used only for test purpose
                             'contents': [
                                 {'name': 'id',
                                  'contents': String(val_list=['color='])},
                                 {'name': 'val',
                                  'contents': String(val_list=['red', 'black'])}
                             ]},
                            {'name': 'type',
                             'contents': [
                                 {'name': ('id', 2),
                                  'contents': String(val_list=['type='])},
                                 {'name': ('val', 2),
                                  'contents': String(val_list=['circle', 'cube', 'rectangle'], determinist=False)}
                            ]},
                        ]}]},
                  {'contents': String(val_list=['AAAA', 'BBBB', 'CCCC'], determinist=False),
                   'qty': (4, 6),
                   'name': 'str'}
              ]}
         ]}


        sync_desc = \
        {'name': 'exist_cond',
         'shape_type': MH.Ordered,
         'contents': [
             {'name': 'opcode',
              'contents': String(val_list=['A1', 'A2', 'A3'], determinist=True)},

             {'name': 'command_A1',
              'contents': String(val_list=['AAA', 'BBBB', 'CCCCC']),
              'exists_if': (RawCondition('A1'), 'opcode'),
              'qty': 3},

             {'name': 'command_A2',
              'contents': UINT32_be(int_list=[0xDEAD, 0xBEEF]),
              'exists_if': (RawCondition('A2'), 'opcode')},

             {'name': 'command_A3',
              'exists_if': (RawCondition('A3'), 'opcode'),
              'contents': [
                  {'name': 'A3_subopcode',
                   'contents': BitField(subfield_sizes=[15,2,4], endian=VT.BigEndian,
                                        subfield_val_lists=[None, [1,2], [5,6,12]],
                                        subfield_val_extremums=[[500, 600], None, None],
                                        determinist=False)},

                  {'name': 'A3_int',
                   'contents': UINT16_be(int_list=[10, 20, 30], determinist=False)},

                  {'name': 'A3_deco1',
                   'exists_if': (IntCondition(10), 'A3_int'),
                   'contents': String(val_list=['*1*0*'])},

                  {'name': 'A3_deco2',
                   'exists_if': (IntCondition([20, 30]), 'A3_int'),
                   'contents': String(val_list=['+2+0+3+0+'])}
              ]},

             {'name': 'A31_payload',
              'contents': String(val_list=['$ A31_OK $', '$ A31_KO $'], determinist=False),
              'exists_if': (BitFieldCondition(sf=2, val=[6,12]), 'A3_subopcode')},

             {'name': 'A32_payload',
              'contents': String(val_list=['$ A32_VALID $', '$ A32_INVALID $'], determinist=False),
              'exists_if': (BitFieldCondition(sf=2, val=5), 'A3_subopcode')}
         ]}


        len_gen_desc = \
        {'name': 'len_gen',
         'contents': [
             {'name': 'len',
              'type': MH.Generator,
              'contents': MH.LEN(UINT32_be),
              'node_args': 'payload',
              'absorb_csts': AbsNoCsts()},

             {'name': 'payload',
              'contents': String(min_sz=10, max_sz=100, determinist=False)},
         ]}


        offset_gen_desc = \
        {'name': 'off_gen',
         'contents': [
             {'name': 'prefix',
              'contents': String(size=10, alphabet='*+')},

             {'name': 'body',
              'shape_type': MH.FullyRandom,
              'contents': [
                  {'contents': String(val_list=['AAA']),
                   'qty': 10,
                   'name': 'str'},
                  {'contents': UINT8(int_list=[0x3F]),
                   'name': 'int'}
              ]},

             {'name': 'len',
              'type': MH.Generator,
              'contents': MH.OFFSET(use_current_position=False, vt=UINT8),
              'node_args': ['prefix', 'int', 'body']},
         ]}


        misc_gen_desc = \
        {'name': 'misc_gen',
         'contents': [
             {'name': 'integers',
              'contents': [
                  {'name': 'int16',
                   'qty': (2, 10),
                   'contents': UINT16_be(int_list=[16, 1, 6], determinist=False)},

                  {'name': 'int32',
                   'qty': (3, 8),
                   'contents': UINT32_be(int_list=[32, 3, 2], determinist=False)}
              ]},

             {'name': 'int16_qty',
              'type': MH.Generator,
              'contents': MH.QTY(node_name='int16', vt=UINT8),
              'node_args': 'integers'},

             {'name': 'int32_qty',
              'type': MH.Generator,
              'contents': MH.QTY(node_name='int32', vt=UINT8),
              'node_args': 'integers'},

             {'name': 'tstamp',
              'type': MH.Generator,
              'contents': MH.TIMESTAMP("%H%M%S"),
              'absorb_csts': AbsCsts(contents=False)},

             {'name': 'crc',
              'type': MH.Generator,
              'contents': MH.CRC(UINT32_be),
              'node_args': ['tstamp', 'int32_qty'],
              'absorb_csts': AbsCsts(contents=False)}

         ]}


        self.register(test_node_desc, abstest_desc, abstest2_desc, separator_desc,
                      sync_desc, len_gen_desc, misc_gen_desc, offset_gen_desc)



data_model = MyDF_DataModel()