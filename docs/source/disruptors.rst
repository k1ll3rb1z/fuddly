.. _dis:generic-disruptors:

Generic Disruptors
******************

The current generic disruptors are presented within the following
sections.

Stateful Disruptors
===================

.. _dis:ttype:

tTYPE - Advanced Alteration of Terminal Typed Node
--------------------------------------------------

Description:
  Perform alterations on typed nodes (one at a time) according to
  its type and various complementary information (such as size,
  allowed values, ...).

Reference:
  :class:`framework.generic_data_makers.sd_fuzz_typed_nodes`

Parameters:
  .. code-block:: none

      parameters:
        |_ init
        |      | desc: make the model walker ignore all the steps until the provided
        |      |       one
        |      | default: 1 [type: int]
        |_ runs_per_node
        |      | desc: maximum number of test cases for a single node (-1 means until
        |      |       the end)
        |      | default: -1 [type: int]
        |_ max_steps
        |      | desc: maximum number of steps (-1 means until the end)
        |      | default: -1 [type: int]
        |_ clone_node
        |      | desc: if True the dmaker will always return a copy of the node. (for
        |      |       stateless disruptors dealing with big data it can be useful
        |      |       to it to False)
        |      | default: True [type: bool]
        |_ path
        |      | desc: graph path regexp to select nodes on which the disruptor should
        |      |       apply
        |      | default: None [type: str]
        |_ deep
        |      | desc: when set to True, if a node structure has changed, the modelwalker
        |      |       will reset its walk through the children nodes
        |      | default: True [type: bool]
        |_ ign_sep
        |      | desc: when set to True, non-terminal separators will be ignored if
        |      |       any are defined.
        |      | default: False [type: bool]
        |_ fix
        |      | desc: limit constraints fixing to the nodes related to the currently
        |      |       fuzzed one (only implemented for 'sync_size_with' and
        |      |       'sync_enc_size_with')
        |      | default: True [type: bool]
        |_ fix_all
        |      | desc: for each produced data, reevaluate the constraints on the whole
        |      |       graph
        |      | default: False [type: bool]
        |_ order
        |      | desc: when set to True, the fuzzing order is strictly guided by the
        |      |       data structure. Otherwise, fuzz weight (if specified in the
        |      |       data model) is used for ordering
        |      | default: False [type: bool]
        |_ fuzz_mag
        |      | desc: order of magnitude for maximum size of some fuzzing test cases.
        |      | default: 1.0 [type: float]

tSTRUCT - Alter Data Structure
------------------------------

Description:
  For each node associated to existence constraints or quantity
  constraints or size constraints, alter the constraint, one at a time, after each call
  to this disruptor. If `deep` is set, enable new structure corruption cases, based on
  the minimum and maximum amount of non-terminal nodes (within the
  input data) specified in the data model.

Reference:
  :class:`framework.generic_data_makers.sd_struct_constraints`

Parameters:
  .. code-block:: none

       parameters:
         |_ init
         |      | desc: make the model walker ignore all the steps until the provided
         |      |       one
         |      | default: 1 [type: int]
         |_ max_steps
         |      | desc: maximum number of steps (-1 means until the end)
         |      | default: -1 [type: int]
         |_ path
         |      | desc: graph path regexp to select nodes on which the disruptor should
         |      |       apply
         |      | default: None [type: str]
         |_ deep
         |      | desc: if True, enable corruption of minimum and maxium amount of non-terminal
         |      |       nodes
         |      | default: False [type: bool]

Usage Example:
   A typical *disruptor chain* for leveraging this disruptor could be:

   .. code-block:: none

      <Data Generator> tWALK(path='path/to/some/node') tSTRUCT

   .. note:: Test this chain with the data example found at
             :ref:`dm:pattern:existence-cond`, and set the path to the
             ``opcode`` node path.

   .. seealso:: Refer to :ref:`tuto:dmaker-chain` for insight
        into *disruptor chains*.



tALT - Walk Through Alternative Node Configurations
---------------------------------------------------

Description:
  Switch the configuration of each node, one by one, with the provided
  alternate configuration.

Reference:
  :class:`framework.generic_data_makers.sd_switch_to_alternate_conf`

Parameters:
  .. code-block:: none

       parameters:
         |_ clone_node
         |      | desc: if True the dmaker will always return a copy of the node. (for
         |      |       stateless disruptors dealing with big data it can be useful
         |      |       to it to False)
         |      | default: True [type: bool]
         |_ init
         |      | desc: make the model walker ignore all the steps until the provided
         |      |       one
         |      | default: 1 [type: int]
         |_ max_steps
         |      | desc: maximum number of steps (-1 means until the end)
         |      | default: -1 [type: int]
         |_ runs_per_node
         |      | desc: maximum number of test cases for a single node (-1 means until
         |      |       the end)
         |      | default: -1 [type: int]
         |_ conf
         |      | desc: Change the configuration, with the one provided (by name), of
         |      |       all nodes reachable from the root, one-by-one. [default value
         |      |       is set dynamically with the first-found existing alternate configuration]
         |      | default: None [type: str, list, tuple]


tSEP - Alteration of Separator Node
-----------------------------------

Description:
  Perform alterations on separators (one at a time). Each time a
  separator is encountered in the provided data, it will be replaced
  by another separator picked from the ones existing within the
  provided data.

Reference:
  :class:`framework.generic_data_makers.sd_fuzz_separator_nodes`

Parameters:
  .. code-block:: none

       parameters:
         |_ clone_node
         |      | desc: if True the dmaker will always return a copy of the node. (for
         |      |       stateless disruptors dealing with big data it can be useful
         |      |       to it to False)
         |      | default: True [type: bool]
         |_ init
         |      | desc: make the model walker ignore all the steps until the provided
         |      |       one
         |      | default: 1 [type: int]
         |_ max_steps
         |      | desc: maximum number of steps (-1 means until the end)
         |      | default: -1 [type: int]
         |_ runs_per_node
         |      | desc: maximum number of test cases for a single node (-1 means until
         |      |       the end)
         |      | default: -1 [type: int]
         |_ path
         |      | desc: graph path regexp to select nodes on which the disruptor should
         |      |       apply
         |      | default: None [type: str]
         |_ order
         |      | desc: when set to True, the fuzzing order is strictly guided by the
         |      |       data structure. Otherwise, fuzz weight (if specified in the
         |      |       data model) is used for ordering
         |      | default: False [type: bool]
         |_ deep
         |      | desc: when set to True, if a node structure has changed, the modelwalker
         |      |       will reset its walk through the children nodes
         |      | default: True [type: bool]



tWALK - Walk Through a Data Model
---------------------------------

Description:
  Walk through the provided data and for each visited node, iterates
  over the allowed values (with respect to the data model).  Note: *no
  alteration* is performed by this disruptor.

Reference:
  :class:`framework.generic_data_makers.sd_iter_over_data`

Parameters:
  .. code-block:: none

      parameters:
        |_ clone_node
        |      | desc: if True the dmaker will always return a copy of the node. (for
        |      |       stateless disruptors dealing with big data it can be useful
        |      |       to it to False)
        |      | default: True [type: bool]
        |_ init
        |      | desc: make the model walker ignore all the steps until the provided
        |      |       one
        |      | default: 1 [type: int]
        |_ max_steps
        |      | desc: maximum number of steps (-1 means until the end)
        |      | default: -1 [type: int]
        |_ runs_per_node
        |      | desc: maximum number of test cases for a single node (-1 means until
        |      |       the end)
        |      | default: -1 [type: int]
        |_ path
        |      | desc: graph path regexp to select nodes on which the disruptor should
        |      |       apply
        |      | default: None [type: str]
        |_ order
        |      | desc: when set to True, the walking order is strictly guided by the
        |      |       data structure. Otherwise, fuzz weight (if specified in the
        |      |       data model) is used for ordering
        |      | default: True [type: bool]
        |_ fix_all
        |      | desc: for each produced data, reevaluate the constraints on the whole
        |      |       graph
        |      | default: True [type: bool]
        |_ nt_only
        |      | desc: walk through non-terminal nodes only
        |      | default: False [type: bool]

Stateless Disruptors
====================

OP - Perform Operations on Nodes
--------------------------------

Description:
    Perform an operation on the nodes specified by the regexp path. @op is an operation that
    applies to a node and @params are a tuple containing the parameters that will be provided to
    @op. If no path is provided, the root node will be used.

Reference:
  :class:`framework.generic_data_makers.d_operate_on_nodes`

Parameters:
  .. code-block:: none

      parameters:
        |_ path
        |      | desc: Graph path regexp to select nodes on which the disruptor should
        |      |       apply.
        |      | default: None [type: str]
        |_ op
        |      | desc: The operation to perform on the selected nodes.
        |      | default: <function Node.clear_attr> [type: method, function]
        |_ params
        |      | desc: Tuple of parameters that will be provided to the operation.
        |      |       (default: MH.Attr.Mutable)
        |      | default: (2,) [type: tuple]
        |_ clone_node
        |      | desc: If True the dmaker will always return a copy of the node. (For
        |      |       stateless disruptors dealing with big data it can be useful
        |      |       to set it to False.)
        |      | default: False [type: bool]


MOD - Modify Node Contents
--------------------------

Description:
  Change the content of the nodes specified by the regexp path with
  the value privided as a parameter (use *node absorption*
  infrastructure). If no path is provided, the root node will be
  used.

Reference:
  :class:`framework.generic_data_makers.d_modify_nodes`

Parameters:
  .. code-block:: none

    parameters:
      |_ path
      |      | desc: graph path regexp to select nodes on which the disruptor should
      |      |       apply
      |      | default: None [type: str]
      |_ clone_node
      |      | desc: if True the dmaker will always return a copy of the node. (for
      |      |       stateless disruptors dealing with big data it can be useful
      |      |       to it to False)
      |      | default: False [type: bool]
      |_ value
      |      | desc: the new value to inject within the data
      |      | default: '' [type: str]
      |_ constraints
      |      | desc: constraints for the absorption of the new value
      |      | default: AbsNoCsts() [type: AbsCsts]



NEXT - Next Node Content
------------------------

Description:
  Move to the next content of the nodes from input data or from only
  a piece of it (if the parameter `path` is provided). Basically,
  unfreeze the nodes then freeze them again, which will consequently
  produce a new data.

Reference:
  :class:`framework.generic_data_makers.d_next_node_content`

Parameters:
  .. code-block:: none

    parameters:
      |_ path
      |      | desc: graph path regexp to select nodes on which the disruptor should
      |      |       apply
      |      | default: None [type: str]
      |_ clone_node
      |      | desc: if True the dmaker will always return a copy of the node. (for
      |      |       stateless disruptors dealing with big data it can be useful
      |      |       to it to False)
      |      | default: False [type: bool]
      |_ recursive
      |      | desc: apply the disruptor recursively
      |      | default: True [type: str]



FIX - Fix Data Constraints
--------------------------

Description:
  Release constraints from input data or from only a piece of it (if
  the parameter `path` is provided), then recompute them. By
  constraints we mean every generator (or function) nodes that may
  embeds constraints between nodes, and every node *existence
  conditions*.

  .. seealso:: Refer to :ref:`dm:pattern:existence-cond` for insight
           into existence conditions.

Reference:
  :class:`framework.generic_data_makers.d_fix_constraints`

Parameters:
  .. code-block:: none

    parameters:
      |_ path
      |      | desc: graph path regexp to select nodes on which the disruptor should
      |      |       apply
      |      | default: None [type: str]
      |_ clone_node
      |      | desc: if True the dmaker will always return a copy of the node. (for
      |      |       stateless disruptors dealing with big data it can be useful
      |      |       to it to False)
      |      | default: False [type: bool]


ALT - Alternative Node Configuration
------------------------------------

Description:
  Switch to an alternate configuration.

Reference:
  :class:`framework.generic_data_makers.d_switch_to_alternate_conf`

Parameters:
  .. code-block:: none

       parameters:
         |_ path
         |      | desc: graph path regexp to select nodes on which the disruptor should
         |      |       apply
         |      | default: None [type: str]
         |_ recursive
         |      | desc: does the reachable nodes from the selected ones need also to
         |      |       be changed?
         |      | default: True [type: bool]
         |_ conf
         |      | desc: change the configuration, with the one provided (by name), of
         |      |       all subnodes fetched by @path, one-by-one. [default value is
         |      |       set dynamically with the first-found existing alternate configuration]
         |      | default: None [type: str]


C - Node Corruption
-------------------

Description:
  Corrupt bits on some nodes of the data model.

Reference:
  :class:`framework.generic_data_makers.d_corrupt_node_bits`

Parameters:
  .. code-block:: none

       parameters:
         |_ path
         |      | desc: graph path regexp to select nodes on which the disruptor should
         |      |       apply
         |      | default: None [type: str]
         |_ nb
         |      | desc: apply corruption on @nb Nodes fetched randomly within the data
         |      |       model
         |      | default: 2 [type: int]
         |_ ascii
         |      | desc: enforce all outputs to be ascii 7bits
         |      | default: False [type: bool]
         |_ new_val
         |      | desc: if provided change the selected byte with the new one
         |      | default: None [type: str]


Cp - Corruption at Specific Position
------------------------------------

Description:
  Corrupt bit at a specific byte.

Reference:
  :class:`framework.generic_data_makers.d_corrupt_bits_by_position`

Parameters:
  .. code-block:: none

       parameters:
         |_ new_val
         |      | desc: if provided change the selected byte with the new one
         |      | default: None [type: str]
         |_ ascii
         |      | desc: enforce all outputs to be ascii 7bits
         |      | default: False [type: bool]
         |_ idx
         |      | desc: byte index to be corrupted (from 1 to data length)
         |      | default: 1 [type: int]


EXT - Make Use of an External Program
-------------------------------------

Description:
  Call an external program to deal with the data.

Reference:
  :class:`framework.generic_data_makers.d_call_external_program`

Parameters:
  .. code-block:: none

       parameters:
         |_ path
         |      | desc: graph path regexp to select nodes on which the disruptor should
         |      |       apply
         |      | default: None [type: str]
         |_ cmd
         |      | desc: the command
         |      | default: None [type: list, tuple, str]
         |_ file_mode
         |      | desc: if True the data will be provided through a file to the external
         |      |       program, otherwise it will be provided on the command line directly
         |      | default: True [type: bool]


SIZE - Truncate
---------------

Description:
  Truncate the data (or part of the data) to the provided size.

Reference:
  :class:`framework.generic_data_makers.d_max_size`

Parameters:
  .. code-block:: none

       parameters:
         |_ sz
         |      | desc: truncate the data (or part of the data) to the provided size
         |      | default: 10 [type: int]
         |_ path
         |      | desc: graph path regexp to select nodes on which the disruptor should
         |      |       apply
         |      | default: None [type: str]


STRUCT - Shake Up Data Structure
--------------------------------

Description:
  Disrupt the data model structure (replace ordered sections by
  unordered ones).

Reference:
  :class:`framework.generic_data_makers.d_fuzz_model_structure`

Parameters:
  .. code-block:: none

       parameters:
         |_ path
         |      | desc: graph path regexp to select nodes on which the disruptor should
         |      |       apply
         |      | default: None [type: str]



COPY - Shallow Copy Data
------------------------

Description:
  Shallow copy of the input data, which means: ignore its frozen
  state during the copy.

Reference:
  :class:`framework.generic_data_makers.d_shallow_copy`

.. note:: Random seeds are generally set while loading the data
          model. This disruptor enables you to reset the seeds for the
          input data.
