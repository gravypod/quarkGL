# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: third_party/bazel/protos/extra_actions_base.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='third_party/bazel/protos/extra_actions_base.proto',
  package='blaze',
  syntax='proto2',
  serialized_pb=_b('\n1third_party/bazel/protos/extra_actions_base.proto\x12\x05\x62laze\"D\n\x12\x45xtraActionSummary\x12.\n\x06\x61\x63tion\x18\x01 \x03(\x0b\x32\x1e.blaze.DetailedExtraActionInfo\"Z\n\x17\x44\x65tailedExtraActionInfo\x12\x17\n\x0ftriggering_file\x18\x01 \x01(\t\x12&\n\x06\x61\x63tion\x18\x02 \x02(\x0b\x32\x16.blaze.ExtraActionInfo\"\xf4\x04\n\x0f\x45xtraActionInfo\x12\r\n\x05owner\x18\x01 \x01(\t\x12\x17\n\x0b\x61spect_name\x18\x06 \x01(\tB\x02\x18\x01\x12K\n\x11\x61spect_parameters\x18\x07 \x03(\x0b\x32,.blaze.ExtraActionInfo.AspectParametersEntryB\x02\x18\x01\x12\x38\n\x07\x61spects\x18\x08 \x03(\x0b\x32\'.blaze.ExtraActionInfo.AspectDescriptor\x12\n\n\x02id\x18\x02 \x01(\t\x12\x10\n\x08mnemonic\x18\x05 \x01(\t\x1aZ\n\x15\x41spectParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x30\n\x05value\x18\x02 \x01(\x0b\x32!.blaze.ExtraActionInfo.StringList:\x02\x38\x01\x1a\x1f\n\nStringList\x12\r\n\x05value\x18\x01 \x03(\t:\x02\x18\x01\x1a\x8b\x02\n\x10\x41spectDescriptor\x12\x13\n\x0b\x61spect_name\x18\x01 \x01(\t\x12X\n\x11\x61spect_parameters\x18\x02 \x03(\x0b\x32=.blaze.ExtraActionInfo.AspectDescriptor.AspectParametersEntry\x1ak\n\x15\x41spectParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x41\n\x05value\x18\x02 \x01(\x0b\x32\x32.blaze.ExtraActionInfo.AspectDescriptor.StringList:\x02\x38\x01\x1a\x1b\n\nStringList\x12\r\n\x05value\x18\x01 \x03(\t*\t\x08\xe8\x07\x10\x80\x80\x80\x80\x02\"2\n\x13\x45nvironmentVariable\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\"\xb3\x01\n\tSpawnInfo\x12\x10\n\x08\x61rgument\x18\x01 \x03(\t\x12,\n\x08variable\x18\x02 \x03(\x0b\x32\x1a.blaze.EnvironmentVariable\x12\x12\n\ninput_file\x18\x04 \x03(\t\x12\x13\n\x0boutput_file\x18\x05 \x03(\t2=\n\nspawn_info\x12\x16.blaze.ExtraActionInfo\x18\xeb\x07 \x01(\x0b\x32\x10.blaze.SpawnInfo\"\xf6\x01\n\x0e\x43ppCompileInfo\x12\x0c\n\x04tool\x18\x01 \x01(\t\x12\x17\n\x0f\x63ompiler_option\x18\x02 \x03(\t\x12\x13\n\x0bsource_file\x18\x03 \x01(\t\x12\x13\n\x0boutput_file\x18\x04 \x01(\t\x12\x1b\n\x13sources_and_headers\x18\x05 \x03(\t\x12,\n\x08variable\x18\x06 \x03(\x0b\x32\x1a.blaze.EnvironmentVariable2H\n\x10\x63pp_compile_info\x12\x16.blaze.ExtraActionInfo\x18\xe9\x07 \x01(\x0b\x32\x15.blaze.CppCompileInfo\"\x96\x02\n\x0b\x43ppLinkInfo\x12\x12\n\ninput_file\x18\x01 \x03(\t\x12\x13\n\x0boutput_file\x18\x02 \x01(\t\x12\x1d\n\x15interface_output_file\x18\x03 \x01(\t\x12\x18\n\x10link_target_type\x18\x04 \x01(\t\x12\x17\n\x0flink_staticness\x18\x05 \x01(\t\x12\x12\n\nlink_stamp\x18\x06 \x03(\t\x12\"\n\x1a\x62uild_info_header_artifact\x18\x07 \x03(\t\x12\x10\n\x08link_opt\x18\x08 \x03(\t2B\n\rcpp_link_info\x12\x16.blaze.ExtraActionInfo\x18\xea\x07 \x01(\x0b\x32\x12.blaze.CppLinkInfo\"\x80\x02\n\x0fJavaCompileInfo\x12\x11\n\toutputjar\x18\x01 \x01(\t\x12\x11\n\tclasspath\x18\x02 \x03(\t\x12\x12\n\nsourcepath\x18\x03 \x03(\t\x12\x13\n\x0bsource_file\x18\x04 \x03(\t\x12\x11\n\tjavac_opt\x18\x05 \x03(\t\x12\x11\n\tprocessor\x18\x06 \x03(\t\x12\x15\n\rprocessorpath\x18\x07 \x03(\t\x12\x15\n\rbootclasspath\x18\x08 \x03(\t2J\n\x11java_compile_info\x12\x16.blaze.ExtraActionInfo\x18\xe8\x07 \x01(\x0b\x32\x16.blaze.JavaCompileInfo\"t\n\nPythonInfo\x12\x13\n\x0bsource_file\x18\x01 \x03(\t\x12\x10\n\x08\x64\x65p_file\x18\x02 \x03(\t2?\n\x0bpython_info\x12\x16.blaze.ExtraActionInfo\x18\xed\x07 \x01(\x0b\x32\x11.blaze.PythonInfoB/\n+com.google.devtools.build.lib.actions.extraP\x01')
)




_EXTRAACTIONSUMMARY = _descriptor.Descriptor(
  name='ExtraActionSummary',
  full_name='blaze.ExtraActionSummary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='blaze.ExtraActionSummary.action', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=128,
)


_DETAILEDEXTRAACTIONINFO = _descriptor.Descriptor(
  name='DetailedExtraActionInfo',
  full_name='blaze.DetailedExtraActionInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='triggering_file', full_name='blaze.DetailedExtraActionInfo.triggering_file', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action', full_name='blaze.DetailedExtraActionInfo.action', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=220,
)


_EXTRAACTIONINFO_ASPECTPARAMETERSENTRY = _descriptor.Descriptor(
  name='AspectParametersEntry',
  full_name='blaze.ExtraActionInfo.AspectParametersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='blaze.ExtraActionInfo.AspectParametersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='blaze.ExtraActionInfo.AspectParametersEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=447,
  serialized_end=537,
)

_EXTRAACTIONINFO_STRINGLIST = _descriptor.Descriptor(
  name='StringList',
  full_name='blaze.ExtraActionInfo.StringList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='blaze.ExtraActionInfo.StringList.value', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\030\001')),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=539,
  serialized_end=570,
)

_EXTRAACTIONINFO_ASPECTDESCRIPTOR_ASPECTPARAMETERSENTRY = _descriptor.Descriptor(
  name='AspectParametersEntry',
  full_name='blaze.ExtraActionInfo.AspectDescriptor.AspectParametersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='blaze.ExtraActionInfo.AspectDescriptor.AspectParametersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='blaze.ExtraActionInfo.AspectDescriptor.AspectParametersEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=704,
  serialized_end=811,
)

_EXTRAACTIONINFO_ASPECTDESCRIPTOR_STRINGLIST = _descriptor.Descriptor(
  name='StringList',
  full_name='blaze.ExtraActionInfo.AspectDescriptor.StringList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='blaze.ExtraActionInfo.AspectDescriptor.StringList.value', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=539,
  serialized_end=566,
)

_EXTRAACTIONINFO_ASPECTDESCRIPTOR = _descriptor.Descriptor(
  name='AspectDescriptor',
  full_name='blaze.ExtraActionInfo.AspectDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='aspect_name', full_name='blaze.ExtraActionInfo.AspectDescriptor.aspect_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='aspect_parameters', full_name='blaze.ExtraActionInfo.AspectDescriptor.aspect_parameters', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_EXTRAACTIONINFO_ASPECTDESCRIPTOR_ASPECTPARAMETERSENTRY, _EXTRAACTIONINFO_ASPECTDESCRIPTOR_STRINGLIST, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=573,
  serialized_end=840,
)

_EXTRAACTIONINFO = _descriptor.Descriptor(
  name='ExtraActionInfo',
  full_name='blaze.ExtraActionInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner', full_name='blaze.ExtraActionInfo.owner', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='aspect_name', full_name='blaze.ExtraActionInfo.aspect_name', index=1,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))),
    _descriptor.FieldDescriptor(
      name='aspect_parameters', full_name='blaze.ExtraActionInfo.aspect_parameters', index=2,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))),
    _descriptor.FieldDescriptor(
      name='aspects', full_name='blaze.ExtraActionInfo.aspects', index=3,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='blaze.ExtraActionInfo.id', index=4,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mnemonic', full_name='blaze.ExtraActionInfo.mnemonic', index=5,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_EXTRAACTIONINFO_ASPECTPARAMETERSENTRY, _EXTRAACTIONINFO_STRINGLIST, _EXTRAACTIONINFO_ASPECTDESCRIPTOR, ],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(1000, 536870912), ],
  oneofs=[
  ],
  serialized_start=223,
  serialized_end=851,
)


_ENVIRONMENTVARIABLE = _descriptor.Descriptor(
  name='EnvironmentVariable',
  full_name='blaze.EnvironmentVariable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='blaze.EnvironmentVariable.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='blaze.EnvironmentVariable.value', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=853,
  serialized_end=903,
)


_SPAWNINFO = _descriptor.Descriptor(
  name='SpawnInfo',
  full_name='blaze.SpawnInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='argument', full_name='blaze.SpawnInfo.argument', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='variable', full_name='blaze.SpawnInfo.variable', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='input_file', full_name='blaze.SpawnInfo.input_file', index=2,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_file', full_name='blaze.SpawnInfo.output_file', index=3,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='spawn_info', full_name='blaze.SpawnInfo.spawn_info', index=0,
      number=1003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=906,
  serialized_end=1085,
)


_CPPCOMPILEINFO = _descriptor.Descriptor(
  name='CppCompileInfo',
  full_name='blaze.CppCompileInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tool', full_name='blaze.CppCompileInfo.tool', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='compiler_option', full_name='blaze.CppCompileInfo.compiler_option', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_file', full_name='blaze.CppCompileInfo.source_file', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_file', full_name='blaze.CppCompileInfo.output_file', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sources_and_headers', full_name='blaze.CppCompileInfo.sources_and_headers', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='variable', full_name='blaze.CppCompileInfo.variable', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='cpp_compile_info', full_name='blaze.CppCompileInfo.cpp_compile_info', index=0,
      number=1001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1088,
  serialized_end=1334,
)


_CPPLINKINFO = _descriptor.Descriptor(
  name='CppLinkInfo',
  full_name='blaze.CppLinkInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='input_file', full_name='blaze.CppLinkInfo.input_file', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_file', full_name='blaze.CppLinkInfo.output_file', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='interface_output_file', full_name='blaze.CppLinkInfo.interface_output_file', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='link_target_type', full_name='blaze.CppLinkInfo.link_target_type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='link_staticness', full_name='blaze.CppLinkInfo.link_staticness', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='link_stamp', full_name='blaze.CppLinkInfo.link_stamp', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='build_info_header_artifact', full_name='blaze.CppLinkInfo.build_info_header_artifact', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='link_opt', full_name='blaze.CppLinkInfo.link_opt', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='cpp_link_info', full_name='blaze.CppLinkInfo.cpp_link_info', index=0,
      number=1002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1337,
  serialized_end=1615,
)


_JAVACOMPILEINFO = _descriptor.Descriptor(
  name='JavaCompileInfo',
  full_name='blaze.JavaCompileInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='outputjar', full_name='blaze.JavaCompileInfo.outputjar', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='classpath', full_name='blaze.JavaCompileInfo.classpath', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sourcepath', full_name='blaze.JavaCompileInfo.sourcepath', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_file', full_name='blaze.JavaCompileInfo.source_file', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='javac_opt', full_name='blaze.JavaCompileInfo.javac_opt', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='processor', full_name='blaze.JavaCompileInfo.processor', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='processorpath', full_name='blaze.JavaCompileInfo.processorpath', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bootclasspath', full_name='blaze.JavaCompileInfo.bootclasspath', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='java_compile_info', full_name='blaze.JavaCompileInfo.java_compile_info', index=0,
      number=1000, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1618,
  serialized_end=1874,
)


_PYTHONINFO = _descriptor.Descriptor(
  name='PythonInfo',
  full_name='blaze.PythonInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source_file', full_name='blaze.PythonInfo.source_file', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dep_file', full_name='blaze.PythonInfo.dep_file', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='python_info', full_name='blaze.PythonInfo.python_info', index=0,
      number=1005, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1876,
  serialized_end=1992,
)

_EXTRAACTIONSUMMARY.fields_by_name['action'].message_type = _DETAILEDEXTRAACTIONINFO
_DETAILEDEXTRAACTIONINFO.fields_by_name['action'].message_type = _EXTRAACTIONINFO
_EXTRAACTIONINFO_ASPECTPARAMETERSENTRY.fields_by_name['value'].message_type = _EXTRAACTIONINFO_STRINGLIST
_EXTRAACTIONINFO_ASPECTPARAMETERSENTRY.containing_type = _EXTRAACTIONINFO
_EXTRAACTIONINFO_STRINGLIST.containing_type = _EXTRAACTIONINFO
_EXTRAACTIONINFO_ASPECTDESCRIPTOR_ASPECTPARAMETERSENTRY.fields_by_name['value'].message_type = _EXTRAACTIONINFO_ASPECTDESCRIPTOR_STRINGLIST
_EXTRAACTIONINFO_ASPECTDESCRIPTOR_ASPECTPARAMETERSENTRY.containing_type = _EXTRAACTIONINFO_ASPECTDESCRIPTOR
_EXTRAACTIONINFO_ASPECTDESCRIPTOR_STRINGLIST.containing_type = _EXTRAACTIONINFO_ASPECTDESCRIPTOR
_EXTRAACTIONINFO_ASPECTDESCRIPTOR.fields_by_name['aspect_parameters'].message_type = _EXTRAACTIONINFO_ASPECTDESCRIPTOR_ASPECTPARAMETERSENTRY
_EXTRAACTIONINFO_ASPECTDESCRIPTOR.containing_type = _EXTRAACTIONINFO
_EXTRAACTIONINFO.fields_by_name['aspect_parameters'].message_type = _EXTRAACTIONINFO_ASPECTPARAMETERSENTRY
_EXTRAACTIONINFO.fields_by_name['aspects'].message_type = _EXTRAACTIONINFO_ASPECTDESCRIPTOR
_SPAWNINFO.fields_by_name['variable'].message_type = _ENVIRONMENTVARIABLE
_CPPCOMPILEINFO.fields_by_name['variable'].message_type = _ENVIRONMENTVARIABLE
DESCRIPTOR.message_types_by_name['ExtraActionSummary'] = _EXTRAACTIONSUMMARY
DESCRIPTOR.message_types_by_name['DetailedExtraActionInfo'] = _DETAILEDEXTRAACTIONINFO
DESCRIPTOR.message_types_by_name['ExtraActionInfo'] = _EXTRAACTIONINFO
DESCRIPTOR.message_types_by_name['EnvironmentVariable'] = _ENVIRONMENTVARIABLE
DESCRIPTOR.message_types_by_name['SpawnInfo'] = _SPAWNINFO
DESCRIPTOR.message_types_by_name['CppCompileInfo'] = _CPPCOMPILEINFO
DESCRIPTOR.message_types_by_name['CppLinkInfo'] = _CPPLINKINFO
DESCRIPTOR.message_types_by_name['JavaCompileInfo'] = _JAVACOMPILEINFO
DESCRIPTOR.message_types_by_name['PythonInfo'] = _PYTHONINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExtraActionSummary = _reflection.GeneratedProtocolMessageType('ExtraActionSummary', (_message.Message,), dict(
  DESCRIPTOR = _EXTRAACTIONSUMMARY,
  __module__ = 'third_party.bazel.protos.extra_actions_base_pb2'
  # @@protoc_insertion_point(class_scope:blaze.ExtraActionSummary)
  ))
_sym_db.RegisterMessage(ExtraActionSummary)

DetailedExtraActionInfo = _reflection.GeneratedProtocolMessageType('DetailedExtraActionInfo', (_message.Message,), dict(
  DESCRIPTOR = _DETAILEDEXTRAACTIONINFO,
  __module__ = 'third_party.bazel.protos.extra_actions_base_pb2'
  # @@protoc_insertion_point(class_scope:blaze.DetailedExtraActionInfo)
  ))
_sym_db.RegisterMessage(DetailedExtraActionInfo)

ExtraActionInfo = _reflection.GeneratedProtocolMessageType('ExtraActionInfo', (_message.Message,), dict(

  AspectParametersEntry = _reflection.GeneratedProtocolMessageType('AspectParametersEntry', (_message.Message,), dict(
    DESCRIPTOR = _EXTRAACTIONINFO_ASPECTPARAMETERSENTRY,
    __module__ = 'third_party.bazel.protos.extra_actions_base_pb2'
    # @@protoc_insertion_point(class_scope:blaze.ExtraActionInfo.AspectParametersEntry)
    ))
  ,

  StringList = _reflection.GeneratedProtocolMessageType('StringList', (_message.Message,), dict(
    DESCRIPTOR = _EXTRAACTIONINFO_STRINGLIST,
    __module__ = 'third_party.bazel.protos.extra_actions_base_pb2'
    # @@protoc_insertion_point(class_scope:blaze.ExtraActionInfo.StringList)
    ))
  ,

  AspectDescriptor = _reflection.GeneratedProtocolMessageType('AspectDescriptor', (_message.Message,), dict(

    AspectParametersEntry = _reflection.GeneratedProtocolMessageType('AspectParametersEntry', (_message.Message,), dict(
      DESCRIPTOR = _EXTRAACTIONINFO_ASPECTDESCRIPTOR_ASPECTPARAMETERSENTRY,
      __module__ = 'third_party.bazel.protos.extra_actions_base_pb2'
      # @@protoc_insertion_point(class_scope:blaze.ExtraActionInfo.AspectDescriptor.AspectParametersEntry)
      ))
    ,

    StringList = _reflection.GeneratedProtocolMessageType('StringList', (_message.Message,), dict(
      DESCRIPTOR = _EXTRAACTIONINFO_ASPECTDESCRIPTOR_STRINGLIST,
      __module__ = 'third_party.bazel.protos.extra_actions_base_pb2'
      # @@protoc_insertion_point(class_scope:blaze.ExtraActionInfo.AspectDescriptor.StringList)
      ))
    ,
    DESCRIPTOR = _EXTRAACTIONINFO_ASPECTDESCRIPTOR,
    __module__ = 'third_party.bazel.protos.extra_actions_base_pb2'
    # @@protoc_insertion_point(class_scope:blaze.ExtraActionInfo.AspectDescriptor)
    ))
  ,
  DESCRIPTOR = _EXTRAACTIONINFO,
  __module__ = 'third_party.bazel.protos.extra_actions_base_pb2'
  # @@protoc_insertion_point(class_scope:blaze.ExtraActionInfo)
  ))
_sym_db.RegisterMessage(ExtraActionInfo)
_sym_db.RegisterMessage(ExtraActionInfo.AspectParametersEntry)
_sym_db.RegisterMessage(ExtraActionInfo.StringList)
_sym_db.RegisterMessage(ExtraActionInfo.AspectDescriptor)
_sym_db.RegisterMessage(ExtraActionInfo.AspectDescriptor.AspectParametersEntry)
_sym_db.RegisterMessage(ExtraActionInfo.AspectDescriptor.StringList)

EnvironmentVariable = _reflection.GeneratedProtocolMessageType('EnvironmentVariable', (_message.Message,), dict(
  DESCRIPTOR = _ENVIRONMENTVARIABLE,
  __module__ = 'third_party.bazel.protos.extra_actions_base_pb2'
  # @@protoc_insertion_point(class_scope:blaze.EnvironmentVariable)
  ))
_sym_db.RegisterMessage(EnvironmentVariable)

SpawnInfo = _reflection.GeneratedProtocolMessageType('SpawnInfo', (_message.Message,), dict(
  DESCRIPTOR = _SPAWNINFO,
  __module__ = 'third_party.bazel.protos.extra_actions_base_pb2'
  # @@protoc_insertion_point(class_scope:blaze.SpawnInfo)
  ))
_sym_db.RegisterMessage(SpawnInfo)

CppCompileInfo = _reflection.GeneratedProtocolMessageType('CppCompileInfo', (_message.Message,), dict(
  DESCRIPTOR = _CPPCOMPILEINFO,
  __module__ = 'third_party.bazel.protos.extra_actions_base_pb2'
  # @@protoc_insertion_point(class_scope:blaze.CppCompileInfo)
  ))
_sym_db.RegisterMessage(CppCompileInfo)

CppLinkInfo = _reflection.GeneratedProtocolMessageType('CppLinkInfo', (_message.Message,), dict(
  DESCRIPTOR = _CPPLINKINFO,
  __module__ = 'third_party.bazel.protos.extra_actions_base_pb2'
  # @@protoc_insertion_point(class_scope:blaze.CppLinkInfo)
  ))
_sym_db.RegisterMessage(CppLinkInfo)

JavaCompileInfo = _reflection.GeneratedProtocolMessageType('JavaCompileInfo', (_message.Message,), dict(
  DESCRIPTOR = _JAVACOMPILEINFO,
  __module__ = 'third_party.bazel.protos.extra_actions_base_pb2'
  # @@protoc_insertion_point(class_scope:blaze.JavaCompileInfo)
  ))
_sym_db.RegisterMessage(JavaCompileInfo)

PythonInfo = _reflection.GeneratedProtocolMessageType('PythonInfo', (_message.Message,), dict(
  DESCRIPTOR = _PYTHONINFO,
  __module__ = 'third_party.bazel.protos.extra_actions_base_pb2'
  # @@protoc_insertion_point(class_scope:blaze.PythonInfo)
  ))
_sym_db.RegisterMessage(PythonInfo)

_SPAWNINFO.extensions_by_name['spawn_info'].message_type = _SPAWNINFO
ExtraActionInfo.RegisterExtension(_SPAWNINFO.extensions_by_name['spawn_info'])
_CPPCOMPILEINFO.extensions_by_name['cpp_compile_info'].message_type = _CPPCOMPILEINFO
ExtraActionInfo.RegisterExtension(_CPPCOMPILEINFO.extensions_by_name['cpp_compile_info'])
_CPPLINKINFO.extensions_by_name['cpp_link_info'].message_type = _CPPLINKINFO
ExtraActionInfo.RegisterExtension(_CPPLINKINFO.extensions_by_name['cpp_link_info'])
_JAVACOMPILEINFO.extensions_by_name['java_compile_info'].message_type = _JAVACOMPILEINFO
ExtraActionInfo.RegisterExtension(_JAVACOMPILEINFO.extensions_by_name['java_compile_info'])
_PYTHONINFO.extensions_by_name['python_info'].message_type = _PYTHONINFO
ExtraActionInfo.RegisterExtension(_PYTHONINFO.extensions_by_name['python_info'])

DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n+com.google.devtools.build.lib.actions.extraP\001'))
_EXTRAACTIONINFO_ASPECTPARAMETERSENTRY.has_options = True
_EXTRAACTIONINFO_ASPECTPARAMETERSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_EXTRAACTIONINFO_STRINGLIST.has_options = True
_EXTRAACTIONINFO_STRINGLIST._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\030\001'))
_EXTRAACTIONINFO_ASPECTDESCRIPTOR_ASPECTPARAMETERSENTRY.has_options = True
_EXTRAACTIONINFO_ASPECTDESCRIPTOR_ASPECTPARAMETERSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_EXTRAACTIONINFO.fields_by_name['aspect_name'].has_options = True
_EXTRAACTIONINFO.fields_by_name['aspect_name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))
_EXTRAACTIONINFO.fields_by_name['aspect_parameters'].has_options = True
_EXTRAACTIONINFO.fields_by_name['aspect_parameters']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))
# @@protoc_insertion_point(module_scope)
