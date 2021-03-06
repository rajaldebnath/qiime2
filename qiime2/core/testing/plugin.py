# ----------------------------------------------------------------------------
# Copyright (c) 2016-2017, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from importlib import import_module

import qiime2
import qiime2.plugin

from .format import (
    IntSequenceFormat,
    IntSequenceFormatV2,
    MappingFormat,
    SingleIntFormat,
    IntSequenceDirectoryFormat,
    IntSequenceV2DirectoryFormat,
    MappingDirectoryFormat,
    FourIntsDirectoryFormat,
    RedundantSingleIntDirectoryFormat,
    UnimportableFormat,
    UnimportableDirectoryFormat
)

from .type import (IntSequence1, IntSequence2, Mapping, FourInts, SingleInt,
                   Kennel, Dog, Cat)
from .method import (concatenate_ints, split_ints, merge_mappings,
                     identity_with_metadata, identity_with_metadata_category,
                     identity_with_optional_metadata,
                     identity_with_optional_metadata_category,
                     params_only_method, no_input_method,
                     optional_artifacts_method, long_description_method)
from .visualizer import (most_common_viz, mapping_viz, params_only_viz,
                         no_input_viz)
from .pipeline import (parameter_only_pipeline, typical_pipeline,
                       optional_artifact_pipeline, visualizer_only_pipeline,
                       pipelines_in_pipeline, pointless_pipeline,
                       failing_pipeline)

dummy_plugin = qiime2.plugin.Plugin(
    name='dummy-plugin',
    description='Description of dummy plugin.',
    short_description='Dummy plugin for testing.',
    version='0.0.0-dev',
    website='https://github.com/qiime2/qiime2',
    package='qiime2.core.testing',
    citation_text='No relevant citation.',
    user_support_text='For help, see https://qiime2.org'
)

import_module('qiime2.core.testing.transformer')

# Register semantic types
dummy_plugin.register_semantic_types(IntSequence1, IntSequence2, Mapping,
                                     FourInts, Kennel, Dog, Cat, SingleInt)

# Register formats
dummy_plugin.register_formats(
    IntSequenceFormat, IntSequenceFormatV2, MappingFormat, SingleIntFormat,
    IntSequenceDirectoryFormat, IntSequenceV2DirectoryFormat,
    MappingDirectoryFormat, FourIntsDirectoryFormat, UnimportableFormat,
    UnimportableDirectoryFormat, RedundantSingleIntDirectoryFormat
)

dummy_plugin.register_semantic_type_to_format(
    IntSequence1,
    artifact_format=IntSequenceDirectoryFormat
)
dummy_plugin.register_semantic_type_to_format(
    IntSequence2,
    artifact_format=IntSequenceV2DirectoryFormat
)
dummy_plugin.register_semantic_type_to_format(
    Mapping,
    artifact_format=MappingDirectoryFormat
)
dummy_plugin.register_semantic_type_to_format(
    FourInts,
    artifact_format=FourIntsDirectoryFormat
)
dummy_plugin.register_semantic_type_to_format(
    SingleInt,
    artifact_format=RedundantSingleIntDirectoryFormat
)
dummy_plugin.register_semantic_type_to_format(
    Kennel[Dog | Cat],
    artifact_format=MappingDirectoryFormat
)

# TODO add an optional parameter to this method when they are supported
dummy_plugin.methods.register_function(
    function=concatenate_ints,
    inputs={
        'ints1': IntSequence1 | IntSequence2,
        'ints2': IntSequence1,
        'ints3': IntSequence2
    },
    parameters={
        'int1': qiime2.plugin.Int,
        'int2': qiime2.plugin.Int
    },
    outputs=[
        ('concatenated_ints', IntSequence1)
    ],
    name='Concatenate integers',
    description='This method concatenates integers into a single sequence in '
                'the order they are provided.'
)

# TODO update to use TypeMap so IntSequence1 | IntSequence2 are accepted, and
# the return type is IntSequence1 or IntSequence2.
dummy_plugin.methods.register_function(
    function=split_ints,
    inputs={
        'ints': IntSequence1
    },
    parameters={},
    outputs=[
        ('left', IntSequence1),
        ('right', IntSequence1)
    ],
    name='Split sequence of integers in half',
    description='This method splits a sequence of integers in half, returning '
                'the two halves (left and right). If the input sequence\'s '
                'length is not evenly divisible by 2, the right half will '
                'have one more element than the left.'
)

dummy_plugin.methods.register_function(
    function=merge_mappings,
    inputs={
        'mapping1': Mapping,
        'mapping2': Mapping
    },
    input_descriptions={
        'mapping1': 'Mapping object to be merged'
    },
    parameters={},
    outputs=[
        ('merged_mapping', Mapping)
    ],
    output_descriptions={
        'merged_mapping': 'Resulting merged Mapping object'},
    name='Merge mappings',
    description='This method merges two mappings into a single new mapping. '
                'If a key is shared between mappings and the values differ, '
                'an error will be raised.'
)

dummy_plugin.methods.register_function(
    function=identity_with_metadata,
    inputs={
        'ints': IntSequence1 | IntSequence2
    },
    parameters={
        'metadata': qiime2.plugin.Metadata
    },
    outputs=[
        ('out', IntSequence1)
    ],
    name='Identity',
    description='This method does nothing, but takes metadata'
)

dummy_plugin.methods.register_function(
    function=long_description_method,
    inputs={
        'mapping1': Mapping
    },
    input_descriptions={
        'mapping1': ("This is a very long description. If asked about its "
                     "length, I would have to say it is greater than 79 "
                     "characters.")
    },
    parameters={
        'name': qiime2.plugin.Str,
        'age': qiime2.plugin.Int
    },
    parameter_descriptions={
        'name': ("This is a very long description. If asked about its length,"
                 " I would have to say it is greater than 79 characters.")
    },
    outputs=[
        ('out', Mapping)
    ],
    output_descriptions={
        'out': ("This is a very long description. If asked about its length,"
                " I would have to say it is greater than 79 characters.")
    },
    name="Long Description",
    description=("This is a very long description. If asked about its length,"
                 " I would have to say it is greater than 79 characters.")
)

dummy_plugin.methods.register_function(
    function=identity_with_metadata_category,
    inputs={
        'ints': IntSequence1 | IntSequence2
    },
    parameters={
        'metadata': qiime2.plugin.MetadataCategory
    },
    outputs=[
        ('out', IntSequence1)
    ],
    name='Identity',
    description='This method does nothing, but takes a metadata category'
)


dummy_plugin.methods.register_function(
    function=identity_with_optional_metadata,
    inputs={
        'ints': IntSequence1 | IntSequence2
    },
    parameters={
        'metadata': qiime2.plugin.Metadata
    },
    outputs=[
        ('out', IntSequence1)
    ],
    name='Identity',
    description='This method does nothing, but takes optional metadata'
)

dummy_plugin.methods.register_function(
    function=identity_with_optional_metadata_category,
    inputs={
        'ints': IntSequence1 | IntSequence2
    },
    parameters={
        'metadata': qiime2.plugin.MetadataCategory
    },
    outputs=[
        ('out', IntSequence1)
    ],
    name='Identity',
    description='This method does nothing, but takes an optional metadata '
                'category'
)


dummy_plugin.methods.register_function(
    function=params_only_method,
    inputs={},
    parameters={
        'name': qiime2.plugin.Str,
        'age': qiime2.plugin.Int
    },
    outputs=[
        ('out', Mapping)
    ],
    name='Parameters only method',
    description='This method only accepts parameters.'
)


dummy_plugin.methods.register_function(
    function=no_input_method,
    inputs={},
    parameters={},
    outputs=[
        ('out', Mapping)
    ],
    name='No input method',
    description='This method does not accept any type of input.'
)


dummy_plugin.methods.register_function(
    function=optional_artifacts_method,
    inputs={
        'ints': IntSequence1,
        'optional1': IntSequence1,
        'optional2': IntSequence1 | IntSequence2
    },
    parameters={
        'num1': qiime2.plugin.Int,
        'num2': qiime2.plugin.Int
    },
    outputs=[
        ('output', IntSequence1)
    ],
    name='Optional artifacts method',
    description='This method declares optional artifacts and concatenates '
                'whatever integers are supplied as input.'
)


dummy_plugin.visualizers.register_function(
    function=params_only_viz,
    inputs={},
    parameters={
        'name': qiime2.plugin.Str,
        'age': qiime2.plugin.Int
    },
    name='Parameters only viz',
    description='This visualizer only accepts parameters.'
)


dummy_plugin.visualizers.register_function(
    function=no_input_viz,
    inputs={},
    parameters={},
    name='No input viz',
    description='This visualizer does not accept any type of input.'
)


dummy_plugin.visualizers.register_function(
    function=most_common_viz,
    inputs={
        'ints': IntSequence1 | IntSequence2
    },
    parameters={},
    name='Visualize most common integers',
    description='This visualizer produces HTML and TSV outputs containing the '
                'input sequence of integers ordered from most- to '
                'least-frequently occurring, along with their respective '
                'frequencies.'
)

# TODO add optional parameters to this method when they are supported
dummy_plugin.visualizers.register_function(
    function=mapping_viz,
    inputs={
        'mapping1': Mapping,
        'mapping2': Mapping
    },
    parameters={
        'key_label': qiime2.plugin.Str,
        'value_label': qiime2.plugin.Str
    },
    name='Visualize two mappings',
    description='This visualizer produces an HTML visualization of two '
                'key-value mappings, each sorted in alphabetical order by key.'
)

dummy_plugin.pipelines.register_function(
    function=parameter_only_pipeline,
    inputs={},
    parameters={
        'int1': qiime2.plugin.Int,
        'int2': qiime2.plugin.Int,
        'metadata': qiime2.plugin.Metadata
    },
    outputs=[
        ('foo', IntSequence2),
        ('bar', IntSequence1)
    ],
    name='Do multiple things',
    description='This pipeline only accepts parameters',
    parameter_descriptions={
        'int1': 'An integer, the first one in fact',
        'int2': 'An integer, the second one',
        'metadata': 'Very little is done with this'
    },
    output_descriptions={
        'foo': 'Foo - "The Integers of 2"',
        'bar': 'Bar - "What a sequences"'
    }
)

dummy_plugin.pipelines.register_function(
    function=typical_pipeline,
    inputs={
        'int_sequence': IntSequence1,
        'mapping': Mapping
    },
    parameters={
        'do_extra_thing': qiime2.plugin.Bool,
        'add': qiime2.plugin.Int
    },
    outputs=[
        ('out_map', Mapping),
        ('left', IntSequence1),
        ('right', IntSequence1),
        ('left_viz', qiime2.plugin.Visualization),
        ('right_viz', qiime2.plugin.Visualization)
    ],
    input_descriptions={
        'int_sequence': 'A sequence of ints',
        'mapping': 'A map to a number other than 42 will fail'
    },
    parameter_descriptions={
        'do_extra_thing': 'Increment `left` by `add` if true',
        'add': 'Unused if `do_extra_thing` is false'
    },
    output_descriptions={
        'out_map': 'Same as input',
        'left': 'Left side of `int_sequence` unless `do_extra_thing`',
        'right': 'Right side of `int_sequence`',
        'left_viz': '`left` visualized',
        'right_viz': '`right` visualized'
    },
    name='A typical pipeline with the potential to raise an error',
    description='Waste some time shuffling data around for no reason'
)

dummy_plugin.pipelines.register_function(
    function=optional_artifact_pipeline,
    inputs={
        'int_sequence': IntSequence1,
        'single_int': SingleInt
    },
    parameters={},
    outputs=[
        ('ints', IntSequence1)
    ],
    input_descriptions={
        'int_sequence': 'Some integers',
        'single_int': 'An integer'
    },
    output_descriptions={
        'ints': 'More integers'
    },
    name='Do stuff normally, but override this one step sometimes',
    description='Creates its own single_int, unless provided'
)

dummy_plugin.pipelines.register_function(
    function=visualizer_only_pipeline,
    inputs={
        'mapping': Mapping
    },
    parameters={},
    outputs=[
        ('viz1', qiime2.plugin.Visualization),
        ('viz2', qiime2.plugin.Visualization)
    ],
    input_descriptions={
        'mapping': 'A mapping to look at twice'
    },
    output_descriptions={
        'viz1': 'The no input viz',
        'viz2': 'Our `mapping` seen through the lense of "foo" *and* "bar"'
    },
    name='Visualize many things',
    description='Looks at both nothing and a mapping'
)

dummy_plugin.pipelines.register_function(
    function=pipelines_in_pipeline,
    inputs={
        'int_sequence': IntSequence1,
        'mapping': Mapping
    },
    parameters={},
    outputs=[
        ('int1', SingleInt),
        ('out_map', Mapping),
        ('left', IntSequence1),
        ('right', IntSequence1),
        ('left_viz', qiime2.plugin.Visualization),
        ('right_viz', qiime2.plugin.Visualization),
        ('viz1', qiime2.plugin.Visualization),
        ('viz2', qiime2.plugin.Visualization)
    ],
    name='Do a great many things',
    description=('Mapping is chained from typical_pipeline into '
                 'visualizer_only_pipeline')
)

dummy_plugin.pipelines.register_function(
    function=pointless_pipeline,
    inputs={},
    parameters={},
    outputs=[('random_int', SingleInt)],
    name='Get an integer',
    description='Integer was chosen to be 4 by a random dice roll'
)

dummy_plugin.pipelines.register_function(
    function=failing_pipeline,
    inputs={
        'int_sequence': IntSequence1
    },
    parameters={
        'break_from': qiime2.plugin.Str % qiime2.plugin.Choices(
            {'arity', 'return-view', 'type', 'method', 'internal', 'no-plugin',
             'no-action'})
    },
    outputs=[('mapping', Mapping)],
    name='Test different ways of failing',
    description=('This is useful to make sure all of the intermediate stuff is'
                 ' cleaned up the way it should be.')
)
