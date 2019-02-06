Changes
=======

0.2.25 (unreleased)
===================


0.2.24
======
- enforce consistent ordering by ``timepoint``, ``visit_code_sequence``
- in ``delete_for_subject_after_date``, bypass ``schedule`` filter with ``is_offstudy``

0.2.23
======
- in ``delete_for_subject_after_date``, add ``visit_schedule_name`` and ``schedule_name``
  to query of future appts (gh-4)
- increment timepoint decimal for interim (continuation) appointments (gh-4)
- enforce consistent ordering by ``timepoint``, ``visit_code_sequence``
- in ``delete_for_subject_after_date``, bypass ``schedule`` filter with ``is_offstudy``

5 feb 2019
==========

- start using changes document
