REQ-012 (SEEN) The parsed STRENGTH value is first
  limited to the signed 64-bit range, then reduced
  to its lower 32 bits and read as a signed 32-bit
  integer, before the range check of REQ-004.
  Evidence: F-14 (ev_9d2, main), observations run 7.
  Platform: Linux x86-64 build only. Test: T-012.
