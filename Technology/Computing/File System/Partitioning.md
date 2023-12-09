When partitioning a storage device, we have two partitioning methods (or schemes) to choose from:

* **Master boot record (MBR) Scheme**.
* **GUID Partition Table (GPT) Scheme**.

Regardless of what partitioning scheme you choose, the first few blocks on the storage device will always contain critical data about your partitions.

The system's  _firmware_  uses these data structures to boot up the operating system on a partition.

#filesystem #computing 